"""
Copyright (c) 2023, Ronny Ascencio
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Redistribution of this software in source or binary forms shall be free
      of all charges or fees to the recipient of this software.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




"""
import nuke
import sys, os
import xo_Show_Directory
import xo_Shot_Create
import xo_Work
from xo_SetUp import project_set_up




# Custom Writes

import xoWrite


# reload

import importlib

importlib.reload(xoWrite)

importlib.reload(xo_Work)



name = 'xolo :  xoPipe loading'
print(f'{name}')




project_panel_instance = project_set_up()

# nuke menu
xolo_menu = nuke.menu('Nuke').addMenu('xolo')
xolo_menu.addCommand('xoPipe/Write/xoWrite	Ctrl+Alt+W', 'xoWrite.write_create()', 'ctrl+alt+w')
xolo_menu.addCommand('xoPipe/Work/xoShow', 'xo_Show_Directory.addShowPanel()')
xolo_menu.addCommand('xoPipe/Work/xoShot', 'xo_Shot_Create.addShotPanel()')
xolo_menu.addCommand('xoPipe/Work/xoWork	Ctrl+F', 'xo_Work.addxoPanel()', 'ctrl+f')
xolo_menu.addCommand('xoPipe/Work/xoSetUp', 'project_panel_instance.show()')

#nuke nodes menu
xolo_menu = nuke.menu('Nodes').addMenu('xolo')
xolo_menu.addCommand('xoPipe/Write/xoWrite	Ctrl+Alt+W', 'xoWrite.write_create()', 'ctrl+alt+w')
xolo_menu.addCommand('xoPipe/Work/xoShow', 'xo_Show_Directory.addShowPanel()')
xolo_menu.addCommand('xoPipe/Work/xoShot', 'xo_Shot_Create.addShotPanel()')
xolo_menu.addCommand('xoPipe/Work/xoWork	Ctrl+F', 'xo_Work.addxoPanel()', 'ctrl+f')
xolo_menu.addCommand('xoPipe/Work/xoSetUp', 'project_panel_instance.show()')






