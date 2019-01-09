CREATE TABLE public.billsales
(
    billno text COLLATE pg_catalog."default" NOT NULL,
    dateinfo date NOT NULL,
    sno integer NOT NULL DEFAULT nextval('billsales_sno_seq'::regclass),
    totalsales double precision,
    CONSTRAINT billsales_pkey PRIMARY KEY (sno)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.billsales
    OWNER to postgres;