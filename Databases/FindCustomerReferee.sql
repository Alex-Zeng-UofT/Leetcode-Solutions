# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_isd IS NULL OR referee_id != 2;