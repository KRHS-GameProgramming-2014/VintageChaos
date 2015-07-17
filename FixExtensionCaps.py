#FixExtensionCaps.py

import os

def fixFiles(folder):
    fls = os.listdir(folder)

    #print fls

    for f in fls:
        if f[-3:] == "PNG":
            cmd = ("mv " + folder + f + " " + folder + f[:-3] + "png")
            os.system(cmd)
        if os.path.isdir(f) and (f != "." or  f!= ".."):
            newFolder = (folder+f+"/")
            print newFolder
            fixFiles(newFolder)
            
fixFiles("Arrow Buttons/")
