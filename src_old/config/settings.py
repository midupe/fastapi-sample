#
#
DEV_MODE = True
#
#

import sqlalchemy
import pandas as pd

#set database
db=sqlalchemy.create_engine(f'sqlite:///db.sqlite3')

#aux functions bellow
def sql(query):
    try:
        return pd.read_sql_query(query, db).to_dict('records')
    except Exception as e:
        print(e)
        if DEV_MODE:
            return str(e)
        else:
            return pd.DataFrame()