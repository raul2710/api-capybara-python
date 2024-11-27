from sqlalchemy import Column, ForeignKey, Integer, String
from data.config import Base
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = "tb_address"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    city: str = Column(String(120), nullable=False)
    state: str = Column(String(120), nullable=False)
    lake_name: str = Column(String(120))
    capybara_id: int = Column(Integer, ForeignKey('tb_capybara.id'), unique=True) 

    capybara = relationship('Capybara', back_populates='address')

