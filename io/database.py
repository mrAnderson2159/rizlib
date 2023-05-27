__all__ = {'JSONDatabase'}

__author__ = "Valerio Molinari"
__credits__ = "Valerio Molinari"
__maintainer__ = "Valerio Molinari"
__email__ = "valeriomolinariprogrammazione@gmail.com"

from json import dumps, loads
from pathlib import Path
from documentation.types import PathHint
from terminal.text.logs import warning, success, Silence
from os.path import exists


class JSONDatabase:
    def __init__(self, json_db_path: PathHint):
        """Allows to create and manage a database in a json file.
        Is used to read and parse the database into a dictionary then
        update the file with the modified database if needed.

        :param json_db_path: the absolute or relative path to the database.
        The extension .json will be added automatically if not present
        """
        if not json_db_path.endswith('.json'):
            json_db_path += '.json'

        self.__path: Path = Path(json_db_path)

    def create(self, silence: Silence = Silence.none) -> bool:
        """Creates a database.json file in the file system at constructor's path

        :param silence: Used to silence logs. See rizlib.text.logs.Silence enum class.
        :return: True if database file has been created, False if it already exists
        """
        if not exists(self.__path):
            with open(self.__path, 'w') as file:
                file.write(dumps({}))
            success(f"{self.__path} created", silence)

            return True

        warning(f"{self.__path} already exists", silence)
        return False

    def read(self, silence: Silence = Silence.none) -> dict:
        """Reads the content of the database and parses it as a dictionary.
        If the database doesn't exist, it creates it.

        :param silence: Used to silence logs. See rizlib.text.logs.Silence enum class.
        :return: the database
        """
        self.create(Silence.warning)
        with open(self.__path, 'r') as file:
            database = file.read()
            success('database read', silence)
            database_dict = loads(database)
            success('database loaded', silence)
            return database_dict

    def write(self, database: dict, silence: Silence = Silence.none) -> dict:
        """Writes on the database's path the new value of the database.
        If the database doesn't exist, it creates it.

        :param database: a dictionary containing the updated database
        :param silence: Used to silence logs. See rizlib.text.logs.Silence enum class.
        :return: the previous value of the database
        """
        old_db = self.read(Silence.success)
        with open(self.__path, 'w') as file:
            database_str = dumps(database)
            success('database parsed', silence)
            file.write(database_str)
            success('database updated', silence)

        return old_db

    @property
    def path(self) -> str:
        """Getter
        :return: path to json database
        """
        return self.__path

    def set_path(self, json_db_path: PathHint) -> str:
        """Setter
        :param json_db_path: path to json database
        :return: previous path to json database
        """
        old_path = self.__path
        self.__path = json_db_path
        return old_path


if __name__ == '__main__':
    pass
#     test = 'db_test'
#     db = JSONDatabase(test)
#
#     db_test = db.read()
#
#     print(db_test)
#
#     db_test = db.read()
#     print(db_test)
#
#     db_test |= {'nome': 'john smith'}
#     print(db_test)
#
#     old = db.write(db_test)
#     print(old)
#
#     print(db.read())
