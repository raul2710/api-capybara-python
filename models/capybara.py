from sqlalchemy import Column, Integer, String, Float, Enum as SqlEnum
from data.config import Base
from enum import Enum
from sqlalchemy.orm import relationship

class ClassificationStatus(Enum):
    RARE = 'Rare'
    COMUM = 'Comum'
    AMAZING = 'Amazing'

class Capybara(Base):
    __tablename__ = "tb_capybara"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name: str = Column(String(100), nullable=False)
    age: int = Column(Integer, nullable=False)
    weight: float = Column(Float, nullable=False)
    color: str = Column(String(10), nullable=True) 
    curiosity: str = Column(String(500), nullable=True)
    classification: ClassificationStatus = Column(SqlEnum(ClassificationStatus), nullable=False)

    address = relationship('Address', back_populates='capybara', uselist=False)
