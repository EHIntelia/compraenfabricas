// Solo servidor. Lectura pública (RLS: aprobada = true) y escrituras con service role.
import { publicClient } from "@/lib/blog/posts.server";

export type Resena = {
  id: string;
  producto: string;
  nombre: string;
  ciudad: string | null;
  texto: string;
  calificacion: number;
  media_url: string | null;
  media_tipo: "foto" | "video" | null;
  fecha: string;
  verificada: boolean;
};

export type ResenaAdmin = Resena & { aprobada: boolean; created_at: string };

const COLS = "id,producto,nombre,ciudad,texto,calificacion,media_url,media_tipo,fecha,verificada";

/** Primero las reseñas aprobadas de ese producto; si no hay, las generales. */
export async function fetchResenas(codigo: string): Promise<Resena[]> {
  const db = publicClient();
  const q = (producto: string) =>
    db.from("resenas").select(COLS).eq("aprobada", true).eq("producto", producto).order("fecha", { ascending: false }).limit(12);
  const propias = await q(codigo);
  if (propias.error) throw new Error(propias.error.message);
  if (propias.data && propias.data.length > 0) return propias.data as unknown as Resena[];
  const generales = await q("general");
  if (generales.error) throw new Error(generales.error.message);
  return (generales.data ?? []) as unknown as Resena[];
}
