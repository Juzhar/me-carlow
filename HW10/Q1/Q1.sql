CREATE TABLE IF NOT EXISTS pokemon (
id integer PRIMARY KEY,
name text NOT NULL UNIQUE,
height integer,
weight integer,
base_experience integer) STRICT;
