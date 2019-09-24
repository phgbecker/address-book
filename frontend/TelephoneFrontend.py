from flask import Blueprint, render_template, request, redirect

from SetupService import Session
from model.Contact import Contact
from model.Telephone import Telephone
from model.TelephoneType import TelephoneType

telephone_frontend = Blueprint(
    'telephone_frontend',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/'
)


@telephone_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/telephone/<int:telephone_id>',
                          methods=['GET'])
def get_telephone_by_id(address_book_id, contact_id, telephone_id):
    telephone = Session().query(Telephone) \
        .filter(Telephone.id == telephone_id) \
        .first()

    return render_template('telephoneById.html', address_book_id=address_book_id, contact_id=contact_id,
                           telephone=telephone, static_path='../../../../')


@telephone_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/telephone', methods=['GET'])
def show_add_telephone_page(address_book_id, contact_id):
    return render_template('addTelephone.html', address_book_id=address_book_id, contact_id=contact_id, static_path='../../../')


@telephone_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/telephone/add', methods=['POST'])
def add_telephone(address_book_id, contact_id):
    session = Session()

    contact = session.query(Contact) \
        .filter(Contact.id == contact_id) \
        .first()

    telephone = Telephone(
        request.form.get('number'),
        TelephoneType.LANDLINE
    )

    contact.telephones.append(telephone)
    session.commit()

    return redirect('/addressBooks/{}/contacts/{}'.format(address_book_id, contact_id))


@telephone_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/telephone/<int:telephone_id>/update',
                          methods=['POST'])
def update_telephone_by_id(address_book_id, contact_id, telephone_id):
    session = Session()

    telephone = session.query(Telephone) \
        .filter(Telephone.id == telephone_id) \
        .first()

    telephone.number = request.form.get('number')
    session.commit()

    return redirect('/addressBooks/{}/contacts/{}'.format(address_book_id, contact_id))


@telephone_frontend.route('/<int:address_book_id>/contacts/<int:contact_id>/telephone/<int:telephone_id>/delete')
def delete_telephone_by_id(address_book_id, contact_id, telephone_id):
    session = Session()

    telephone = session.query(Telephone) \
        .filter(Telephone.id == telephone_id) \
        .first()

    session.delete(telephone)
    session.commit()

    return redirect('/addressBooks/{}/contacts/{}'.format(address_book_id, contact_id))
