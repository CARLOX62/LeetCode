import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = (activity.sort_values('event_date')
    .drop_duplicates(subset='player_id')
    [['player_id','event_date']]
    .rename(columns={'event_date': 'first_login'})
    )
    return first_login
