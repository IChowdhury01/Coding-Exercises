SELECT w2.id
FROM Weather w1 INNER JOIN Weather w2   -- Join together two copies of the table, to compare temperatures
ON w2.recordDate = w1.recordDate + 1    -- Align rows when right row's date is 1 day after left row's date
WHERE w2.temperature > w1.temperature   -- Filter out rows where right row's temperature isn't larger
