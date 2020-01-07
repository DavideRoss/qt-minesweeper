from configparser import ConfigParser

CONFIG_FILE_NAME = 'config.ini'

# TODO: handle exceptions

class Settings():
    CELL_SIZE = 32
    SIZE = [9, 9]
    MINES = 10

    @staticmethod
    def initialize(ctx):
        Settings.CFG_PATH = ctx.get_resource(CONFIG_FILE_NAME)

        Settings.config = ConfigParser()
        Settings.config.read(Settings.CFG_PATH)

        Settings.SIZE = [int(Settings.config.get('game', 'size_x')), int(Settings.config.get('game', 'size_y'))]
        Settings.MINES = int(Settings.config.get('game', 'mines'))

    @staticmethod
    def write_file(ctx):
        Settings.config.set('game', 'size_x', str(Settings.SIZE[0]))
        Settings.config.set('game', 'size_y', str(Settings.SIZE[1]))
        Settings.config.set('game', 'mines', str(Settings.MINES))

        with open(Settings.CFG_PATH, 'w') as f:
            Settings.config.write(f)