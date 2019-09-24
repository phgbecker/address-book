from sqlalchemy import Column, String, Integer, ForeignKey

from model import Base


class Owner(Base):
    __tablename__ = 'owner'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address_book_id = Column(Integer, ForeignKey('address_book.id'), nullable=True)

    def __init__(self, name):
        self.name = name

    def to_dict(self, show_dependencies=False):
        data = {
            'id': self.id,
            'name': self.name
        }

        return data
