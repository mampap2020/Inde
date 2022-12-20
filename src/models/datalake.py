import pandas as pd
from src.models.database import Database


def lake_setup():
    db = Database()
    
    df_1 = pd.read_csv("src/assets/file_02.csv")
    df_2 = pd.read_csv("src/assets/region_cordinates.csv")
    df_3 = pd.read_csv("src/assets/state_region_corrected.csv")
    dfs = {"file_02" : df_1, "region_cordinates":df_2, "State_Region_corrected":df_3}
    for key in dfs:
        dfs[key].to_sql(key, db.db, if_exists="replace")
def lake_query(query, *args):
    db = Database()
    return pd.read_sql(query, db.db, params=args)

