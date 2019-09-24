from datetime import datetime

from flask import Blueprint, render_template, request, redirect

from RunService import Session
from model.AddressBook import AddressBook
from model.Contact import Contact

contact_frontend = Blueprint(
    'contact_frontend',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/'
)


@contact_frontend.route('/<int:address_book_id>/contacts/<int:id>', methods=['GET'])
def get_contact_by_id(address_book_id, id):
    result_set = Session().query(Contact) \
        .join(AddressBook) \
        .filter(AddressBook.id == address_book_id) \
        .filter(Contact.id == id) \
        .first()

    return render_template('contactById.html', contact=result_set, static_path='../../')


@contact_frontend.route('/<int:address_book_id>/contacts', methods=['GET'])
def show_add_contact_page(address_book_id):
    return render_template('addContact.html', address_book_id=address_book_id, static_path='../')


@contact_frontend.route('/<int:address_book_id>/contacts/add', methods=['POST'])
def add_contact(address_book_id):
    session = Session()

    address_book = session.query(AddressBook) \
        .filter(AddressBook.id == address_book_id) \
        .first()

    contact = Contact(
        request.form.get('name'),
        datetime.strptime(request.form.get('birthday'), '%Y-%m-%d').date()
    )

    address_book.contacts.append(contact)
    session.commit()

    return redirect('/addressBooks/{}'.format(address_book_id))


@contact_frontend.route('/<int:address_book_id>/contacts/<int:id>/update', methods=['POST'])
def update_contact_by_id(address_book_id, id):
    session = Session()

    contact = session.query(Contact) \
        .join(AddressBook) \
        .filter(AddressBook.id == address_book_id) \
        .filter(Contact.id == id) \
        .first()

    contact.name = request.form.get('name')
    contact.birthday = datetime.strptime(request.form.get('birthday'), '%Y-%m-%d').date()
    session.commit()

    return redirect('/addressBooks/{}'.format(address_book_id))


@contact_frontend.route('/<int:address_book_id>/contacts/<int:id>/delete')
def delete_contact_by_id(address_book_id, id):
    session = Session()

    contact = session.query(Contact) \
        .join(AddressBook) \
        .filter(AddressBook.id == address_book_id) \
        .filter(Contact.id == id) \
        .first()

    session.delete(contact)
    session.commit()

    return redirect('/addressBooks/{}'.format(address_book_id))
