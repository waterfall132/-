import re

import pandas as pd
from sqlalchemy import create_engine
path='./xiecheng.csv'
data = pd.read_csv(path,header = 0)
print(data.head(5))

data = data[data['评价'].str.len() <= 100]



# 数据库连接信息
username = 'root'
password = 'root'
host = 'localhost'
dbname = 'changlong'
table_name = 'xiecheng2'

# 建立数据库连接
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}/{dbname}?charset=utf8mb4')

# 将 DataFrame 保存到 MySQL 中
data.to_sql(name=table_name, con=engine, if_exists='append', index=False)



# 编写 SQL 查询语句
sql_query = f"SELECT * FROM {table_name}"
# 从数据库中执行 SQL 查询并读取数据
table_data = pd.read_sql(sql_query, con=engine)
# 显示数据
print(table_data.head())



# 从数据库中读取整个表
table_data = pd.read_sql_table(table_name, con=engine)
# 显示数据
print(table_data.head())
