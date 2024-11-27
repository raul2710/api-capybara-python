from __future__ import annotations
from sqlalchemy.orm import Session, joinedload
from models import Address, Capybara
from schemas import CapybaraBase

class CapybaraRepository:

    #
    # Retornar todos as Capybaras
    #
    @staticmethod
    def get_all(db:Session) -> list[Capybara]:
        # return db.query(Capybara).all()      #select * from tb_Capybaras
        return db.query(Capybara).options(joinedload(Capybara.address)).all()
    
    #
    # Salvar um Capybara na tabela
    #
    @staticmethod
    def save(db:Session, capybara: CapybaraBase) -> Capybara:

        new_capybara = Capybara(
            name=capybara.name, 
            age=capybara.age, 
            weight=capybara.weight, 
            color=capybara.color, 
            curiosity=capybara.curiosity, 
            classification=capybara.classification
        )
        
        # Criar o perfil relacionado, se fornecido
        if capybara.address:
            new_address = Address(
                city = capybara.address.city,
                state = capybara.address.state,
                lake_name = capybara.address.lake_name,

                capybara=new_capybara
            )
            new_capybara.address = new_address  # Relacionamento explícito

        db.add(new_capybara)  # Adicionar o usuário ao banco de dados
        db.commit()
        db.refresh(new_capybara)  # Atualizar a instância com os dados do banco

        return new_capybara
    
    def update(db: Session, capybara_id: int, capybara_update: CapybaraBase) -> Capybara:

        """Atualiza um usuário existente."""
        # Buscar o usuário existente
        db_capybara = db.query(Capybara).filter(Capybara.id == capybara_id).first()
        if not db_capybara:
            return None

        # Atualizar os campos do usuário
        db_capybara.name = capybara_update.name
        db_capybara.age = capybara_update.age
        db_capybara.color = capybara_update.color
        db_capybara.curiosity = capybara_update.curiosity
        db_capybara.classification = capybara_update.classification

        # Atualizar o perfil, se fornecido
        if db_capybara.address:
            db_capybara.address.city = capybara_update.address.city
            db_capybara.address.state = capybara_update.address.state
            db_capybara.address.lake_name = capybara_update.address.lake_name
        else: 
            db_capybara.address = Address(
                city=capybara_update.address.city,
                state=capybara_update.address.state,
                lake_name=capybara_update.address.lake_name,

                capybara_id=db_capybara.id
            )
            
        # Salvar as alterações
        db.commit()
        db.refresh(db_capybara)

        return db_capybara

    #
    # Return a Capybara by Id
    #
    @staticmethod
    def get_by_id(db:Session, id: int) -> Capybara:
        return db.query(Capybara).filter(Capybara.id == id).first()
    
    #
    # Verify if a Capybara Id exist 
    #
    @staticmethod
    def exists_by_id(db:Session, id: int) -> bool:
        return db.query(Capybara).filter(Capybara.id == id).first() is not None
    
    #
    # Delete a Capybara by Id
    #
    @staticmethod
    def delete(db:Session, id: int) -> bool:

        capybara = db.query(Capybara).filter(Capybara.id == id).first()
        
        if capybara is not None:
            db.delete(capybara.address)
            db.delete(capybara)
            db.commit()

            return True

        return False


