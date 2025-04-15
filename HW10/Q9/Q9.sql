SELECT p.id, p.name, pt.name
FROM "pokemon" p left join "pokemon_types" pt
ON p.type_id = pt.id