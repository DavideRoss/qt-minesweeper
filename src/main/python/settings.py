from configparser import ConfigParser

CONFIG_FILE_NAME = 'config.ini'

class Settings():
    CELL_SIZE = 32
    SIZE = [9, 9]
    MINES = 10

    # 0: beginner
    # 1: intermediate
    # 2: expert
    # 3: custom
    DIFFICULTY_SETTING = 0

    @staticmethod
    def initialize(ctx):
        Settings.CFG_PATH = ctx.get_resource(CONFIG_FILE_NAME)

        Settings.config = ConfigParser()
        Settings.config.read(Settings.CFG_PATH)

        Settings.CELL_SIZE = int(Settings.config.get('game', 'cell_size'))
        Settings.SIZE = [int(Settings.config.get('game', 'size_x')), int(Settings.config.get('game', 'size_y'))]
        Settings.MINES = int(Settings.config.get('game', 'mines'))
        Settings.DIFFICULTY_SETTING = int(Settings.config.get('game', 'difficulty'))

    @staticmethod
    def write_file(ctx):
        Settings.config.set('game', 'cell_size', str(Settings.CELL_SIZE))
        Settings.config.set('game', 'size_x', str(Settings.SIZE[0]))
        Settings.config.set('game', 'size_y', str(Settings.SIZE[1]))
        Settings.config.set('game', 'mines', str(Settings.MINES))
        Settings.config.set('game', 'difficulty', str(Settings.DIFFICULTY_SETTING))

        with open(Settings.CFG_PATH, 'w') as f:
            Settings.config.write(f)