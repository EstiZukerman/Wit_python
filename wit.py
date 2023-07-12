from file_handler import FileHandler


class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_wit_path()

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


Wit.add(["exe.txt"])
