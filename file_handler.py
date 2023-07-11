import os


class FileHandler:
    working_directory = None

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
        pass

    @classmethod
    def find_base_path(cls):
        if not cls.base_path:
            raise Exception("Not a wit repository")

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
        pass