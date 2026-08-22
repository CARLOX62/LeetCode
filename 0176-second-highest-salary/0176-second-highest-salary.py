import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)

    if len(salaries) < 2:
        return pd.DataFrame({
            f"SecondHighestSalary": [None]
        })

    return pd.DataFrame({
        f"SecondHighestSalary": [salaries.iloc[1]]
    })