import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Find maximum salary in each department
    max_salary = employee.groupby('departmentId')['salary'].transform('max')

    # Keep employees whose salary equals department maximum
    result = employee[employee['salary'] == max_salary]

    # Join with Department table to get department name
    result = result.merge(
        department,
        left_on='departmentId',
        right_on='id'
    )

    # Rename columns
    result = result.rename(columns={
        'name_y': 'Department',
        'name_x': 'Employee',
        'salary': 'Salary'
    })

    return result[['Department', 'Employee', 'Salary']]