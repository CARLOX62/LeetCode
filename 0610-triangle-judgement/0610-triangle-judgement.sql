# Write your MySQL query statement below
Select x,y,z,
Case 
    When
    x + y > z 
    and y + z > x 
    and x + z > y
    Then 
      'Yes'
    else 
      'No'
End As triangle
From Triangle;