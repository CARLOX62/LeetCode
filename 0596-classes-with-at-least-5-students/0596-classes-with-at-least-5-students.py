import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = (courses.groupby('class').size().reset_index(name = 'student_count'))

    result = result[result['student_count'] >= 5]

    return result[['class']]