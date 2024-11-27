from __future__ import annotations
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas import CapybaraResponse, CapybaraRequest
from repository import CapybaraRepository
from data.config import engine, Base, get_db

#
# INICIALIZAÇÃO
#
Base.metadata.create_all(bind=engine)

app_capybara = APIRouter()

#
# ROUTES
#
@app_capybara.post("/capybara", response_model=CapybaraResponse, status_code=status.HTTP_201_CREATED)
def insert(request: CapybaraRequest, db:Session = Depends(get_db)):
    """_summary_    

    Args:
        Add a capybara with a autoincrement Id

    Returns:
        Capybara with your Id
    """
    return CapybaraRepository.save(db, request)

@app_capybara.get("/capybaras", response_model=list[CapybaraResponse])
def list_all_capybara(db:Session = Depends(get_db)):
    """_summary_    

    Args:
        Get method don't need arguments

    Returns:
        List of Capybara
    """
    return CapybaraRepository.get_all(db)

@app_capybara.get("/capybara/{id}", response_model=CapybaraResponse)
def get_by_id(id: int, db:Session = Depends(get_db)):
    """_summary_    

    Args:
        Needs a Id of Capybara that exist

    Returns:
        Capybara with id and capybara_id
    """
    capybara = CapybaraRepository.get_by_id(db,id)
    if (not capybara):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Capybara not found.')
    return capybara

@app_capybara.delete("/capybara/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db:Session = Depends(get_db)):
    """_summary_    

    Args:
        This operations needs a Id of valid Capybara

    Returns:
        Successfull or Address not found
    """
    if not CapybaraRepository.exists_by_id(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Capybara not found.')
    
    if CapybaraRepository.delete(db,id):
        raise HTTPException(status_code=status.HTTP_200_OK,detail='Operation successful!')
    else:
        raise HTTPException(status_code=status.HTTP_200_OK,detail='Operation not performed.')

@app_capybara.put("/capybara/{id}", response_model=CapybaraResponse)
def update(id: int, request: CapybaraRequest, db:Session = Depends(get_db)):
    """_summary_    

    Args:
        This operations needs a Id of valid Capybara

    Returns:
        Capybara updated
    """
    if not CapybaraRepository.exists_by_id(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Capybara not found.')
    
    return CapybaraRepository.update(db, id, request)
