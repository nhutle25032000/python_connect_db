# create function connect and query data from AWS RDS database
 
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from database.models.AiJobData import AiJobData
from database.connect import engine as conn
from sqlalchemy.orm import Session
from sqlalchemy import select

from config.checkpoints import checkpoints
 
#def connect():
#    #conn = pymysql.connect(
#    #    host='snafty-headswap-prod.cn5cjf5ay4r8.us-east-1.rds.amazonaws.com',
#    #    port=3306,
#    #    user='headha_admin_prod',
#    #    password='DAod+N<uj4Ry+rQtzrvLeT2&*2PnQ',
#    #    database='snafty_headswap_prod'
#    #)
#    # Thông tin kết nối
#    user = 'headha_admin_prod'
#    password = 'DAod+N<uj4Ry+rQtzrvLeT2&*2PnQ'
#    host = 'snafty-headswap-prod.cn5cjf5ay4r8.us-east-1.rds.amazonaws.com'
#    port = 3306
#    database = 'snafty_headswap_prod'
# 
#    # Tạo engine kết nối
#    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
#    
#    return engine
#    
#def query_data():
#    try:
#        conn = connect()
#        print('Connection to MySQL DB successful')
#        query = 'SELECT * FROM admins'
#        return pd.read_sql(query, conn)
#        
#    except Exception as e:
#        print(e)
#    finally:
#        #if conn:
#        #    conn.close()
#        print('Connection to MySQL DB closed')
# 
def main():
    ##df = query_data()
    #session = Session(conn)
    #stmt = select(AiJobData).where(AiJobData.id == 1)
    ##users = session.scalars(stmt)
    #for user in session.scalars(stmt):
    #    print(user)
    #print('Data from MySQL DB')
    print(checkpoints)
    
if __name__ == '__main__':
    main()
 