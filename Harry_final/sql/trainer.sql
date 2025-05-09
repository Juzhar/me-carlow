CREATE TABLE IF NOT EXISTS trainer (
ID integer PRIMARY KEY,
Name text NOT NULL UNIQUE,
Email text,
Phone text
) STRICT;

