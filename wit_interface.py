import sys
from wit import Wit


class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        match command:
            case "init":
                Wit.init()
            case "add":
                Wit.add(args)


if __name__ == "__main__":
    # TODO: handle edge cases
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)
