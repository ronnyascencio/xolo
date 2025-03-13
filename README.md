Index
Page.

1.Introduction 3

2. Installation 4

3. xoPipe 5
   Work
   I. xoShow
   II. xoShot
   III. xoWork
   IV. xoSetUp
   Write
   I.Custom Write

4. xoTools 6
   Utilities
   I. Labeler
   II. Node Selector
   Comp
   I. xo Kernel
   II. xoSmartGrade

Introduction

Thank you for giving this tool a shot!

“XOLO” is a ready to use tool for solo artists that wants to simplify the task of creating folder structure for each project, including sequence and shot names folders, giving the artist the availability to just type and create the necessary to start working.

This is a free tool within tools that helps you to start work in the project and not worry about the boring stuff of creating folders and set paths and names.

Installation

Video guide

1. Unzip the file you already download and you will find a folder called “xolo”, go to your Nuke root folder and create a folder called “python” this folder you can call it whatever you want, in my case I called like this, then copy the “xolo” folder in to it :

Nuke folder :
Linux: /home/login name/.nuke
Mac OS X: /Users/login name/.nuke
Windows: C:\Users\user name\.nuke

The path of the python folder should be: “C:\Users\user name\.nuke\python”

2. In the “.nuke” folder you should have an init.py and menu.py files if not create it. Open the init.py file with a text editor and use the following code to tell nuke where it should find “xolo” folder.

Copy this code:

nuke.pluginAddPath("./python/xolo")

Now you can start Nuke.

xoPipe

xoPipe menu includes different tools that help you to set the “project” from the “Show” name to save and open a script and also set frame range and resolution size based on the Read node.

Here is what the set of tools you can use:

Work and Write categories.
Click to see the video

xoTools

xoTools include 2 categories “comp” and “utilities” this are tools for a daily work task i develop this tools base on the needs of the work to speed up a bit of time while working

See the video to know how the tools works:

Click to see the video

Thank you!

For any feedback, suggestions, bugs, or feature requests, please send me a message at the following email address: ronnycompartist@gmail.com
