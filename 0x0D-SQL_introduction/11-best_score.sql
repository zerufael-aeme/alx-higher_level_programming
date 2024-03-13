-- This script list all records in order if they meet a condition
SELECT `score`, `name`
FROM `second_table`
WHERE score>=10
ORDER BY `score` DESC;
