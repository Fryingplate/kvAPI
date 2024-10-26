from sqlalchemy import Column, Integer, String, Float, JSON
from database import Base

class IoTData(Base):
    __tablename__ = "iot_data"

    id = Column(Integer, primary_key=True,index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    device_id = Column(String)
    timestamp = Column(String)
    



