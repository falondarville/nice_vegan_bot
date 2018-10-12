from sqlalchemy import create_engine, MetaData, insert, func, select, DateTime, Integer, Table, String, Column, Text
from datetime import datetime

metadata = MetaData()

engine = create_engine("mysql+pymysql://root@localhost/vegan_facts")

facts = Table('facts', metadata,
	Column('id', Integer(), primary_key=True),
	Column('content', Text(), nullable=False),
	Column('created_on', DateTime(), default=datetime.now)
	)

# metadata.create_all(engine)
# ins = insert(facts)

def pick_facts():
	conn = engine.connect()
	s = select([facts]).order_by(func.rand())
	r = conn.execute(s)
	row = r.fetchone()
	result = row['content']
	return result

# r = conn.execute(ins, [
# 	{"content": "Processed meat is a carcinogenic according to the World Health Organization."},
# 	{"content": "The egg industry kills newborn male chicks because they are not needed."},
# 	{"content": "Male calves are taken from their mothers as soon as they are born. They make up the veal industry."},
# 	{"content": "Red meat is linked to colon cancer."},
# 	{"content": "The human body naturally produces cholesterol, so you don't need to eat things with cholesterol in them!"},
# 	{"content": "Veganism is cheap if you eat a whole foods diet!"}
# 	])

