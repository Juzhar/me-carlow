CREATE TABLE IF NOT EXISTS team (
ID integer PRIMARY KEY,
Name text NOT NULL UNIQUE,
Manager integer,
Wins integer,
Losses integer,
FOREIGN KEY(Manager) REFERENCES trainer(ID)
) STRICT;


