from pydantic import BaseModel

class AddressBase(BaseModel):
    city: str
    state: str
    lake_name: str

class AddressRequest(AddressBase):
    ...

class AddressResponse(AddressBase):
    id: int
    capybara_id: int

    class Config:
        from_attributes = True
        populate_by_name = True
        orm_mode = True
