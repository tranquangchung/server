import sys
import os

dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')) + "/Training_server"
sys.path.append(dir_path)

import musicmain
def get_music():
    return musicmain.get_music()
