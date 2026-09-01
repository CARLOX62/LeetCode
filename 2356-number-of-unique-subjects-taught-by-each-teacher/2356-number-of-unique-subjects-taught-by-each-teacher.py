import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()

    return result.rename(columns = {'subject_id':'cnt'})