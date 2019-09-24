# address-book

Address Book frontend and service application, developed with Python, SQLAlchemy, and Flask

## API endpoints

- AddressBookService
    - http://{host}/api/addressBooks/
    - http://{host}/api/addressBooks/{id}

- ContactService
    - http://{host}/api/addressBooks/{id}/contacts/
    - http://{host}/api/addressBooks/{id}/contacts/{id}
    - http://{host}/api/addressBooks/{id}/contacts/{id}/name/{name}
    - http://{host}/api/addressBooks/{id}/contacts/{id}/birthday/year/{year}
    - http://{host}/api/addressBooks/{id}/contacts/{id}/birthday/month/{month}
    - http://{host}/api/addressBooks/{id}/contacts/{id}/birthday/day/{day}

## ORM diagram

![ORM diagram](ORM%20diagram.png)
