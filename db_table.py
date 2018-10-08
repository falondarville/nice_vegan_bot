from sqlalchemy import create_engine, MetaData, DateTime, Integer, Table, String, Column, Text
from datetime import datetime

metadata = MetaData()

engine = create_engine("mysql+pymysql://root@localhost/vegan_facts")

facts = Table('facts', metadata,
	Column('id', Integer(), primary_key=True),
	Column('content', Text(), nullable=False),
	Column('created_on', DateTime(), default=datetime.now)
	)

metadata.create_all(engine)