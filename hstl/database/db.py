from sqlalchemy.schema import *
from sqlalchemy import *
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import  sessionmaker

engine = create_engine('mysql+pymysql://root:root@localhost:3306')
ins = sa.inspect(engine)
db_list = ins.get_schema_names()

if not 'test' in db_list:
    engine.execute(CreateSchema('test'))

uri = 'mysql+pymysql://root:root@localhost:3306/test'

db = create_engine(uri)
metadata = MetaData(db)

if not db.dialect.has_table(db,'personal_info'):
    personal_info = Table('personal_info',metadata,Column('p_id',Integer,primary_key=True,nullable=False),
                          Column('first_name',String(500)),Column('DOB',DATE),Column('occupation',String(1000)),
                          Column('id_proof',String(500),nullable=False),Column('id_proof_no',String(500),nullable=False,unique=True),
                    Column('h_no',String(1000)),Column('village',String(500)),Column('landmark',String(1000)),Column('street',String(1000)),
                    Column('district',String(1000)),Column('pincode',Integer),Column('mobileno',String(100)))
    personal_info.create()
if not db.dialect.has_table(db,'login'):
    login = Table('login',metadata,Column('l_id',Integer,primary_key=True,nullable=False),Column('username',String(500)),Column('password',String(500)))
    login.create()

Session = sessionmaker()
conn = db.connect()
Session.configure(bind = conn)
session = Session()
