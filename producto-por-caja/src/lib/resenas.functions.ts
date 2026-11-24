import { createServerFn } from "@tanstack/react-start";
import { useSession } from "@tanstack/react-start/server";
import { createHash, timingSafeEqual } from "node:crypto";
import type { Resena, ResenaAdmin } from "./resenas.server";

// ---------- Público ----------

export const getResenas = createServerFn({ method: "GET" })
  .inputValidator((d: { codigo: string }) => ({ codigo: String(d.codigo).slice(0, 60) }))
  .handler(async ({ data }): Promise<Resena[]> => {
    const { fetchResenas } = await import("./resenas.server");
    try {
      return await fetchResenas(data.codigo);
    } catch {
      return []; // si falla la base, la página se muestra sin reseñas
    }
  });

// ---------- Equipo (protegido con contraseña: RESENAS_ADMIN_PASSWORD) ----------

type AdminSession = { ok?: boolean };

function sessionConfig() {
  return {
    password: process.env["SESSION_SECRET"]!,
    name: "resenas-admin",
    maxAge: 60 * 60 * 24 * 30,
    cookie: { httpOnly: true, secure: true, sameSite: "lax" as const, path: "/" },
  };
}

function iguales(a: string, b: string) {
  const ha = createHash("sha256").update(a, "utf8").digest();
  const hb = createHash("sha256").update(b, "utf8").digest();
  return timingSafeEqual(ha, hb);
}

async function exigirAdmin() {
  const s = await useSession<AdminSession>(sessionConfig());
  if (!s.data.ok) throw new Error("NO_AUTORIZADO");
}

export const entrarAdminResenas = createServerFn({ method: "POST" })
  .inputValidator((d: { password: string }) => d)
  .handler(async ({ data }) => {
    const expected = process.env["RESENAS_ADMIN_PASSWORD"];
    if (!expected) throw new Error("Falta configurar RESENAS_ADMIN_PASSWORD");
    if (typeof data?.password !== "string" || !iguales(data.password.trim(), expected)) return { ok: false as const };
    const s = await useSession<AdminSession>(sessionConfig());
    await s.update({ ok: true });
    return { ok: true as const };
  });

export const estadoAdminResenas = createServerFn({ method: "GET" }).handler(async () => {
  const s = await useSession<AdminSession>(sessionConfig());
  return { ok: !!s.data.ok };
});

export const listarResenasAdmin = createServerFn({ method: "GET" }).handler(async (): Promise<ResenaAdmin[]> => {
  await exigirAdmin();
  const { supabaseAdmin } = await import("@/integrations/supabase/client.server");
  const { data, error } = await supabaseAdmin.from("resenas").select("*").order("created_at", { ascending: false }).limit(500);
  if (error) throw new Error(error.message);
  return (data ?? []) as unknown as ResenaAdmin[];
});

const MAX_MB = 50;

/** Alta de reseña. Recibe FormData (para poder subir foto o video). */
export const crearResena = createServerFn({ method: "POST" })
  .inputValidator((d: FormData) => {
    if (!(d instanceof FormData)) throw new Error("Datos inválidos");
    return d;
  })
  .handler(async ({ data: fd }) => {
    await exigirAdmin();
    const txt = (k: string) => String(fd.get(k) ?? "").trim();
    const producto = txt("producto") || "general";
    const nombre = txt("nombre");
    const texto = txt("texto");
    const calificacion = Number(txt("calificacion"));
    if (!nombre || !texto) return { ok: false as const, error: "Falta el nombre o el texto." };
    if (!Number.isInteger(calificacion) || calificacion < 1 || calificacion > 5) return { ok: false as const, error: "La calificación debe ser de 1 a 5." };

    const { supabaseAdmin } = await import("@/integrations/supabase/client.server");

    let media_url: string | null = txt("media_url") || null;
    let media_tipo: "foto" | "video" | null = media_url ? (/\.(mp4|mov|webm)(\?|$)/i.test(media_url) ? "video" : "foto") : null;
    const file = fd.get("archivo");
    if (file instanceof File && file.size > 0) {
      if (file.size > MAX_MB * 1024 * 1024) return { ok: false as const, error: `El archivo pesa más de ${MAX_MB} MB.` };
      const esVideo = file.type.startsWith("video/");
      const esFoto = file.type.startsWith("image/");
      if (!esVideo && !esFoto) return { ok: false as const, error: "Sube una foto o un video." };
      const ext = (file.name.split(".").pop() || (esVideo ? "mp4" : "jpg")).toLowerCase().replace(/[^a-z0-9]/g, "");
      const path = `${producto}/${Date.now()}-${Math.random().toString(36).slice(2, 8)}.${ext}`;
      const up = await supabaseAdmin.storage.from("resenas").upload(path, file, { contentType: file.type, upsert: false });
      if (up.error) return { ok: false as const, error: `No se pudo subir el archivo: ${up.error.message}` };
      media_url = supabaseAdmin.storage.from("resenas").getPublicUrl(path).data.publicUrl;
      media_tipo = esVideo ? "video" : "foto";
    }

    const fecha = txt("fecha") || new Date().toISOString().slice(0, 10);
    const { error } = await supabaseAdmin.from("resenas").insert({
      producto,
      nombre,
      ciudad: txt("ciudad") || null,
      texto,
      calificacion,
      media_url,
      media_tipo,
      fecha,
      verificada: fd.get("verificada") === "on",
      aprobada: fd.get("aprobada") === "on",
    });
    if (error) return { ok: false as const, error: error.message };
    return { ok: true as const };
  });

export const cambiarResena = createServerFn({ method: "POST" })
  .inputValidator((d: { id: string; aprobada?: boolean; verificada?: boolean; borrar?: boolean }) => d)
  .handler(async ({ data }) => {
    await exigirAdmin();
    const { supabaseAdmin } = await import("@/integrations/supabase/client.server");
    if (data.borrar) {
      const { error } = await supabaseAdmin.from("resenas").delete().eq("id", data.id);
      if (error) throw new Error(error.message);
      return { ok: true };
    }
    const patch: { aprobada?: boolean; verificada?: boolean } = {};
    if (typeof data.aprobada === "boolean") patch.aprobada = data.aprobada;
    if (typeof data.verificada === "boolean") patch.verificada = data.verificada;
    const { error } = await supabaseAdmin.from("resenas").update(patch).eq("id", data.id);
    if (error) throw new Error(error.message);
    return { ok: true };
  });
