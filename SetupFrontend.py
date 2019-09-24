from flask import Flask


class SetupFrontend(object):

    @staticmethod
    def setup():
        from frontend.AddressBookFrontend import address_book_frontend
        from frontend.ContactFrontend import contact_frontend
        from frontend.TelephoneFrontend import telephone_frontend
        from frontend.AddressFrontend import address_frontend

        app = Flask('Frontend')
        app.register_blueprint(address_book_frontend, url_prefix='/addressBooks')
        app.register_blueprint(contact_frontend, url_prefix='/addressBooks')
        app.register_blueprint(telephone_frontend, url_prefix='/addressBooks')
        app.register_blueprint(address_frontend, url_prefix='/addressBooks')
        print(app.template_folder)
        app.run(port=80)


if __name__ == '__main__':
    SetupFrontend.setup()
