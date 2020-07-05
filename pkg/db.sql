--DROP TABLE public."usuario";

CREATE TABLE public."usuario"
(
  id serial,
  matricula character varying(7) NOT NULL,
  nome character varying(100) NOT NULL,
  senha character varying(60) NOT NULL,
  perfil character varying(25) NOT NULL,
  CONSTRAINT usuario_pkey PRIMARY KEY (id),
  CONSTRAINT usuario_matricula_key UNIQUE (matricula)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."usuario"
  OWNER TO psi;

  CREATE TABLE public.menu1
(
  id serial,
  nome character varying(50) NOT NULL,
  perfil character varying(25) NOT NULL,
  ordem smallint,
  ativo boolean,
  CONSTRAINT menu1_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.menu1
  OWNER TO psi;

INSERT INTO menu1(nome, perfil, ordem, ativo) VALUES('ADMINISTRADOR', 'ADM', 1, true);
INSERT INTO menu1(nome, perfil, ordem, ativo) VALUES('MENU 1', 'NORMAL', 1, true);
INSERT INTO menu1(nome, perfil, ordem, ativo) VALUES('BUSINESS', 'NORMAL', 1, true);


CREATE TABLE public.menu2
(
  id serial,
  nome character varying(50) NOT NULL,
  id_menu1 integer NOT NULL,
  ordem smallint,
  ativo boolean,
  target character varying(120),
  CONSTRAINT menu2_pkey PRIMARY KEY (id),
  CONSTRAINT menu2_menu1_id_fkey FOREIGN KEY (id_menu1)
      REFERENCES public."menu1" (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.menu2
  OWNER TO psi;

INSERT INTO menu2(nome, id_menu1, ordem, ativo, target) VALUES('USUÁRIOS', 1, 1, true, 'function999()');