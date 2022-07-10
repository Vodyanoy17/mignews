"""AI is creating summary for
"""
import re
from string import ascii_lowercase, digits


class CardCheck:
    """A CardCheck class that checks whether a card is valid"""

    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        """AI is creating summary for check_card_number

        Args:
            number (str): Формат номера следующий: XXXX-XXXX-XXXX-XXXX,
            где X - любая цифра (от 0 до 9).
        """
        pattern = re.compile(r"^(\d{4}-){3}(\d{4})$")

        if re.search(pattern, number):
            return True
        else:
            return False

    @classmethod
    def check_name(cls, name):
        """AI is creating summary for check_name

        Args:
            name ([str]):  проверяет строку name именем пользователя карты.
            Возвращает булево значение True, если имя записано верно и False - в противном случае
        """
        name_tmp = name.replace(" ", "")
        return all(c in cls.CHARS_FOR_NAME for c in name_tmp)
