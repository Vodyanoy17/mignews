"""AI is creating summary for 
"""


class Application:
    """Application"""

    def __init__(self, name, blocked=False):
        """Initialize the application"""
        self.name = name
        self.blocked = blocked

    def set_blocked(self, block=True):
        """AI is creating summary for set_blocked

        Args:
            block (bool, optional): [description]. Defaults to True.
        """
        self.blocked = block


class AppStore:
    """Store"""

    __application_list = []

    def add_application(self, app):
        """- добавление нового приложения app в магазин;"""
        self.__application_list.append(app)

    def remove_application(self, app):
        """- удаление приложения app из магазина;

        Args:
            app ([type]): [description]
        """
        self.__application_list.remove(app)

    @staticmethod
    def block_application(app):
        """- блокировка приложения app (устанавливает локальное свойство blocked объекта
        app в значение True)

        Args:
            app ([type]): [description]
        """
        app.set_blocked()

    def total_apps(self):
        """возвращает общее число приложений в магазине."""

        print(self.__application_list[0].blocked)
        return len(self.__application_list)


# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.block_application(app_youtube)
# store.remove_application(app_youtube)
# print(store.total_apps())
