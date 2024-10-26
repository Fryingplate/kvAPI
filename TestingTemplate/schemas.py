from pydantic import BaseModel
from typing import Optional, Dict

class IoTDataInput(BaseModel):
    temperature: float
    humidity: float
    device_id: str
    timestamp: str
    