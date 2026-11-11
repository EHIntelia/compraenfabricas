import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { useEffect, useRef, useState } from "react";
import { toast } from "sonner";
import {
  BadgeCheck,
  CalendarDays,
  Check,
  Expand,
  FileText,
  Globe,
  Lock,
  MapPin,
  MessageCircle,
  Package,
  Play,
  Receipt,
  Share2,
  ShieldCheck,
  Truck,
  Video,
  X,
} from "lucide-react";
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Footer, Header } from "@/lib/site";
import { cajaId, type Caja } from "@/lib/cajas";
import { fotoCaja, galeriaCaja, ogImagenCaja, videoCaja } from "@/lib/cajas-media";
import { categoriaDe, categoriaLabel, track } from "@/lib/tracking";
import { AUTHOR_NAME, AUTHOR_PHOTO, BASE_URL, abs, breadcrumbLd, ld } from "@/lib/blog/seo";
import {
  apartadoDe,
  buscarCaja,
  disponible,
  fmt,
  margenEjemplo,
  nombreModelo,
  precioPieza,
  similares,
  usdDe,
  waApartar,
  waDuda,
  waPedirVideo,
  waVendida,
} from "@/lib/producto";
import { CLASE_BANNER, CONFIANZA, FAQ_PRODUCTO } from "@/config/producto";
import { getResenas } from "@/lib/resenas.functions";
import type { Resena } from "@/lib/resenas.server";

const GRAD = "linear-gradient(135deg, #F97316, #EA580C)";
const ORANGE = "#EA580C";

export const Route = createFileRoute("/producto/$codigo")({
  loader: async ({ params }) => {
    const caja = buscarCaja(params.codigo);
    if (!caja) throw notFound();
    const id = cajaId(caja);
    const resenas: Resena[] = disponible(caja) ? await getResenas({ data: { codigo: id } }).catch(() => []) : [];
    return { id, resenas };
  },
  head: ({ loaderData }) => {
    const c = loaderData ? buscarCaja(loaderData.id) : undefined;
    if (!c) return { meta: [{ title: "Caja no encontrada | Compra en Fábricas de China" }, { name: "robots", content: "noindex" }] };
    const id = cajaId(c);
    const url = `${BASE_URL}/producto/${encodeURIComponent(id)}`;
    if (!disponible(c)) {
      return {
        meta: [
          { title: `Caja vendida: ${c.name} | Compra en Fábricas de China` },
          { name: "description", content: "Esta caja ya se vendió. Mira otras cajas disponibles directo de fábrica, con flete desde China incluido." },
          { name: "robots", content: "noindex, follow" },
        ],
        links: [{ rel: "canonical", href: url }],
      };
    }
    const pp = precioPieza(c);
    const title = `${nombreModelo(c)} · $${fmt(pp)} MXN por pieza | Compra en Fábricas`;
    const description = `$${fmt(pp)} MXN (~$${usdDe(c.priceMxnPerPiece)} USD) por pieza · Caja de ${c.pieces} piezas · Flete desde China incluido. Aparta con el 20%: $${fmt(apartadoDe(c))} MXN.`;
    const og = ogImagenCaja(c);
    const video = videoCaja(c);
    const meta: Record<string, string>[] = [
      { title },
      { name: "description", content: description },
      { property: "og:title", content: `${nombreModelo(c)} · $${fmt(pp)} MXN por pieza` },
      { property: "og:description", content: description },
      { property: "og:url", content: url },
      { property: "og:type", content: "product" },
      { property: "og:locale", content: "es_MX" },
      { property: "og:site_name", content: "Compra en Fábricas de China" },
      { property: "product:price:amount", content: String(c.priceMxn) },
      { property: "product:price:currency", content: "MXN" },
      { name: "twitter:card", content: "summary_large_image" },
      { name: "twitter:title", content: title },
      { name: "twitter:description", content: description },
    ];
    if (og) {
      meta.push(
        { property: "og:image", content: abs(og.url) },
        { property: "og:image:secure_url", content: abs(og.url) },
        { property: "og:image:type", content: "image/jpeg" },
        { property: "og:image:width", content: String(og.width) },
        { property: "og:image:height", content: String(og.height) },
        { property: "og:image:alt", content: `Caja de ${c.pieces} piezas de ${c.name}` },
        { name: "twitter:image", content: abs(og.url) },
      );
    }
    if (video) {
      meta.push(
        { property: "og:video", content: abs(video) },
        { property: "og:video:secure_url", content: abs(video) },
        { property: "og:video:type", content: "video/mp4" },
        { property: "og:video:width", content: "720" },
        { property: "og:video:height", content: "406" },
      );
    }
    const foto = fotoCaja(c);
    return {
      meta,
      links: [{ rel: "canonical", href: url }],
      scripts: [
        ld({
          "@context": "https://schema.org",
          "@type": "Product",
          name: nombreModelo(c),
          sku: id,
          ...(c.model ? { model: c.model } : {}),
          category: categoriaLabel(categoriaDe(c.name)),
          description: `Caja de ${c.pieces} piezas. Precio por pieza $${fmt(pp)} MXN con flete desde China incluido.`,
          ...(foto ? { image: [abs(foto)] } : {}),
          offers: {
            "@type": "Offer",
            url,
            priceCurrency: "MXN",
            price: c.priceMxn,
            availability: c.apartada ? "https://schema.org/LimitedAvailability" : "https://schema.org/InStock",
            seller: { "@id": `${BASE_URL}/#organization` },
          },
        }),
        ld(
          breadcrumbLd([
            { name: "Inicio", url: BASE_URL },
            { name: "Cajas", url: `${BASE_URL}/productos` },
            { name: c.name, url },
          ]),
        ),
      ],
    };
  },
  component: ProductoPage,
  notFoundComponent: () => <CajaNoDisponible titulo="No encontramos esta caja" />,
});

// ============================================================
// Página
// ============================================================

function ProductoPage() {
  const { id, resenas } = Route.useLoaderData();
  const c = buscarCaja(id)!;
  if (!disponible(c)) return <CajaNoDisponible caja={c} titulo="Esta caja ya se vendió" />;
  return <ProductoDisponible c={c} resenas={resenas} />;
}

function ProductoDisponible({ c, resenas }: { c: Caja; resenas: Resena[] }) {
  const id = cajaId(c);
  const foto = fotoCaja(c);
  const video = videoCaja(c);
  const fotos = galeriaCaja(c);
  const margen = margenEjemplo(c);
  const apartado = apartadoDe(c);
  const datos = { content_name: nombreModelo(c), content_ids: [id], content_category: categoriaLabel(categoriaDe(c.name)), value: c.priceMxn, currency: "MXN" };

  return (
    <div className="min-h-screen bg-background text-foreground overflow-x-hidden pb-24 lg:pb-0">
      <Header />
      <main>
        {/* 1. VIDEO — hasta arriba, ancho completo en celular */}
        <section className="bg-black">
          <div className="mx-auto max-w-4xl">
            <VideoProducto c={c} src={video} poster={foto} onPlay={() => track("track", "ViewContent", datos)} />
          </div>
        </section>

        <div className="mx-auto max-w-4xl px-4">
          {/* Galería de fotos */}
          {fotos.length > 0 && <Galeria fotos={fotos} nombre={c.name} />}

          {/* 2. INFO DEL PRODUCTO */}
          <section className="mt-6">
            <nav aria-label="Migas de pan" className="text-sm text-muted-foreground">
              <Link to="/productos" className="font-semibold hover:text-foreground">← Todas las cajas</Link>
            </nav>
            <div className="mt-3 flex flex-wrap items-center gap-2">
              {c.apartada ? (
                <span className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-sm font-black text-white" style={{ background: "#111827" }}>
                  <Lock className="h-4 w-4" /> Caja apartada
                </span>
              ) : (
                <span className="inline-flex items-center gap-1.5 rounded-full px-3 py-1 text-sm font-black" style={{ background: "#DCFCE7", color: "#166534" }}>
                  <span className="h-2 w-2 rounded-full" style={{ background: "#16A34A" }} /> Disponible: 1 caja
                </span>
              )}
              <span className="font-mono text-sm text-muted-foreground">Código {id}</span>
            </div>
            <h1 className="mt-3 text-3xl sm:text-4xl font-black leading-tight">{c.name}</h1>
            {c.model && <p className="mt-1 text-lg font-bold text-muted-foreground">Modelo: {c.model}</p>}

            {/* Precio por pieza, grande */}
            <div className="mt-5 rounded-3xl p-5 sm:p-6" style={{ background: "#FFF8F5", border: "2px solid #FED7AA" }}>
              <p className="text-sm font-black uppercase tracking-wide" style={{ color: ORANGE }}>Precio por pieza</p>
              <p className="mt-1 flex flex-wrap items-baseline gap-x-3">
                <span className="text-5xl sm:text-6xl font-black text-transparent bg-clip-text" style={{ backgroundImage: GRAD }}>
                  ${fmt(precioPieza(c))}
                </span>
                <span className="text-2xl font-black">MXN</span>
                <span className="text-xl font-bold text-muted-foreground">~${fmt(usdDe(c.priceMxnPerPiece))} USD</span>
              </p>
              <p className="mt-2 inline-flex items-center gap-1.5 text-base font-bold" style={{ color: "#166534" }}>
                <Check className="h-5 w-5" /> Flete desde China incluido
              </p>
            </div>

            {/* Piezas, total y apartado */}
            <dl className="mt-4 grid grid-cols-1 gap-3 sm:grid-cols-3">
              <Dato titulo="Piezas por caja" valor={`${c.pieces} piezas`} />
              <Dato titulo="Precio total de la caja" valor={`$${fmt(c.priceMxn)} MXN`} sub={`~$${fmt(usdDe(c.priceMxn))} USD`} />
              <Dato titulo="Apartas con el 20%" valor={`$${fmt(apartado)} MXN`} sub={`Resto: $${fmt(c.priceMxn - apartado)} MXN`} destacado />
            </dl>

            {/* Margen de ejemplo (solo si hay precio de reventa capturado) */}
            {margen && margen.porCaja > 0 && (
              <p className="mt-4 rounded-2xl p-4 text-base" style={{ background: "#F0FDF4", color: "#14532D" }}>
                <b>Margen de ejemplo:</b> si vendes cada pieza a <b>${fmt(margen.venta)} MXN</b>, ganas <b>~${fmt(margen.porCaja)} MXN por caja</b>{" "}
                (${fmt(margen.porPieza)} por pieza). <span className="text-sm opacity-80">Antes del envío nacional y tus gastos de venta.</span>
              </p>
            )}

            {/* Peso y medidas */}
            {(c.pesoKg || c.medidasCm) && (
              <p className="mt-4 flex items-start gap-2 text-base">
                <Package className="h-5 w-5 shrink-0 mt-0.5" style={{ color: ORANGE }} />
                <span>
                  <b>Caja master:</b> {c.pesoKg ? `${c.pesoKg} kg` : ""}
                  {c.pesoKg && c.medidasCm ? " · " : ""}
                  {c.medidasCm ? `${c.medidasCm.largo} × ${c.medidasCm.ancho} × ${c.medidasCm.alto} cm` : ""}
                </span>
              </p>
            )}
            <p className="mt-2 flex items-start gap-2 text-base">
              <Truck className="h-5 w-5 shrink-0 mt-0.5" style={{ color: ORANGE }} />
              <span>
                Envío nacional aparte.{" "}
                <Link to="/cotizar-envio" search={{ caja: id }} className="font-bold underline underline-offset-4" style={{ color: ORANGE }}>
                  Cotiza el envío a tu ciudad
                </Link>
              </span>
            </p>
          </section>

          {/* 3. BOTONES */}
          <section className="mt-6 space-y-3">
            {!c.apartada && (
              <a
                href={waApartar(c)}
                target="_blank"
                rel="noopener noreferrer"
                data-tracked="1"
                onClick={() => track("track", "Contact", { ...datos, page: "/producto" })}
                className="hidden lg:flex w-full min-h-16 items-center justify-center gap-2 rounded-2xl px-6 py-4 text-xl font-black text-white shadow-lg"
                style={{ backgroundImage: GRAD }}
              >
                <Lock className="h-6 w-6" /> Apartar con ${fmt(apartado)} (20%)
              </a>
            )}
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
              <a
                href={waDuda(c)}
                target="_blank"
                rel="noopener noreferrer"
                data-tracked="1"
                onClick={() => track("track", "Contact", { ...datos, page: "/producto", tipo: "duda" })}
                className="flex min-h-14 items-center justify-center gap-2 rounded-2xl border-2 px-4 py-3 text-lg font-black"
                style={{ borderColor: "#25D366", color: "#166534" }}
              >
                <MessageCircle className="h-5 w-5" /> Tengo una duda
              </a>
              <BotonCompartir c={c} />
            </div>
            <Link
              to="/cotizador"
              search={{ caja: id }}
              className="flex items-center justify-center gap-2 rounded-2xl px-4 py-3 text-base font-bold"
              style={{ background: "#F5F5F4" }}
            >
              <Globe className="h-5 w-5" style={{ color: ORANGE }} /> ¿Estás fuera de México? Cotiza envío internacional
            </Link>
          </section>

          {/* 5. CONFIANZA */}
          <section className="mt-12">
            <h2 className="text-2xl sm:text-3xl font-black">Compra con confianza</h2>
            <ul className="mt-5 grid gap-3 sm:grid-cols-2">
              {CONFIANZA.map((t, i) => (
                <li key={t} className="flex items-start gap-3 rounded-2xl p-4 card-soft text-base">
                  <span className="grid h-9 w-9 shrink-0 place-items-center rounded-full text-white" style={{ backgroundImage: GRAD }}>
                    {[<FileText key="a" className="h-5 w-5" />, <Receipt key="b" className="h-5 w-5" />, <Video key="c" className="h-5 w-5" />, <MapPin key="d" className="h-5 w-5" />, <ShieldCheck key="e" className="h-5 w-5" />][i] ?? <Check className="h-5 w-5" />}
                  </span>
                  <span className="pt-1.5 font-semibold">{t}</span>
                </li>
              ))}
              <li className="sm:col-span-2">
                <Link to="/autor/eduardo-hernandez" className="flex items-center gap-4 rounded-2xl p-4 card-soft hover:ring-2 hover:ring-orange-300">
                  <img src={AUTHOR_PHOTO} alt={AUTHOR_NAME} width={64} height={64} loading="lazy" className="h-16 w-16 rounded-full object-cover" />
                  <span className="text-base">
                    <b>{AUTHOR_NAME}</b>, más de 26 años importando de China.
                    <span className="block font-bold" style={{ color: ORANGE }}>Conoce a Eduardo →</span>
                  </span>
                </Link>
              </li>
            </ul>
          </section>

          {/* 6. RESEÑAS (solo reales y aprobadas; si no hay, no se muestra nada) */}
          {resenas.length > 0 && <Resenas resenas={resenas} />}

          {/* 7. FAQ */}
          <section className="mt-12">
            <h2 className="text-2xl sm:text-3xl font-black">Preguntas frecuentes</h2>
            <Accordion type="single" collapsible className="mt-4 card-soft rounded-2xl px-5">
              {FAQ_PRODUCTO.map((f, n) => (
                <AccordionItem key={f.q} value={`f${n}`}>
                  <AccordionTrigger className="text-left text-base font-bold">{f.q}</AccordionTrigger>
                  <AccordionContent className="text-base text-muted-foreground">
                    {f.a}
                    {f.link && (
                      <>
                        {" "}
                        <a href={`${f.link.href}?caja=${encodeURIComponent(id)}`} className="font-bold underline underline-offset-4" style={{ color: ORANGE }}>
                          {f.link.texto}
                        </a>
                      </>
                    )}
                  </AccordionContent>
                </AccordionItem>
              ))}
            </Accordion>
          </section>

          {/* 9. OTRAS CAJAS */}
          <OtrasCajas cajas={similares(c, 6)} titulo="Otras cajas disponibles" />

          <BannerClase />
        </div>
      </main>

      <div className="mt-12">
        <Footer />
      </div>

      {/* Botón principal fijo abajo en celular */}
      {c.apartada ? (
        <div className="fixed inset-x-0 bottom-0 z-50 border-t border-border bg-background/95 p-3 backdrop-blur lg:hidden">
          <a href={waDuda(c)} target="_blank" rel="noopener noreferrer" className="flex min-h-14 w-full items-center justify-center gap-2 rounded-2xl text-lg font-black text-white" style={{ background: "#25D366" }}>
            <MessageCircle className="h-5 w-5" /> Avísame si se libera
          </a>
        </div>
      ) : (
        <div className="fixed inset-x-0 bottom-0 z-50 border-t border-border bg-background/95 p-3 backdrop-blur lg:hidden" style={{ paddingBottom: "max(0.75rem, env(safe-area-inset-bottom))" }}>
          <a
            href={waApartar(c)}
            target="_blank"
            rel="noopener noreferrer"
            data-tracked="1"
            onClick={() => track("track", "Contact", { ...datos, page: "/producto" })}
            className="flex min-h-14 w-full items-center justify-center gap-2 rounded-2xl text-lg font-black text-white shadow-lg"
            style={{ backgroundImage: GRAD }}
          >
            <Lock className="h-5 w-5" /> Apartar con ${fmt(apartado)} (20%)
          </a>
        </div>
      )}
    </div>
  );
}

function Dato({ titulo, valor, sub, destacado }: { titulo: string; valor: string; sub?: string; destacado?: boolean }) {
  return (
    <div className="rounded-2xl p-4 card-soft" style={destacado ? { background: "#FFEDD5" } : undefined}>
      <dt className="text-sm font-bold text-muted-foreground">{titulo}</dt>
      <dd className="mt-1 text-2xl font-black">{valor}</dd>
      {sub && <dd className="text-sm font-semibold text-muted-foreground">{sub}</dd>}
    </div>
  );
}

// ============================================================
// Video (lo más importante)
// ============================================================

type VideoEl = HTMLVideoElement & { webkitEnterFullscreen?: () => void; webkitRequestFullscreen?: () => void };

function VideoProducto({ c, src, poster, onPlay }: { c: Caja; src?: string; poster?: string; onPlay: () => void }) {
  const ref = useRef<VideoEl>(null);
  const [empezo, setEmpezo] = useState(false);
  const [fallo, setFallo] = useState(!src);
  const visto = useRef(false);

  // Si el error ocurrió antes de que React conectara los eventos (SSR + hidratación), lo detectamos aquí.
  useEffect(() => {
    const v = ref.current;
    if (v && (v.error || v.networkState === HTMLMediaElement.NETWORK_NO_SOURCE)) setFallo(true);
  }, []);

  function reproducir() {
    const v = ref.current;
    if (!v) return;
    setEmpezo(true);
    const p = v.play();
    if (p && typeof p.catch === "function") p.catch(() => { /* quedan los controles nativos para que el usuario toque play */ });
  }

  function pantallaCompleta() {
    const v = ref.current;
    if (!v) return;
    setEmpezo(true);
    try {
      if (document.fullscreenEnabled && v.requestFullscreen) {
        v.requestFullscreen().catch(() => v.webkitEnterFullscreen?.());
      } else if (v.webkitEnterFullscreen) {
        v.webkitEnterFullscreen(); // iPhone
      } else if (v.webkitRequestFullscreen) {
        v.webkitRequestFullscreen();
      }
    } catch {
      /* sin pantalla completa: sigue en la página */
    }
    v.play().catch(() => {});
  }

  if (fallo) {
    return (
      <div>
        <div className="relative aspect-video w-full overflow-hidden bg-black">
          {poster ? (
            <img src={poster} alt={c.name} fetchPriority="high" className="h-full w-full object-contain" />
          ) : (
            <div className="grid h-full w-full place-items-center text-white/70"><Package className="h-16 w-16" /></div>
          )}
        </div>
        <div className="bg-black px-4 pb-4 pt-3">
          <a
            href={waPedirVideo(c)}
            target="_blank"
            rel="noopener noreferrer"
            className="flex min-h-14 w-full items-center justify-center gap-2 rounded-2xl text-lg font-black text-white"
            style={{ background: "#25D366" }}
          >
            <MessageCircle className="h-5 w-5" /> Pedir el video por WhatsApp
          </a>
        </div>
      </div>
    );
  }

  return (
    <div>
      <div className="relative aspect-video w-full overflow-hidden bg-black">
        <video
          ref={ref}
          className="absolute inset-0 h-full w-full object-contain"
          src={src}
          poster={poster}
          controls={empezo}
          playsInline
          webkit-playsinline="true"
          x5-playsinline="true"
          preload="metadata"
          aria-label={`Video de ${c.name}`}
          onPlay={() => {
            setEmpezo(true);
            if (!visto.current) {
              visto.current = true;
              onPlay();
            }
          }}
          onError={() => setFallo(true)}
        />
        {!empezo && (
          <button
            type="button"
            onClick={reproducir}
            aria-label={`Reproducir video de ${c.name}`}
            className="absolute inset-0 flex flex-col items-center justify-center gap-3"
            style={{ background: "linear-gradient(to top, rgba(0,0,0,0.55), rgba(0,0,0,0.1))" }}
          >
            <span className="grid h-24 w-24 place-items-center rounded-full shadow-2xl" style={{ backgroundImage: GRAD }}>
              <Play className="h-12 w-12 translate-x-0.5 fill-white text-white" />
            </span>
            <span className="rounded-full bg-black/60 px-4 py-1.5 text-base font-black text-white">Ver video</span>
          </button>
        )}
      </div>
      <div className="flex items-center justify-center gap-3 bg-black px-4 py-3">
        <button
          type="button"
          onClick={pantallaCompleta}
          className="flex min-h-12 flex-1 items-center justify-center gap-2 rounded-xl border border-white/30 px-4 text-base font-bold text-white sm:flex-none"
        >
          <Expand className="h-5 w-5" /> Ver en pantalla completa
        </button>
      </div>
    </div>
  );
}

// ============================================================
// Galería
// ============================================================

function Galeria({ fotos, nombre }: { fotos: string[]; nombre: string }) {
  const [abierta, setAbierta] = useState<number | null>(null);
  return (
    <section className="mt-5">
      <h2 className="sr-only">Fotos</h2>
      <div className="-mx-4 flex snap-x snap-mandatory gap-3 overflow-x-auto px-4 pb-2" style={{ scrollbarWidth: "none" }}>
        {fotos.map((src, i) => (
          <button
            key={src}
            type="button"
            onClick={() => setAbierta(i)}
            className="relative aspect-video w-[70%] shrink-0 snap-start overflow-hidden rounded-xl bg-muted sm:w-[32%]"
            aria-label={`Ver foto ${i + 1} de ${nombre}`}
          >
            <img src={src} alt={`${nombre} — foto ${i + 1}`} loading="lazy" decoding="async" className="h-full w-full object-cover" />
          </button>
        ))}
      </div>
      {abierta !== null && (
        <div className="fixed inset-0 z-[60] flex flex-col bg-black/95" role="dialog" aria-label={`Foto de ${nombre}`}>
          <div className="flex justify-end p-3">
            <button type="button" onClick={() => setAbierta(null)} aria-label="Cerrar" className="grid h-12 w-12 place-items-center rounded-full bg-white/15 text-white">
              <X className="h-6 w-6" />
            </button>
          </div>
          <div className="flex flex-1 items-center justify-center px-2" onClick={() => setAbierta(null)}>
            <img src={fotos[abierta]} alt={nombre} className="max-h-full max-w-full object-contain" />
          </div>
          {fotos.length > 1 && (
            <div className="flex justify-center gap-3 p-4">
              <button type="button" className="min-h-12 rounded-xl bg-white/15 px-5 font-bold text-white" onClick={() => setAbierta((abierta - 1 + fotos.length) % fotos.length)}>← Anterior</button>
              <button type="button" className="min-h-12 rounded-xl bg-white/15 px-5 font-bold text-white" onClick={() => setAbierta((abierta + 1) % fotos.length)}>Siguiente →</button>
            </div>
          )}
        </div>
      )}
    </section>
  );
}

// ============================================================
// Compartir
// ============================================================

function BotonCompartir({ c }: { c: Caja }) {
  async function compartir() {
    const url = `${BASE_URL}/producto/${encodeURIComponent(cajaId(c))}`;
    const text = `${c.name}: $${fmt(precioPieza(c))} MXN por pieza, caja de ${c.pieces} piezas, flete desde China incluido.`;
    track("trackCustom", "Compartir", { content_ids: [cajaId(c)] });
    if (typeof navigator !== "undefined" && navigator.share) {
      try {
        await navigator.share({ title: c.name, text, url });
        return;
      } catch (e) {
        if (e instanceof DOMException && e.name === "AbortError") return;
      }
    }
    try {
      await navigator.clipboard.writeText(url);
      toast.success("Link copiado");
    } catch {
      window.prompt("Copia el link:", url);
    }
  }
  return (
    <button
      type="button"
      data-tracked="1"
      onClick={compartir}
      className="flex min-h-14 items-center justify-center gap-2 rounded-2xl border-2 px-4 py-3 text-lg font-black"
      style={{ borderColor: "#FED7AA", color: ORANGE }}
    >
      <Share2 className="h-5 w-5" /> Compartir
    </button>
  );
}

// ============================================================
// Reseñas reales
// ============================================================

function Resenas({ resenas }: { resenas: Resena[] }) {
  return (
    <section className="mt-12">
      <h2 className="text-2xl sm:text-3xl font-black">Lo que dicen nuestros clientes</h2>
      <ul className="mt-5 grid gap-4 sm:grid-cols-2">
        {resenas.map((r) => (
          <li key={r.id} className="card-soft rounded-2xl p-5">
            {r.media_url && r.media_tipo === "video" && (
              <video className="mb-3 aspect-video w-full rounded-xl bg-black object-contain" src={r.media_url} controls playsInline preload="none" />
            )}
            {r.media_url && r.media_tipo === "foto" && (
              <img src={r.media_url} alt={`Foto de ${r.nombre}`} loading="lazy" className="mb-3 aspect-video w-full rounded-xl object-cover" />
            )}
            <p className="text-lg" aria-label={`${r.calificacion} de 5`} style={{ color: "#F59E0B" }}>
              {"★".repeat(r.calificacion)}
              <span className="text-muted-foreground/40">{"★".repeat(5 - r.calificacion)}</span>
            </p>
            <p className="mt-2 text-base">“{r.texto}”</p>
            <p className="mt-3 text-sm font-black">
              {r.nombre}
              {r.ciudad ? <span className="font-semibold text-muted-foreground"> · {r.ciudad}</span> : null}
            </p>
            <p className="mt-1 flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
              <span>{new Intl.DateTimeFormat("es-MX", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" }).format(new Date(r.fecha))}</span>
              {r.verificada && (
                <span className="inline-flex items-center gap-1 font-bold" style={{ color: "#166534" }}>
                  <BadgeCheck className="h-4 w-4" /> Compra verificada
                </span>
              )}
            </p>
          </li>
        ))}
      </ul>
    </section>
  );
}

// ============================================================
// Otras cajas + banner de la clase
// ============================================================

function OtrasCajas({ cajas, titulo }: { cajas: Caja[]; titulo: string }) {
  if (cajas.length === 0) return null;
  return (
    <section className="mt-12">
      <h2 className="text-2xl sm:text-3xl font-black">{titulo}</h2>
      <div className="-mx-4 mt-4 flex snap-x snap-mandatory gap-4 overflow-x-auto px-4 pb-3" style={{ scrollbarWidth: "none" }}>
        {cajas.map((x) => (
          <TarjetaCaja key={cajaId(x)} c={x} className="w-[75%] shrink-0 snap-start sm:w-[45%] lg:w-[31%]" />
        ))}
      </div>
    </section>
  );
}

function TarjetaCaja({ c, className = "" }: { c: Caja; className?: string }) {
  const foto = fotoCaja(c);
  return (
    <Link to="/producto/$codigo" params={{ codigo: cajaId(c) }} className={`card-soft flex flex-col overflow-hidden rounded-2xl ${className}`}>
      <div className="relative aspect-video w-full bg-muted">
        {foto ? (
          <img src={foto} alt={c.name} loading="lazy" decoding="async" className="h-full w-full object-cover" />
        ) : (
          <div className="grid h-full w-full place-items-center text-muted-foreground"><Package className="h-10 w-10" /></div>
        )}
        <span className="absolute bottom-2 left-2 inline-flex items-center gap-1 rounded-full bg-black/70 px-2.5 py-1 text-xs font-bold text-white">
          <Play className="h-3 w-3 fill-white" /> Video
        </span>
      </div>
      <div className="flex flex-1 flex-col p-4">
        <p className="font-black leading-snug line-clamp-2">{c.name}</p>
        <p className="mt-1 text-sm text-muted-foreground">{c.pieces} piezas · flete incluido</p>
        <p className="mt-auto pt-2 text-xl font-black" style={{ color: ORANGE }}>
          ${fmt(precioPieza(c))} MXN <span className="text-sm font-bold text-muted-foreground">por pieza</span>
        </p>
      </div>
    </Link>
  );
}

function BannerClase() {
  if (Date.now() > new Date(CLASE_BANNER.ocultarDespuesDe).getTime()) return null;
  return (
    <a href={CLASE_BANNER.href} className="mt-12 flex items-center gap-4 rounded-2xl p-4 sm:p-5 text-white" style={{ background: "#111111" }}>
      <span className="grid h-12 w-12 shrink-0 place-items-center rounded-xl" style={{ backgroundImage: GRAD }}>
        <CalendarDays className="h-6 w-6" />
      </span>
      <span className="text-base">
        <b>{CLASE_BANNER.titulo}</b>
        <span className="block text-white/80">
          {CLASE_BANNER.fecha}, {CLASE_BANNER.hora} · {CLASE_BANNER.precio}
        </span>
      </span>
      <span className="ml-auto hidden font-black sm:inline" style={{ color: "#F97316" }}>Ver clase →</span>
    </a>
  );
}

// ============================================================
// Caja vendida / oculta / inexistente
// ============================================================

function CajaNoDisponible({ caja, titulo }: { caja?: Caja; titulo: string }) {
  const alternativas = similares(caja, 3);
  const foto = caja ? fotoCaja(caja) : undefined;
  return (
    <div className="min-h-screen bg-background text-foreground overflow-x-hidden">
      <Header />
      <main className="mx-auto max-w-4xl px-4 py-10">
        <div className="text-center">
          {foto && (
            <div className="relative mx-auto mb-5 aspect-video w-full max-w-md overflow-hidden rounded-2xl bg-muted">
              <img src={foto} alt={caja?.name ?? ""} className="h-full w-full object-cover opacity-60" />
              <div className="absolute inset-0 grid place-items-center">
                <span className="rounded-lg px-4 py-1.5 text-xl font-black tracking-widest text-white" style={{ background: "rgba(220,38,38,0.9)", transform: "rotate(-8deg)" }}>VENDIDO</span>
              </div>
            </div>
          )}
          <h1 className="text-3xl sm:text-4xl font-black">{titulo}</h1>
          {caja && <p className="mt-2 text-lg text-muted-foreground">{caja.name}</p>}
          <p className="mt-3 text-base">Estas cajas parecidas siguen disponibles:</p>
        </div>
        {alternativas.length > 0 && (
          <div className="mt-6 grid gap-4 sm:grid-cols-3">
            {alternativas.map((x) => <TarjetaCaja key={cajaId(x)} c={x} />)}
          </div>
        )}
        <div className="mt-8 flex flex-col items-center gap-3">
          <Link to="/productos" className="flex min-h-14 w-full max-w-sm items-center justify-center rounded-2xl text-lg font-black text-white" style={{ backgroundImage: GRAD }}>
            Ver todas las cajas
          </Link>
          {caja && (
            <a href={waVendida(caja)} target="_blank" rel="noopener noreferrer" className="text-base font-bold underline underline-offset-4" style={{ color: ORANGE }}>
              ¿Quieres una igual? Escríbenos
            </a>
          )}
        </div>
      </main>
      <Footer />
    </div>
  );
}
