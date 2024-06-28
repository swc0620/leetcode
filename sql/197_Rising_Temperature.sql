SELECT w2.id FROM Weather w1
CROSS JOIN Weather w2
WHERE DATEDIFF(w2.recordDate, w1.recordDate) = 1 AND w2.temperature > w1.temperature;