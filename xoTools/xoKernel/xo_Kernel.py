import nuke
import os
"""
setting up the environment variables
"""

filedir = os.path.dirname(__file__)
nkdir = filedir + '\\nkfiles'


def xo_Kernel_node():
    node_path = os.path.join(nkdir, 'xo_kernel.nk')
    nuke.nodePaste(node_path)