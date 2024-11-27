from pydantic import BaseModel
from models.capybara import ClassificationStatus 
from .address_schemas import AddressBase

class CapybaraBase(BaseModel):
    name: str
    age: int
    weight: float
    color: str
    curiosity: str
    classification: ClassificationStatus
    address: AddressBase | None

class CapybaraRequest(CapybaraBase):
    ...

class CapybaraResponse(CapybaraBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
        orm_mode = True