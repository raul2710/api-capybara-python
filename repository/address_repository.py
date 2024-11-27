from __future__ import annotations
from sqlalchemy.orm import Session
from models import Address
from schemas import AddressBase

class AddressRepository:

    #
    # Retornar todos as Addresss
    #
    def get_all(db:Session) -> list[Address]:
        return db.query(Address).all()    #select * from tb_addresss
    
    # def get_all(db:Session, id:int) -> list[Address]:
    #     return db.query(Capybara).filter(Capybara.id == id).first().address    #select * from tb_addresss
    
    #
    # Salvar um Address na tabela
    #
    @staticmethod
    def save(db:Session, capybara_id: int, address: AddressBase) -> Address:

        new_address = Address(**address.model_dump(), capybara_id=capybara_id)
        db.add(new_address)
        db.commit()
        db.refresh(new_address)

        return new_address
    
    def update(db: Session, address_id: int, address_update: AddressBase) -> Address:

        # """Atualiza um usuário existente."""
        db_address = db.query(Address).filter(Address.id == address_id).first()
        # if not db_address:
        #     return None

        # Atualizar o perfil, se fornecido
        if db_address:
            db_address.city = address_update.city
            db_address.state = address_update.state
            db_address.lake_name = address_update.lake_name

        # Salvar as alterações
        db.commit()
        db.refresh(db_address)

        return db_address

    #
    # Return a Address by Id
    #
    @staticmethod
    def get_by_id(db:Session, id: int) -> Address:
        return db.query(Address).filter(Address.id == id).first()
    
    #
    # Verify if a Address Id exist 
    #
    @staticmethod
    def exists_by_id(db:Session, id: int) -> bool:
        return db.query(Address).filter(Address.id == id).first() is not None
    
    #
    # Delete a Address by Id
    #
    @staticmethod
    def delete(db:Session, id: int) -> bool:

        address = db.query(Address).filter(Address.id == id).first()
        
        if Address is not None:
            db.delete(address)
            db.commit()

            return True

        return False


