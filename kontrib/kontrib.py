import sys
from settings import Settings


class Kontrib():
    def __init__(self):
        pass

    def run(self, argv):
        Settings.set_settings(argv)


if __name__ == "__main__":
    kontrib = Kontrib()
    kontrib.run(sys.argv)
