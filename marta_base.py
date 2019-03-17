from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class marta_realtime(Base):
    __tablename__ = 'marta_realtime'
    id = Column(Integer, primary_key=True)
    destination =  Column(String(50))
    cardinal_direction = Column(String(2))
    event_time = (DateTime)
    line = Column(String(20))
    next_arrival_time = (DateTime)
    station = Column(String(100))
    train_id = Column(String(50))


