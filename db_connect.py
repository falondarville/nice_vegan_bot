# pymysql driver
import pymysql
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root@localhost/vegan_facts")

engine.connect()

print(engine)