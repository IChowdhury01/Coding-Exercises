SELECT 
    CASE
        WHEN MOD(id, 2) = 1 AND id != last_id THEN id+1
        WHEN MOD(id, 2) = 0 THEN id-1
        ELSE id
    END AS id,
    student
FROM Seat, (SELECT max(id) AS last_id FROM Seat)
ORDER BY id ASC
