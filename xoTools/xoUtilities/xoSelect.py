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



class node_selector(nukescripts.PythonPanel):
    def __init__(self):
        nodes = []
        def create_list_nodes():
            
            #populate the list nodes
            for n in nuke.allNodes():
                name = n.name()
                
                nodeclass = n.Class()
            
                nodes.append(name)
            
            
            nodes.sort()

        create_list_nodes()
        nukescripts.PythonPanel.__init__(self, 'Node Selector')
        self.nodes_type = nuke.Enumeration_Knob('nodes', 'nodes', nodes)
        
        
        self.addKnob(self.nodes_type)
        
        
    def knobChanged(self, knob):
        if knob.name() == "OK":
            node_name = self.nodes_type.value()
            nukescripts.clear_selection_recursive()

            node_to_select = nuke.toNode(node_name)
            if node_to_select:
                node_to_select.knob('selected').setValue(True)
                # Manipulate the Node Graph. Zoom on the Selected Node
                nuke.zoom(2, [node_to_select.xpos(), node_to_select.ypos()])
            else:
                nuke.message("Node not found!")
        
        
def addnodePanel():
    iPanel = node_selector()
    return iPanel.showModalDialog()      
    
    
    



