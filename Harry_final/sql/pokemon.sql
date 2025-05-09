CREATE TABLE IF NOT EXISTS pokemon (
ID integer PRIMARY KEY,
Name TEXT NOT NULL UNIQUE,
Height integer,
Weight integer,
Experience integer
) STRICT;
