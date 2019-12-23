import yaml
import os

class Config:
    def __init__(self):
        self.rootpath = rootpath = os.path.dirname(os.getcwd())
        self.datapath = os.path.join(rootpath, 'data')
        self.casepath = os.path.join(rootpath, 'cases')
        self.picturepath = os.path.join(rootpath, 'Picture')
