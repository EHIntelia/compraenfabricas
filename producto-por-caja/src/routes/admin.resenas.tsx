import { createFileRoute } from "@tanstack/react-router";
import { useServerFn } from "@tanstack/react-start";
import { useEffect, useState } from "react";
import { toast } from "sonner";
import { Header } from "@/lib/site";
import { CAJAS, cajaId } from "@/lib/cajas";
import { cambiarResena, crearResena, entrarAdminResenas, estadoAdminResenas, listarResenasAdmin } from "@/lib/resenas.functions";
import type { ResenaAdmin } from "@/lib/resenas.server";

export const Route = createFileRoute("/admin/resenas")({
  head: () => ({ meta: [{ title: "Reseñas — equipo" }, { name: "robots", content: "noindex, nofollow" }] }),
  component: AdminResenas,
});

const input = "mt-1 w-full rounded-xl border border-border bg-background px-4 py-3 text-base outline-none focus:ring-2 focus:ring-orange-400";
const GRAD = "linear-gradient(135deg, #F97316, #EA580C)";

function AdminResenas() {
  const estado = useServerFn(estadoAdminResenas);
  const [ok, setOk] = useState<boolean | null>(null);
  useEffect(() => {
    estado().then((r) => setOk(r.ok)).catch(() => setOk(false));
  }, [estado]);
  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header />
      <main className="mx-auto max-w-3xl px-4 py-10">
        <h1 className="text-3xl font-black">Reseñas de clientes</h1>
        <p className="mt-2 text-muted-foreground">
          Solo para el equipo. Da de alta reseñas de compradores reales. En el sitio solo se ven las <b>aprobadas</b>.
        </p>
        {ok === null ? <p className="mt-8">Cargando…</p> : ok ? <Panel /> : <Entrar onOk={() => setOk(true)} />}
      </main>
    </div>
  );
}

function Entrar({ onOk }: { onOk: () => void }) {
  const entrar = useServerFn(entrarAdminResenas);
  const [pw, setPw] = useState("");
  const [err, setErr] = useState("");
  return (
    <form
      className="mt-8 card-soft rounded-2xl p-6 space-y-4"
      onSubmit={async (e) => {
        e.preventDefault();
        setErr("");
        const r = await entrar({ data: { password: pw } }).catch(() => ({ ok: false as const }));
        if (r.ok) onOk();
        else setErr("Contraseña incorrecta.");
      }}
    >
      <label className="block">
        <span className="text-sm font-bold">Contraseña del equipo</span>
        <input type="password" className={input} value={pw} onChange={(e) => setPw(e.target.value)} autoComplete="current-password" />
      </label>
      {err && <p className="text-sm font-bold text-destructive">{err}</p>}
      <button type="submit" className="w-full min-h-12 rounded-xl font-black text-white" style={{ backgroundImage: GRAD }}>Entrar</button>
    </form>
  );
}

function Panel() {
  const listar = useServerFn(listarResenasAdmin);
  const crear = useServerFn(crearResena);
  const cambiar = useServerFn(cambiarResena);
  const [lista, setLista] = useState<ResenaAdmin[]>([]);
  const [enviando, setEnviando] = useState(false);
  const cargar = () => listar().then(setLista).catch(() => toast.error("No se pudo cargar la lista"));
  useEffect(() => {
    cargar();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function onSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const form = e.currentTarget;
    setEnviando(true);
    try {
      const r = await crear({ data: new FormData(form) });
      if (r.ok) {
        toast.success("Reseña guardada");
        form.reset();
        cargar();
      } else toast.error(r.error);
    } catch {
      toast.error("No se pudo guardar");
    } finally {
      setEnviando(false);
    }
  }

  async function accion(id: string, patch: { aprobada?: boolean; verificada?: boolean; borrar?: boolean }) {
    if (patch.borrar && !window.confirm("¿Borrar esta reseña?")) return;
    try {
      await cambiar({ data: { id, ...patch } });
      cargar();
    } catch {
      toast.error("No se pudo actualizar");
    }
  }

  const opciones = [...CAJAS].sort((a, b) => a.name.localeCompare(b.name));

  return (
    <>
      <form onSubmit={onSubmit} className="mt-8 card-soft rounded-2xl p-6 space-y-4">
        <h2 className="text-xl font-black">Nueva reseña</h2>
        <label className="block">
          <span className="text-sm font-bold">Producto</span>
          <select name="producto" className={input} defaultValue="general">
            <option value="general">General (no es de una caja en particular)</option>
            {opciones.map((c) => (
              <option key={cajaId(c)} value={cajaId(c)}>{cajaId(c)} — {c.name}</option>
            ))}
          </select>
        </label>
        <div className="grid gap-4 sm:grid-cols-2">
          <label className="block">
            <span className="text-sm font-bold">Nombre del cliente *</span>
            <input name="nombre" required className={input} />
          </label>
          <label className="block">
            <span className="text-sm font-bold">Ciudad</span>
            <input name="ciudad" className={input} placeholder="Ej. Guadalajara, Jal." />
          </label>
        </div>
        <label className="block">
          <span className="text-sm font-bold">Lo que dijo el cliente *</span>
          <textarea name="texto" required rows={4} className={input} />
        </label>
        <div className="grid gap-4 sm:grid-cols-2">
          <label className="block">
            <span className="text-sm font-bold">Calificación (1 a 5) *</span>
            <select name="calificacion" required className={input} defaultValue="">
              <option value="" disabled>Elige</option>
              {[5, 4, 3, 2, 1].map((n) => <option key={n} value={n}>{n} {"★".repeat(n)}</option>)}
            </select>
          </label>
          <label className="block">
            <span className="text-sm font-bold">Fecha</span>
            <input name="fecha" type="date" className={input} />
          </label>
        </div>
        <label className="block">
          <span className="text-sm font-bold">Foto o video (opcional, máx. 50 MB)</span>
          <input name="archivo" type="file" accept="image/*,video/mp4,video/quicktime" className={input} />
        </label>
        <label className="block">
          <span className="text-sm font-bold">…o link a la foto/video (opcional)</span>
          <input name="media_url" type="url" className={input} placeholder="https://…" />
        </label>
        <div className="flex flex-wrap gap-6">
          <label className="flex items-center gap-2 font-bold"><input type="checkbox" name="verificada" className="h-5 w-5" /> Compra verificada</label>
          <label className="flex items-center gap-2 font-bold"><input type="checkbox" name="aprobada" className="h-5 w-5" /> Aprobada (se publica)</label>
        </div>
        <button type="submit" disabled={enviando} className="w-full min-h-12 rounded-xl font-black text-white disabled:opacity-50" style={{ backgroundImage: GRAD }}>
          {enviando ? "Guardando…" : "Guardar reseña"}
        </button>
      </form>

      <h2 className="mt-10 text-xl font-black">Reseñas guardadas ({lista.length})</h2>
      <ul className="mt-4 space-y-3">
        {lista.map((r) => (
          <li key={r.id} className="card-soft rounded-2xl p-4">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <p className="font-black">{r.nombre}{r.ciudad ? ` · ${r.ciudad}` : ""}</p>
              <span className="text-sm">{"★".repeat(r.calificacion)}</span>
            </div>
            <p className="text-xs text-muted-foreground">{r.producto} · {r.fecha}{r.media_tipo ? ` · con ${r.media_tipo}` : ""}</p>
            <p className="mt-2 text-sm">{r.texto}</p>
            <div className="mt-3 flex flex-wrap gap-2 text-sm font-bold">
              <button type="button" onClick={() => accion(r.id, { aprobada: !r.aprobada })} className="rounded-lg border px-3 py-2" style={r.aprobada ? { background: "#DCFCE7", borderColor: "#16A34A" } : undefined}>
                {r.aprobada ? "✓ Aprobada (quitar)" : "Aprobar"}
              </button>
              <button type="button" onClick={() => accion(r.id, { verificada: !r.verificada })} className="rounded-lg border px-3 py-2">
                {r.verificada ? "✓ Verificada (quitar)" : "Marcar verificada"}
              </button>
              <button type="button" onClick={() => accion(r.id, { borrar: true })} className="rounded-lg border px-3 py-2 text-destructive">Borrar</button>
            </div>
          </li>
        ))}
      </ul>
    </>
  );
}
