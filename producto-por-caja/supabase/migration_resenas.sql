-- Reseñas reales de compradores. Solo se muestran las aprobadas.
CREATE TABLE public.resenas (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  producto text NOT NULL DEFAULT 'general',          -- código de la caja (ej. 'CF-027') o 'general'
  nombre text NOT NULL,                               -- nombre del cliente
  ciudad text,
  texto text NOT NULL,
  calificacion smallint NOT NULL CHECK (calificacion BETWEEN 1 AND 5),
  media_url text,                                     -- foto o video opcional
  media_tipo text CHECK (media_tipo IN ('foto','video')),
  fecha date NOT NULL DEFAULT current_date,
  verificada boolean NOT NULL DEFAULT false,          -- compra confirmada por el equipo
  aprobada boolean NOT NULL DEFAULT false,            -- solo las aprobadas se ven en el sitio
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX resenas_producto_idx ON public.resenas (producto, aprobada, fecha DESC);
GRANT SELECT ON public.resenas TO anon, authenticated;
GRANT ALL ON public.resenas TO service_role;
ALTER TABLE public.resenas ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Resenas aprobadas son publicas" ON public.resenas FOR SELECT TO anon, authenticated
  USING (aprobada = true);

-- Bucket público para la foto o video de cada reseña (las escrituras solo con service role).
INSERT INTO storage.buckets (id, name, public) VALUES ('resenas', 'resenas', true)
  ON CONFLICT (id) DO NOTHING;
