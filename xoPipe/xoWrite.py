"""
name = xoWrite

version = 1.0
date = 8-31-2023
author = Ronny Ascencio
contact = ronnycompartist@gmail.com

--------------------------------------------------------------------------------------------

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
import re
import threading
import time

filepath = os.path.dirname(nuke.root().name())




    

def setcontext():
   
    
    
    
    root_name = nuke.root().name()
    
    if '.nk' in root_name:
        root_name.replace('.nk', '')
        root_name_split = root_name.split('/')
        shot_name = root_name_split[-1]
        shot_split = shot_name.split('_')
        shot_split.pop(-1)
        shot_core_name = '_'.join(shot_split)
    
    
    
    # shot version 
    script_name = nuke.root().name()
    shot_version = script_name.split('_')[-1].replace('.nk', '')
    
    #shot name
    shot_name_code = shot_core_name
    
    platetype = nuke.thisNode()['asset_type'].value()
    
    root_name = nuke.root().name()
    path_split = root_name.split('/')
    
    main_folder_path = '/'.join(path_split[0:6])
    
    save_path = main_folder_path + '/renders/' + platetype + '/' + str(shot_name_code) + '_' + platetype + '_' + shot_version

    nuke.message(save_path)
    nuke.thisNode()['write_path'].setValue(save_path)
    
    print(save_path)
   
    



# Before render checks


def precheck():
    # in develop

    nuke.message('ready to render')
    
    
    






    

#Write Node Creation

def write_create():
    selected_node = nuke.selectedNode()
    if selected_node == False:
        nuke.message('please seleecy a node first')
    else:

        write_node = nuke.nodes.Write()
        write_node['tile_color'].setValue(0x03021F)
        publish_tab = nuke.Tab_Knob("PublishTab", "Publish")
        write_node.addKnob(publish_tab)
        write_asset_type_knob = nuke.Enumeration_Knob('asset_type', 'Asset Type', ['asset', 'delivery', 'mattes', 'paint', 'comp'])
        write_node.addKnob(write_asset_type_knob)
        write_path_knob = nuke.String_Knob("write_path", " File Path")
        write_node.addKnob(write_path_knob)
        write_node['file'].setValue('[value write_path].%04d.exr')
        
       
        write_node['label'].setValue('[value file]')
        script_knob = nuke.PyScript_Knob("set_context_button", "Set Context", 'import xoWrite; xoWrite.setcontext()')
        write_node.addKnob(script_knob)
        write_node['file_type'].setValue('exr')
        
        # render settings
        write_node['beforeRender'].setValue('import xoWrite; xoWrite.precheck()')
        write_node['afterRender'].setValue('nukescripts.script_and_write_nodes_version_up()')
        write_node['raw'].setValue(True)
        write_node['create_directories'].setValue(True)
        
        selected_node = nuke.selectedNode()
        if selected_node:
            write_node.setInput(0, selected_node)


