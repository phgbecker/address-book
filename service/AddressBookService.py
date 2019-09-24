from flask import Blueprint

from SetupService import Session
from model.AddressBook import AddressBook
from service.util.ResponseUtil import ResponseUtil

address_book_service = Blueprint('address_book_service', __name__)


@address_book_service.route('/', methods=['GET'])
def get():
    return ResponseUtil.parse_collection(
        Session().query(AddressBook)
            .all()
    )


@address_book_service.route('/<int:id>', methods=['GET'])
def get_address_book_by_id(id):
    return ResponseUtil.parse(
        Session().query(AddressBook)
            .filter(AddressBook.id == id)
            .first()
    )
