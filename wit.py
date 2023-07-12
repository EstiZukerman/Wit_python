from file_handler import FileHandler
import logging


class Logger:
    logging_format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
    logging_file_path = r'C:\עבודות\Esti\bootcamp\Wit_python\.wit\loggers\logger.txt'
    logging.basicConfig(filename=logging_file_path, format=logging_format, level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    @staticmethod
    def logging_to_file(*args):
        def wrapper(func):
            def inner_wrapper():
                logging_format = "%(asctime)s LEVEL: %(levelname)s MSG: %(message)s"
                logging_file_path = r'C:\עבודות\Esti\bootcamp\Wit_python\.wit\loggers\logger.txt'
                logging.basicConfig(filename=logging_file_path, format=logging_format, level=logging.DEBUG)
                logger = logging.getLogger(__name__)
                logger.info(func)
                if len(args) > 0:
                    func(args)
                else:
                    func()
            return inner_wrapper
        return wrapper
class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_wit_path()

    @Logger.logging_to_file()
    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            pass
            # TODO raise exception- cant init initial dir
        else:
            FileHandler.create_dir(".wit")
            FileHandler.create_dir(".wit/images")
            FileHandler.create_dir(".wit/staging_area")

    @staticmethod
    def add(args):
        item_to_move_path = FileHandler.get_full_path(args[0])
        Wit.move_to_staging(item_to_move_path)

    @staticmethod
    def move_to_staging(item_to_move):
        staging_area_path = FileHandler.join_path(FileHandler.find_wit_path(), 'staging_area')
        FileHandler.copy_item(item_to_move, staging_area_path)


Wit.init()
