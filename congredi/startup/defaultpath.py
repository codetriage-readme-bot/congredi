import os
defaultPath = os.path.expanduser('~') + '/.local/congredi/'
defaultFile = 'congrediSettings.yaml'


def normalConfigPath():
    if 'windows' == True:
        return 'windows path'
    if 'linux' == True:
        return 'linux path'
