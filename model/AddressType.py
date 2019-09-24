import enum

import enumtables

from model import Base


class AddressType(enum.Enum):
    HOME = 'HOME'
    WORK = 'WORK'

    def to_dict(self, show_dependencies=False):
        data = {
            'type': self.name,
        }

        return data


AddressTypeTable = enumtables.EnumTable(AddressType, Base)
