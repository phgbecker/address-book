from flask import Blueprint, render_template

from RunService import Session
from model.AddressBook import AddressBook

address_book_frontend = Blueprint(
    'address_book_frontend',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/'
)


@address_book_frontend.route('/', methods=['GET'])
def get():
    result_set = Session().query(AddressBook) \
        .all()

    return render_template('addressBooks.html', address_books=result_set, static_path='')


@address_book_frontend.route('/<int:id>', methods=['GET'])
def get_address_book_by_id(id):
    result_set = Session().query(AddressBook) \
        .filter(AddressBook.id == id) \
        .first()

    return render_template('addressBookById.html', address_book=result_set, static_path='')
