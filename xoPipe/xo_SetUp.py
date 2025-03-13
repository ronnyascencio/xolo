"""
name = xo setUp

version = 1.0
date = 8-31-2023
author = Ronny Ascencio
contact = ronnycompartist@gmail.com

-----------------------------------------------------------------------------------------

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

from PySide2 import QtWidgets, QtGui, QtCore

class project_set_up(QtWidgets.QWidget):
    def __init__(self):
        super(project_set_up, self).__init__()

        # Set panel properties
        self.setWindowTitle('Project Set Up')
        self.setMinimumSize(300, 200)

        #  layouts
        layout = QtWidgets.QVBoxLayout(self)
        
        
        Title = QtWidgets.QLabel(' Set the Comp')
        Title.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        Title.setFont(font)
        layout.addWidget(Title)

        # adding the buttons 
        format = QtWidgets.QPushButton('set Format', self)
        frame_range = QtWidgets.QPushButton('set Frame Range', self)
        fps = QtWidgets.QPushButton('set FPS', self)
        layout.addWidget(format)
        layout.addWidget(frame_range)
        layout.addWidget(fps)
        format.clicked.connect(self.on_format_clicked)
        frame_range.clicked.connect(self.on_frame_range_clicked)
        fps.clicked.connect(self.on_fps_clicked)

        # Add layout to the main container
        self.setLayout(layout)
        

    def on_format_clicked(self):
        selected_node = nuke.selectedNode()
        if selected_node is not None and selected_node.Class() == 'Read':
            
           knob_value = selected_node['format'].value()
           nuke.root().knob('format').setValue(knob_value)
        else:
            nuke.message('please select a read node')
        
        
    def on_frame_range_clicked(self):
        selected_node = nuke.selectedNode()
        if selected_node:
            
           knob_value_first = selected_node['first'].value()
           knob_value_last = selected_node['last'].value()
           nuke.root().knob('first_frame').setValue(knob_value_first)
           nuke.root().knob('last_frame').setValue(knob_value_last)
           
           
    
    
    def on_fps_clicked(self):
        nuke.root()['fps'].setValue(24)