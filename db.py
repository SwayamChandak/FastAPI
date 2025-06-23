
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base




Base=declarative_base()
engine = None
DBSession: sessionmaker = None

def init_db():
    try:
        global DBSession, engine
        pg_url='postgresql://{username}:{password}@localhost:5432/{db name}'
        engine=create_engine(pg_url)
        conn=engine.connect()
        conn.close()
        Base.metadata.create_all(engine)
        Base.metadata.bind=engine
        DBSession=sessionmaker(bind=engine)
    except Exception as e:
        print(f"Error Occurred in init_db - {e}")
        return False
    
def get_session():
    if DBSession is not None:
        session = DBSession()
        return session
    else:
        return None
