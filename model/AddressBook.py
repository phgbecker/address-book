from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model import Base


class AddressBook(Base):
    __tablename__ = 'address_book'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    owner = relationship('Owner', uselist=False, backref='address_book')
    contacts = relationship('Contact', backref='address_book')

    def __init__(self, description):
        self.description = description

    def get_owner(self):
        return '1'

    def to_dict(self, show_dependencies=False):
        data = {
            'id': self.id,
            'description': self.description,
            'owner': self.owner
        }

        if show_dependencies:
            data['contacts'] = [contact.to_dict() for contact in self.contacts]

        return data
