import nuke
import sys, os
import xo_Grade



# nuke menu
xolo_menu = nuke.menu('Nuke').addMenu('xolo')
xolo_menu.addCommand('xoTools/Comp/xoSmartGrade', 'xo_Grade.xo_Grade_node()')

#nuke nodes menu
xolo_menu = nuke.menu('Nodes').addMenu('xolo')
xolo_menu.addCommand('xoTools/Comp/xoSmartGrade', 'xo_Grade.xo_Grade_node()')