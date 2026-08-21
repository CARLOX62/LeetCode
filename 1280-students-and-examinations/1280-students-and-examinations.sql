# Write your MySQL query statement below
Select Students.student_id, Students.student_name,
Subjects.subject_name,
COUNT(Examinations.subject_name) AS attended_exams
From Students
Cross Join Subjects
Left Join Examinations
ON Students.student_id = Examinations.student_id
And Subjects.subject_name = Examinations.subject_name
Group By 
Students.student_id,
Students.student_name,
Subjects.subject_name
Order By
Students.student_id,
Subjects.subject_name