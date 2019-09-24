import enumtables
from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base
from model.TelephoneType import TelephoneTypeTable


class Telephone(Base):
    __tablename__ = 'telephone'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    type = enumtables.EnumColumn(TelephoneTypeTable)
    contact_id = Column(Integer, ForeignKey('contact.id'))

    def __init__(self, number, type):
        self.number = number
        self.type = type

    def to_dict(self, show_dependencies=False):
        data = {
            'id': self.id,
            'number': self.number,
            'type': self.type
        }

        return data
