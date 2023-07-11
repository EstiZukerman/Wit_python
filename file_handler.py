import os
import shutil


class FileHandler:
    def __init__(self):
        self.base_path = None

    @property
    def base_path(self):
        if not self.base_path:
            raise Exception("Not a wit repository")

    @base_path.setter
    def base_path(self, base_path):
        self.base_path = base_path

    @staticmethod
    def create_dir(path):
        os.mkdir(path)

    @classmethod
    def find_base_path(cls):
        if cls.base_path:
            return cls.base_path
        # TODO: find first dir's path with .wit in it
        found = False
        # TODO: handle not wit repo
        # raise Exception("Not a wit repository")

    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            pass
            # TODO: handle file doesn't exist

    @classmethod
    def copy_item(cls, origin, target):
        if os.path.isfile(origin):
            shutil.copyfile(origin, target)
            return
        shutil.copytree(origin, target)

# TODO: a decorator to check if path is exists
