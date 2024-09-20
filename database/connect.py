from sqlalchemy import create_engine

user = 'root'
password = ''
host = '127.0.0.1'
port = 3306
database = 'headswap'

# Tạo engine kết nối
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')