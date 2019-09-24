from flask import Blueprint, render_template, request, redirect

from SetupService import Session
from model.Address import Address
from model.AddressType import AddressType
from model.Contact import Contact

address_frontend = Blueprint(
    'address_frontend',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/'
)


@address_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/address/<int:address_id>', methods=['GET'])
def get_address_by_id(address_book_id, contact_id, address_id):
    address = Session().query(Address) \
        .filter(Address.id == address_id) \
        .first()

    return render_template('addressById.html', address_book_id=address_book_id, contact_id=contact_id, address=address,
                           static_path='../../../../')


@address_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/address/<int:address_id>/update',
                        methods=['POST'])
def update_address_by_id(address_book_id, contact_id, address_id):
    session = Session()

    address = session.query(Address) \
        .filter(Address.id == address_id) \
        .first()

    address.name = request.form.get('name')
    session.commit()

    return redirect('/addressBooks/{}/contacts/{}'.format(address_book_id, contact_id))


@address_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/address', methods=['GET'])
def show_add_address_page(address_book_id, contact_id):
    return render_template('addAddress.html', address_book_id=address_book_id, contact_id=contact_id,
                           static_path='../../../')


@address_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/address/add', methods=['POST'])
def add_address(address_book_id, contact_id):
    session = Session()

    contact = session.query(Contact) \
        .filter(Contact.id == contact_id) \
        .first()

    address = Address(
        request.form.get('name'),
        AddressType.HOME
    )

    contact.addresses.append(address)
    session.commit()

    return redirect('/addressBooks/{}/contacts/{}'.format(address_book_id, contact_id))


@address_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/address/<int:address_id>/delete')
def delete_address_by_id(address_book_id, contact_id, address_id):
    session = Session()

    address = session.query(Address) \
        .filter(Address.id == address_id) \
        .first()

    session.delete(address)
    session.commit()

    return redirect('/addressBooks/{}/contacts/{}'.format(address_book_id, contact_id))
