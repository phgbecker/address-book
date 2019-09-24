import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from SetupService import Session
from model import Base
from model.Address import Address
from model.AddressBook import AddressBook
from model.AddressType import AddressType
from model.Contact import Contact
from model.Owner import Owner
from model.Telephone import Telephone
from model.TelephoneType import TelephoneType

# SQLAlchemy variables
engine = create_engine('sqlite:///address-book.db', echo=True)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class SetupDatabase(object):

    @staticmethod
    def setup():
        # Stranger Things
        jane_hopper_contact = Contact('Jane Hopper', datetime.date(1990, 3, 22))
        jane_hopper_contact.addresses = [
            Address('Hawkins, Indiana, USA', AddressType.HOME),
            Address('Atlanta, Georgia, USA', AddressType.WORK)
        ]
        jane_hopper_contact.telephones = [
            Telephone('92467-0501', TelephoneType.MOBILE),
            Telephone('33455-0123', TelephoneType.LANDLINE)
        ]

        dustin_henderson_contact = Contact('Dustin Henderson', datetime.date(1991, 4, 12))
        dustin_henderson_contact.addresses = [
            Address('Hawkins, Indiana, USA', AddressType.HOME),
            Address('Atlanta, Georgia, USA', AddressType.WORK)
        ]
        dustin_henderson_contact.telephones = [
            Telephone('5653-1241', TelephoneType.LANDLINE),
            Telephone('88874-121', TelephoneType.MOBILE)
        ]

        stranger_things_address_book = AddressBook('Stranger Things')
        stranger_things_address_book.owner = Owner('Will Byers')
        stranger_things_address_book.contacts = [jane_hopper_contact, dustin_henderson_contact]

        # Back to the Future
        marty_mcfly_contact = Contact('Marty McFly', datetime.date(1968, 6, 12))
        marty_mcfly_contact.addresses = [
            Address('Hill Valley, California, USA', AddressType.HOME),
            Address('Olympic Theater, Los Angeles, USA', AddressType.WORK)
        ]
        marty_mcfly_contact.telephones = [
            Telephone('36474-2313', TelephoneType.MOBILE),
            Telephone('82135-0602', TelephoneType.LANDLINE)
        ]

        jennifer_parker_contact = Contact('Jennifer Parker', datetime.date(1965, 5, 10))
        jennifer_parker_contact.addresses = [
            Address('Hill Valley, California, USA', AddressType.HOME),
            Address('Olympic Theater, Los Angeles, USA', AddressType.WORK)
        ]
        jennifer_parker_contact.telephones = [
            Telephone('7345-0506', TelephoneType.MOBILE),
            Telephone('3344-1286', TelephoneType.LANDLINE)
        ]

        back_to_the_future_address_book = AddressBook('Back to the Future')
        back_to_the_future_address_book.owner = Owner('Emmett Brown')
        back_to_the_future_address_book.contacts = [marty_mcfly_contact, jennifer_parker_contact]

        session = Session()
        session.add(stranger_things_address_book)
        session.add(back_to_the_future_address_book)
        session.commit()
        session.close()


if __name__ == '__main__':
    SetupDatabase.setup()
