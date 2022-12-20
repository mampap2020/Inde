from src.models.datalake import lake_query
def getDfLake(query):
    return lake_query(query)