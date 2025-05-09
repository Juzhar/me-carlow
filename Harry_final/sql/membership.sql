CREATE TABLE IF NOT EXISTS membership (
PokemonID integer,
TeamID integer,
FOREIGN KEY(PokemonID) REFERENCES pokemon(ID),
FOREIGN KEY(TeamID) REFERENCES team(ID),
PRIMARY KEY (PokemonID, TeamID)
) STRICT;

