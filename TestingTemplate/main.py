from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from model import IoTData
from schemas import IoTDataInput
from database import SessionLocal, engine, Base

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/iot-data/")
def create_iot_data(data: IoTDataInput, db: Session = Depends(get_db)):
    db_data = IoTData(
        temperature=data.temperature,
        humidity=data.humidity,
        device_id=data.device_id,
        timestamp=data.timestamp,
        
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data
