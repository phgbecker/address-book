from datetime import date

from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from model import Base


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)
    address_book_id = Column(Integer, ForeignKey('address_book.id'), nullable=True)
    telephones = relationship('Telephone', backref='contact')
    addresses = relationship('Address', backref='contact')

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def to_dict(self, show_dependencies=False):
        data = {
            'id': self.id,
            'name': self.name,
            'birthday': date.strftime(self.birthday, '%Y-%m-%d')
        }

        if show_dependencies:
            data['address_book'] = self.address_book
            data['telephones'] = [telephone.to_dict() for telephone in self.telephones]
            data['addresses'] = [address.to_dict() for address in self.addresses]

        return data
