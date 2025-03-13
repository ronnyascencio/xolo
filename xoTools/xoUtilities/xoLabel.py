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
import nukescripts




def new_label():
    if nuke.selectedNodes():
        
        node_panel = nuke.Panel('node set up')
        node_panel.addSingleLineInput('label name', 'label name')
        node_panel.addSingleLineInput('node name', 'node name')
        

        if node_panel.show():
           
            
           
            for selected in nuke.selectedNodes():
                selected['label'].setValue(node_panel.value('label name'))
                selected['name'].setValue(node_panel.value('node name'))
                col = nuke.getColor()
                selected['tile_color'].setValue(col)
    else:
        nuke.message('please select a node first')


