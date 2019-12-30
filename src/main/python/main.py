import sys

from os import listdir
from PySide2.QtGui import QIcon
from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property
from components import MainWindow
from settings import Settings

class AppContext(ApplicationContext):
    def run(self):
        Settings.initialize(self)
        
        self.main_window.show()
        return self.app.exec_()

    @cached_property
    def icons(self):
        icns = {}

        for f in listdir(self.get_resource('icons')):
            name = f.replace('.png', '').upper()
            path = self.get_resource('icons/' + f).replace('\\', '/')
            icns[name] = 'border-image: url(\'{}\') 0 0 0 0 stretch stretch; border-width: 0px'.format(path)

        return icns

    @cached_property
    def main_window(self):
        return MainWindow(self)

    @cached_property
    def app_icon(self):
        return QIcon(self.get_resource('icons/icon_mine_transparent.png'))

    def get_neighbors_style(self, count):
        path = self.get_resource('icons/icon_neighbors.png').replace('\\', '/')
        return 'border-image: url(\'{}\') 0 0 0 {} repeat repeat; border-width: 0px'.format(path, str(count * 32))

if __name__ == '__main__':
    app_ctx = AppContext()

    test = app_ctx.icons

    exit_code = app_ctx.run()
    sys.exit(exit_code)