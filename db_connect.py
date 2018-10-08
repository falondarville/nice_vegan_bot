# pymysql driver
import pymysql
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root@localhost/vegan_facts")

conn = engine.connect()

ins = facts.insert().values(
	content = 'Being vegan saves over 200 animals a year.'
)

r = conn.execute(ins)

print(engine)