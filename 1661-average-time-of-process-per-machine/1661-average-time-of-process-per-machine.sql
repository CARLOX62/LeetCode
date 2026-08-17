# Write your MySQL query statement below
Select s.machine_id,
Round(AVG(e.timestamp - s.timestamp),3) AS processing_time
From Activity s
join Activity e
ON s.machine_id = e.machine_id
AND s.process_id = e.process_id
AND s.activity_type = 'start'
AND e.activity_type = 'end'
Group By s.machine_id;