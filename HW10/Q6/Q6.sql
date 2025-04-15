CREATE TABLE IF NOT EXISTS pokemon_types (
id integer PRIMARY KEY,
name text NOT NULL UNIQUE) STRICT;

CREATE TABLE IF NOT EXISTS pokemon (
id integer PRIMARY KEY,
name text NOT NULL UNIQUE,
height integer,
weight integer,
base_experience integer,
type_id integer NOT NULL,
FOREIGN KEY(type_id) REFERENCES pokemon_types(id)) STRICT;

INSERT INTO pokemon_types (id, name) VALUES (999,"unknown")

