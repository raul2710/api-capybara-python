from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import Capybara
from schemas import AddressResponse, AddressRequest
from repository import AddressRepository
from data.config import engine, Base, get_db

#
# INICIALIZAÇÃO
#
Base.metadata.create_all(bind=engine)

app_address = APIRouter()

#
# ROUTES
#
@app_address.post("/capybara/{id}/address", response_model=AddressResponse, status_code=status.HTTP_201_CREATED)
def insert(id: int, request: AddressRequest, db:Session = Depends(get_db)):
    """_summary_    

    Args:
        This operation needs a capybara without address

    Returns:
        Address with your Id and the capybara_id
    """
    capybara = db.query(Capybara).filter(Capybara.id == id).first()

    if not capybara:
        raise HTTPException(status_code=404, detail="Capybara not found")

    # Verifica se o usuário já tem um perfil
    if capybara.address:
        raise HTTPException(status_code=400, detail="Capybara already has a address")

    return AddressRepository.save(db, id, request)

@app_address.get("/addresses", response_model=list[AddressResponse])
def list_all_Address(db:Session = Depends(get_db)):
    """_summary_    

    Args:
        Get method don't need arguments

    Returns:
        List of Address
    """
    return AddressRepository.get_all(db)

@app_address.get("/address/{id}", response_model=AddressResponse)
def get_by_id(id: int, db:Session = Depends(get_db)):
    """_summary_    

    Args:
        Needs a Id of Address that exist

    Returns:
        Address with id and capybara_id
    """
    Address = AddressRepository.get_by_id(db,id)
    if (not Address):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Address not found.')
    return Address

@app_address.delete("/address/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db:Session = Depends(get_db)):
    """_summary_    

    Args:
        This operations needs a Id of valid Address

    Returns:
        Successfull or Address not found
    """
    if not AddressRepository.exists_by_id(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Address not found.')
    
    if AddressRepository.delete(db,id):
        raise HTTPException(status_code=status.HTTP_200_OK,detail='Operation successful!')
    else:
        raise HTTPException(status_code=status.HTTP_200_OK,detail='Operation not performed.')

@app_address.put("/address/{id}", response_model=AddressResponse)
def update(id: int, request: AddressRequest, db:Session = Depends(get_db)):
    """_summary_    

    Args:
        This operations needs a Id of valid Address

    Returns:
        Address updated
    """
    if not AddressRepository.exists_by_id(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Address not found.')
    
    return AddressRepository.update(db, id, request)
