import nuke
import sys, os
import xo_Kernel



# nuke menu
xolo_menu = nuke.menu('Nuke').addMenu('xolo')
xolo_menu.addCommand('xoTools/Comp/xoKernel', 'xo_Kernel.xo_Kernel_node()')

#nuke nodes menu
xolo_menu = nuke.menu('Nodes').addMenu('xolo')
xolo_menu.addCommand('xoTools/Comp/xoKernel', 'xo_Kernel.xo_Kernel_node()')