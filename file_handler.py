import os
import shutil


class FileHandler:
    working_directory = os.getcwd()
    base_path = None
    # def __init__(self):
    # self.base_path = None

    # @property
    # def base_path(self):
    #     if not self.base_path:
    #         raise Exception("Not a wit repository")
    #     for path in walk_up()
    #
    # @base_path.setter
    # def base_path(self, base_path):
    #     self.base_path = base_path

    @staticmethod
    def create_dir(path):
        os.mkdir(path)

    @classmethod
    def find_wit_path(cls):
        if cls.base_path:
            return cls.base_path
        files_tree = FileHandler.walk_up_in_path(cls.working_directory, "C:\\")
        for path in files_tree:
            if os.path.isdir(os.path.join(path, '.wit')):
                cls.base_path = os.path.join(path, '.wit')
                return cls.base_path
        return None

    @classmethod
    def get_full_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            raise
            # TODO: handle file doesn't exist
        return full_path

    @classmethod
    def copy_item(cls, origin, target):
        if os.path.isfile(origin):
            shutil.copy2(origin, target)
            return
        shutil.copytree(origin, target)

    @staticmethod
    def walk_up_in_path(path, top):
        while path != top:
            yield path
            path = os.path.dirname(path)
    @staticmethod
    def join_path(path, path_to_join):
        return os.path.join(path, path_to_join)
# TODO: a decorator to check if path is exists
