CREATE TABLE public.itemsdb
(
    "s.no" integer NOT NULL DEFAULT nextval('"itemsdb_s.no_seq"'::regclass),
    qty integer,
    prdid text COLLATE pg_catalog."default",
    itemclass text COLLATE pg_catalog."default",
    mrp double precision,
    disc double precision,
    CONSTRAINT itemsdb_pkey PRIMARY KEY ("s.no")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.itemsdb
    OWNER to postgres;