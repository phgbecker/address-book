import enumtables
from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base
from model.AddressType import AddressTypeTable


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = enumtables.EnumColumn(AddressTypeTable)
    contact_id = Column(Integer, ForeignKey('contact.id'))

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def to_dict(self, show_dependencies=False):
        data = {
            'id': self.id,
            'name': self.name,
            'type': self.type
        }

        if show_dependencies:
            data['contact'] = self.contact

        return data
