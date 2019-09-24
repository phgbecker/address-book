from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base

# SQLAlchemy variables
engine = create_engine('sqlite:///address-book.db', echo=True, connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class SetupService(object):

    @staticmethod
    def setup_service():
        from service.AddressBookService import address_book_service
        from service.ContactService import contact_service

        app = Flask('Address Book Service', root_path='frontend/')
        app.register_blueprint(address_book_service, url_prefix='/api/addressBooks')
        app.register_blueprint(contact_service, url_prefix='/api/addressBooks')
        app.run(port=8081)


if __name__ == '__main__':
    SetupService.setup_service()
