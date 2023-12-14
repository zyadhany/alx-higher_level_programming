-- Get all DB of server.
SELECT * FROM cities WHERE state_id = (
    SELECT id FROM state WHERE name="California"
) ORDER BY id;
