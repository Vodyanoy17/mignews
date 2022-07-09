"""AI is creating summary for 
"""
from re import T
from string import ascii_lowercase,digits

class CardCheck:
    '''A CardCheck class that checks whether a card is valid'''
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    def check_card_number(self, number):
        """AI is creating summary for check_card_number

        Args:
            number (str): Формат номера следующий: XXXX-XXXX-XXXX-XXXX,
            где X - любая цифра (от 0 до 9).
        """
        import re
        p = re.compile(r'^(\d{4}-){3}(\d{4})$')
        
        re.search(p, number)
    def check_name(self,name):
        """AI is creating summary for check_name

        Args:
            name ([str]):  проверяет строку name именем пользователя карты.
            Возвращает булево значение True, если имя записано верно и False - в противном случае
        """
        return all(c in self.CHARS_FOR_NAME for c in name)