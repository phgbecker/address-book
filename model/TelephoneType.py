import enum

import enumtables

from model import Base


class TelephoneType(enum.Enum):
    MOBILE = 'MOBILE'
    LANDLINE = 'LANDLINE'

    def to_dict(self, show_dependencies=False):
        data = {
            'type': self.name,
        }

        return data


TelephoneTypeTable = enumtables.EnumTable(TelephoneType, Base)
