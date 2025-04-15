CREATE TABLE IF NOT EXISTS pokemon (
id integer PRIMARY KEY,
name text NOT NULL UNIQUE,
height integer,
weight integer,
base_experience integer,
type_id integer NOT NULL,
CONSTRAINT CHK_PKMN CHECK (height>1 AND weight < 1000)
) STRICT;
