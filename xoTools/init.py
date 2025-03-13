import os
import sys
import nuke


filedir = os.path.dirname(__file__)
qt_path = filedir + './qt'
nuke.pluginAddPath(filedir + "./xoKernel")
nuke.pluginAddPath(filedir + "./xoGrade")
nuke.pluginAddPath(filedir + "./xoUtilities")


sys.path.append(qt_path)