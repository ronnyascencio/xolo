"""
name = xo SHow Directory

version = 1.0
date = 8-31-2023
author = Ronny Ascencio
contact = ronnycompartist@gmail.com

----------------------------------------------------------------------------------

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
import nukescripts
import os
import sys
import shutil
from xo_folder_show_template import create_folder_structure



# valirables path

main_path = os.path.dirname(__file__)
foldertemplate_path = os.path.join(main_path, 'setUpshow', 'showSetUp')
foldertemplate_shot_path = os.path.join(main_path, 'setUpshow', 'shotSetUp')





#function to get the drivers in the system 
def get_drives():
    drives = ['']
    if os.name == 'nt':  # For Windows systems
        for drive in range(ord('A'), ord('Z') + 1):
            drive = chr(drive) + ':'
            if os.path.exists(drive):
                drives.append(drive)
    elif os.name == 'posix':  # For Unix/Linux/Mac systems
        mounts = os.popen('mount').read().split('\n')
        for mount in mounts:
            if mount.startswith('/dev/'):
                drive = mount.split()[0]
                drives.append(drive)
    return drives



class show_dir_create(nukescripts.PythonPanel):

    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Show Creator')


        drives = get_drives()





        self.driveMenu = nuke.Enumeration_Knob('drives', 'drives', drives)
        self.showName = nuke.String_Knob('showname', 'show name', '')
        
        


        for knob in (self.driveMenu, self.showName):
            
            self.addKnob(knob)


    def knobChanged(self, knob):
        if knob.name() == "OK":
            drive = self.driveMenu.value()
            show_name = self.showName.value()
            show_Path = os.path.join(drive, 'job', 'shows', show_name)
            print(show_Path)
            if os.path.exists(show_Path):
                nuke.message(' show already exist ')
            else:
                os.makedirs(show_Path)
                create_folder_structure(foldertemplate_path, show_Path)
                nuke.message(' show created succesfuly ')


def addShowPanel():
    iPanel = show_dir_create()
    return iPanel.showModalDialog() 