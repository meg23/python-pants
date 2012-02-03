import os
import sys
from lib.virtualenv import Setupenv
from settings import *

class Pants(object):
    def __init__(self):
        self.dirpath = os.getcwd() 
        self.projectname = "%s" % (project)
        self.projectpath = "%s/%s" % (self.dirpath, self.projectname)
        self.newbin = "%s/bin" % (self.projectpath)
    
    def makeenv(self):
        if not os.path.isdir("%s" % (self.newbin)):
            newenv = Setupenv("%s/%s" % (self.dirpath, self.projectname))
            
    def setupmodules(self):
        os.system("%s/python %s/easy_install pip" % (self.newbin, self.newbin))
        os.system("%s/python %s/pip install %s" % 
                  (self.newbin, self.newbin, " ".join(modules)))
        
    def activate(self):
        execfile("%s/activate_this.py" % 
                 self.newbin, dict(__file__="%s/activate_this.py" % self.newbin))

if __name__ != "__main__":
    a = Pants()
    a.makeenv()
    a.setupmodules()
    a.activate()
