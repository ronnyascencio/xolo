"""
name = xo Work

version = 1.0
date = 8-31-2023
author = Ronny Ascencio
contact = ronnycompartist@gmail.com

-----------------------------------------------------------------------------------------------

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
import re
from xo_folder_show_template import create_folder_structure



# valirables path

main_path = os.path.dirname(__file__)
foldertemplate_path = os.path.join(main_path, 'setUpshow', 'showSetUp')
foldertemplate_shot_path = os.path.join(main_path, 'setUpshow', 'shotSetUp')

icons_path = os.path.normpath(os.path.join(main_path, "icons"))
image_filename = "cdwork.png"



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


        

class loaderSaver(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'xo Work', 'xo.saver')

        self.current_path = ""
        self.selected_sequence = ""
        self.selected_shot = ""
        self.selected_department = ""

        # List
        root_drivers = get_drives()
        

        dpt = ['', 'comp', 'environment', 'mattePainting', 'lighting', 'roto', 'prep', 'lookDev']
        plates = ['', 'sourceplate', 'undistorted', 'graded', 'denoised', 'reference']
        renders = ['', 'environment', 'lighting']
        asset_types = ['', 'matte', 'precomp', 'prep', 'backplate']


        #knobs
        #<font color="#69ff5e">
        self.logo = nuke.Boolean_Knob('', '<img src="C:/Users/ronny/.nuke/python/xolo/icons/xoWork.png" width=600 height=65><center>', False)
        self.loaderTitle = nuke.Text_Knob("loader", "<font size=5> <b>Loader")
        
        self.driversMenu = nuke.Enumeration_Knob('drivers', 'Drive', root_drivers)
        self.showMenu = nuke.Enumeration_Knob('show', 'Show', [''])
        self.showMenu.clearFlag(nuke.STARTLINE)
        self.setShowhButton = nuke.PyScript_Knob('setshow', "<font color='69ff5e'><b>Set Show Context")
        
        
        self.sequenceMenu = nuke.Enumeration_Knob('seq', 'Sequence', [''])
        
        self.shotMenu = nuke.Enumeration_Knob('shot', 'Shot', [''])
        self.shotMenu.clearFlag(nuke.STARTLINE)

        self.departmentMenu = nuke.Enumeration_Knob('department', 'Department', dpt)
        self.versionMenu = nuke.Enumeration_Knob('shotversion', 'Version', [''])
        self.versionMenu.clearFlag(nuke.STARTLINE)
        self.refreshButton = nuke.PyScript_Knob('refresh', "<font color='69ff5e'><b>refresh")
        self.loaderTitleText = nuke.Text_Knob("loadertext", "<b>SHOT LOADER")
        self.loadButton = nuke.PyScript_Knob('lodaer', "<font color='69ff5e'><b>LOAD SCRIPT")
        self.loadButton.setFlag(nuke.STARTLINE)
        
        
        # saver
        
        self.div1 = nuke.Text_Knob("div1", "")
        self.saverTitle = nuke.Text_Knob("saver", "<font size=5> <b>Saver")
        self.prefix = nuke.String_Knob("prefix", "Prefix", "")
        self.saveButton = nuke.PyScript_Knob('savnew', "<b>SAVE SCRIPT")
        self.saveButton.clearFlag(nuke.STARTLINE)
        
        self.saveNewButton = nuke.PyScript_Knob('savnew', "<b>SAVE NEW VERSION")
        self.saveNewButton.setFlag(nuke.STARTLINE)
        
        
        self.div2 = nuke.Text_Knob("div2", "")
        
        # # asset Manager
        # self.assetManagerTitle = nuke.Text_Knob("assetManager", "<font size=5> <b>Asset Import")
        # self.ddassetTitleText = nuke.Text_Knob("2dassettext", "<b>2D ASSETS")
        # self.plateMenu = nuke.Enumeration_Knob('plateMenu', 'Plate', plates)
        # self.plateversionMenu = nuke.Enumeration_Knob('plateVersion', 'Version', dpt)
        # self.plateversionMenu.clearFlag(nuke.STARTLINE)
        # self.plateImportButton = nuke.PyScript_Knob('plateImport', "<b>import plate")
        # self.plateImportButton.clearFlag(nuke.STARTLINE)
        
        
        # self.rendersMenu = nuke.Enumeration_Knob('rendersMenu', 'Renders', renders)
        # self.rendersversionMenu = nuke.Enumeration_Knob('rendersVersion', 'Version', dpt)
        # self.rendersversionMenu.clearFlag(nuke.STARTLINE)
        # self.rendersImportButton = nuke.PyScript_Knob('renderImport', "<b>import render")
        # self.rendersImportButton.clearFlag(nuke.STARTLINE)
        
        
        # self.assetMenu = nuke.Enumeration_Knob('assetMenu', 'Asset type', asset_types)   
        # self.assetversionMenu = nuke.Enumeration_Knob('assetVersion', 'Version', dpt)
        # self.assetversionMenu.clearFlag(nuke.STARTLINE)
        # self.assetImportButton = nuke.PyScript_Knob('assetImport', "<b>import asset")
        # self.assetImportButton.clearFlag(nuke.STARTLINE)
        
        
        # # 3D assets
        
        # self.tdassetTitleText = nuke.Text_Knob("3dassettext", "<b>3D ASSETS")
        
        # # Camera
        
        # self.cameraText = nuke.Text_Knob("cameraText", "Camera")
        # self.cameraversionMenu = nuke.Enumeration_Knob('cameraVersion', 'Version', ['versiontest'])
        # self.cameraversionMenu.clearFlag(nuke.STARTLINE)
        # self.cameraImportButton = nuke.PyScript_Knob('cameraImport', "<b>import camera")
        # self.cameraImportButton.clearFlag(nuke.STARTLINE)
        
        # # Geo 
        
        # self.geoText = nuke.Text_Knob("geoText", "Geo")
        # self.geoversionMenu = nuke.Enumeration_Knob('geoVersion', 'Version', ['versiontest'])
        # self.geoversionMenu.clearFlag(nuke.STARTLINE)
        # self.geoImportButton = nuke.PyScript_Knob('geoImport', "<b>import geo")
        # self.geoImportButton.clearFlag(nuke.STARTLINE)
        
        # # Lnes Distortion
        
        # self.lensDistortText = nuke.Text_Knob("lensDistortText", "Lens Distort")
        # self.lensDistortversionMenu = nuke.Enumeration_Knob('lensDistortVersion', 'Version', ['versiontest'])
        # self.lensDistortversionMenu.clearFlag(nuke.STARTLINE)
        # self.lensDistortImportButton = nuke.PyScript_Knob('lensDistortImport', "<b>import lens distort")
        # self.lensDistortImportButton.clearFlag(nuke.STARTLINE)
        
        
        
        



        



        #adding knobs 
        for knob in (self.loaderTitle, self.driversMenu, self.showMenu, self.setShowhButton, self.sequenceMenu, self.shotMenu, self.loaderTitleText, self.departmentMenu, self.versionMenu, self.refreshButton,  self.loadButton, self.div1, self.saverTitle, self.prefix, self.saveButton, self.saveNewButton, self.div2):
               self.addKnob(knob)
               
# knob changes function
    

    def knobChanged(self, knob):
        shows_path = os.path.join(self.driversMenu.value(), 'job', 'shows')
    
        if knob == self.driversMenu:
            # Handle driver change
            if os.path.exists(shows_path):
                shows = ['']
                shows.extend(os.listdir(shows_path))
                self.showMenu.setValues(shows)
            else:
                self.showMenu.setValues([''])



        elif knob == self.showMenu:
            # Handle showMenu change
            all_shows = self.showMenu.values()
            index = int(self.showMenu.getValue())
            
            # Ensure the index is within range
            if 0 <= index < len(all_shows):
                selected_show_name = all_shows[index]
                print("Selected Show:", selected_show_name)
            else:
                print("Invalid index!")


        
        if knob == self.setShowhButton:
            selected_driver = self.driversMenu.value()
            selected_show = self.showMenu.value()
            
            if self.current_path:  # Check if it's been set
                self.current_path = os.path.join(selected_driver, 'job', 'shows', selected_show, 'sequences')
            
            
            self.current_path = os.path.join(selected_driver, 'job', 'shows', selected_show, 'sequences')
            show_master_path = self.current_path.replace('\\', '/')
            # Print the path to see the result (optional)
            print("Current Path:", show_master_path)
            self.driversMenu.setEnabled(False)
            self.showMenu.setEnabled(False)


            
            



            if os.path.exists(self.current_path):
                sequences = ['']
                sequences.extend(os.listdir(self.current_path))
                self.sequenceMenu.setValues(sequences)



                
        if knob == self.sequenceMenu:
            self.selected_sequence = self.sequenceMenu.value()
            if self.current_path:  # Check if it's been set
                shots_path = os.path.join(self.current_path, self.selected_sequence)
            
            
            if os.path.exists(shots_path):
                shots = ['']
                shots.extend(os.listdir(shots_path))
                self.shotMenu.setValues(shots)
                
                # Also reset the department and version menus
                self.departmentMenu.setValue('')
                self.versionMenu.setValue('')
                self.departmentMenu.setValues([''])
                self.versionMenu.setValues([''])

            print("Current shot path:", shots_path)




        if knob == self.shotMenu: # <- This was missing. After selecting a shot, we want to populate the departments.
            self.selected_shot = self.shotMenu.value()
            department_path = os.path.join(self.current_path, self.selected_sequence, self.selected_shot)
            
            if os.path.exists(department_path):
                departments = ['']
                departments.extend(os.listdir(department_path))
                self.departmentMenu.setValues(departments)
                



        if knob == self.departmentMenu:
            self.selected_shot = self.shotMenu.value()
            self.selected_department = self.departmentMenu.value()
            
            if self.current_path and self.selected_sequence and self.selected_shot:  # Check if they've been set
                script_path = os.path.join(self.current_path, self.selected_sequence, self.selected_shot, self.selected_department, 'Nuke', 'scripts')

            
            if os.path.exists(script_path):
                scripts = ['']
                scripts.extend(os.listdir(script_path))
                self.versionMenu.setValues(scripts)
                
                
                
        if knob == self.refreshButton:
            self.departmentMenu.setValue('')
            self.versionMenu.setValue('')
            self.departmentMenu.setValues([''])
            self.versionMenu.setValues([''])
        
            # Refresh the departments for the current shot
            self.selected_shot = self.shotMenu.value()
            
            
            department_path = os.path.join(self.current_path, self.selected_sequence, self.selected_shot)
            
            if os.path.exists(department_path):
                departments = ['']
                departments.extend(os.listdir(department_path))
                self.departmentMenu.setValues(departments)






                
        if knob == self.loadButton:
            self.selected_version = self.versionMenu.value()
            open_script_path = os.path.join(self.current_path, self.selected_sequence, self.selected_shot, self.selected_department, 'Nuke', 'scripts', self.selected_version)
            
            print(open_script_path) # debug script to open path
            if '.nk' in self.selected_version:
                nuke.scriptOpen(open_script_path)
                print('shot loaded:', self.selected_version) #debu to know what shot was loaded
        
        
        # Saver



        


        savePath = os.path.join(self.current_path, self.selected_sequence, self.selected_shot, self.selected_department, 'Nuke', 'scripts\\')
        script_base_name = savePath + self.selected_shot + '_' + self.selected_department
        
        
        print(savePath)
        print(script_base_name)
        
        
        if knob == self.saveButton:
            if self.prefix:
                prefix = self.prefix.value()
                script_prefix_save = script_base_name + '_' + prefix + '_' + 'v001' + '.nk' 
                nuke.scriptSave(script_prefix_save)
                print(script_prefix_save)
                nuke.message('script saved')
                nuke.scriptOpen(script_prefix_save)
            else:
                save_script = script_base_name + 'v001' + '.nk'
                nuke.scriptSave(save_script)
                print(save_script)
                nuke.message('script saved')
                nuke.scriptOpen(save_script)


        if knob == self.saveNewButton:
            if nuke.root().name():
                
                nukescripts.script_and_write_nodes_version_up()
            else:
                nuke.message('you do not have any script open')
            
                
            
            
                

 
            
                


def addxoPanel():
    iPanel = loaderSaver()
    return iPanel.addToPane()

paneMenu = nuke.menu('Pane')
paneMenu.addCommand('xoWork', addxoPanel)
nukescripts.registerPanel('xo.saver', addxoPanel)