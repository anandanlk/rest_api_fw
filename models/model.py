from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    username: str
    password: str

class BookingDates(BaseModel):
    checkin: Optional[str] = None
    checkout: Optional[str] = None

class Booking(BaseModel):
    firstname: Optional[str] = Field(None, max_length=30)
    lastname: Optional[str] = Field(None, max_length=30)
    totalprice: Optional[int] = Field(None, ge=0)
    depositpaid: Optional[bool] = None
    bookingdates: Optional[BookingDates] = None
    additionalneeds: Optional[str] = Field(None, max_length=50)

class PartialUpdate(BaseModel):
    firstname: Optional[str] = Field(None, max_length=30)
    lastname: Optional[str] = Field(None, max_length=30)
    totalprice: Optional[int] = Field(None, ge=0)
    depositpaid: Optional[bool] = None
    checkin: Optional[str] = None
    checkout: Optional[str] = None
    additionalneeds: Optional[str] = Field(None, max_length=50)