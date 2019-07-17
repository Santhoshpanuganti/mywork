from sqlalchemy.ext.declarative import *
from sqlalchemy import *

Base = declarative_base()

class Personal_info(Base):
    __tablename__ = 'personal_info'
    p_id= Column(Integer, primary_key = True, nullable = False)
    first_name=Column('first_name', String(500))
    DOB=Column('DOB', DATE)
    occupation=Column('occupation', String(1000))
    id_proof=Column('id_proof', String(500), nullable=False)
    id_proof_no = Column('id_proof_no', String(500), nullable=False,unique=True)
    h_no = Column('h_no', String(1000))
    village = Column('village', String(500))
    landmark = Column('landmark', String(1000))
    street = Column('street', String(1000))
    district = Column('district', String(1000))
    pincode = Column('pincode', Integer)
    mobileno = Column('mobileno',String(100))


class Login_credentials(Base):
    __tablename__ = 'login'
    l_id = Column(Integer,primary_key=True,nullable=False)
    username = Column('username',String(500))
    password = Column('password',String(500))



