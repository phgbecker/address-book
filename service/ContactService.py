from flask import Blueprint
from sqlalchemy.sql.expression import extract

from RunService import Session
from model.AddressBook import AddressBook
from model.Contact import Contact
from service.util.ResponseUtil import ResponseUtil

contact_service = Blueprint('contact_service', __name__)


@contact_service.route('/<int:address_book_id>/contacts/', methods=['GET'])
def get(address_book_id):
    return ResponseUtil.parse_collection(
        Session().query(Contact)
            .join(AddressBook)
            .filter(AddressBook.id == address_book_id)
            .all()
    )


@contact_service.route('/<int:address_book_id>/contacts/<int:id>', methods=['GET'])
def get_contact_by_id(address_book_id, id):
    return ResponseUtil.parse(
        Session().query(Contact)
            .join(AddressBook)
            .filter(AddressBook.id == address_book_id)
            .filter(Contact.id == id)
            .first(),
        True
    )


@contact_service.route('/<int:address_book_id>/contacts/name/<name>', methods=['GET'])
def get_contacts_by_name(address_book_id, name):
    return ResponseUtil.parse_collection(
        Session().query(Contact)
            .join(AddressBook)
            .filter(AddressBook.id == address_book_id)
            .filter(Contact.name.like('%' + name + '%'))
            .all()
    )


@contact_service.route('/<int:address_book_id>/contacts/birthday/year/<year>', methods=['GET'])
def get_contacts_by_birthday_year(address_book_id, year):
    return ResponseUtil.parse_collection(
        Session().query(Contact)
            .join(AddressBook)
            .filter(AddressBook.id == address_book_id)
            .filter(extract('year', Contact.birthday) == year)
            .all()
    )


@contact_service.route('/<int:address_book_id>/contacts/birthday/month/<month>', methods=['GET'])
def get_contacts_by_birthday_month(address_book_id, month):
    return ResponseUtil.parse_collection(
        Session().query(Contact)
            .join(AddressBook)
            .filter(AddressBook.id == address_book_id)
            .filter(extract('month', Contact.birthday) == month)
            .all()
    )


@contact_service.route('/<int:address_book_id>/contacts/birthday/day/<day>', methods=['GET'])
def get_contacts_by_birthday_day(address_book_id, day):
    return ResponseUtil.parse_collection(
        Session().query(Contact)
            .join(AddressBook)
            .filter(AddressBook.id == address_book_id)
            .filter(extract('day', Contact.birthday) == day)
            .all()
    )
