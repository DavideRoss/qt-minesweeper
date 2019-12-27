from os import listdir
from PySide2.QtGui import QIcon

icons = {}
styles = {}

# TODO: refactor?
for f in listdir('res/icons'):
    name = f.replace('.png', '').upper()
    styles[name] = 'border-image: url(res/icons/{}) 0 0 0 0 stretch stretch; border-width: 0px'.format(f)

def init():
    global icons

    for f in listdir('res/icons'):
        name = f.replace('.png', '').upper()
        icons[name] = QIcon('res/icons/{}'.format(f))

        styles[name] = 'border-image: url(res/icons/{}) 0 0 0 0 stretch stretch; border-width: 0px'.format(f)

def get_neighbors_style(count):
    return 'border-image: url(res/icons/icon_neighbors) 0 0 0 {} repeat repeat; border-width: 0px'.format(str(count * 32))