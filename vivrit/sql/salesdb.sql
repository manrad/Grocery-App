-- Table: public.salesdb

-- DROP TABLE public.salesdb;

CREATE TABLE public.salesdb
(
    sno integer NOT NULL DEFAULT nextval('salesdb_sno_seq'::regclass),
    itemid text COLLATE pg_catalog."default" NOT NULL,
    qty smallint,
    salesprice double precision,
    mrp double precision,
    disc double precision,
    billdate date,
    bill text COLLATE pg_catalog."default",
    CONSTRAINT salesdb_pkey PRIMARY KEY (sno)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.salesdb
    OWNER to postgres;