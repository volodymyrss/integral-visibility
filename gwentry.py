from numpy import *
import pyfits
import healpy
import healtics
from integralclient import converttime
import ephem
from astropy.coordinates import SkyCoord
from astropy import units as u
import ephem    

import sys
#sys.path.append("/home/vsavchenko/work/integral-visibility")
sys.path.append("../integral-counterpart")
reload(integralvisibility)
from integralvisibility import Visibility

import counterpart
reload(counterpart)
from counterpart import Counterpart


class GWEntry:
    def __init__(self,l):
        self.read_em_str(l)
        
    def read_em_str(self,entry_str):
        if entry_str[0]=="#":
            return
        
        
        fields="GPS UTC mass1 mass2 dist SNR RA dec inclination skymap".split()        
        for f,v in zip(fields,entry_str.split(";")):
           # print f,v
            setattr(self,f,v.replace("\"",""))
            
        self.utc=self.UTC.replace(" ","T")
        self.ijd=float(converttime("UTC",self.utc,"IJD"))
        
        self.skymap=self.skymap[:-1]
            
    def __nonzero__(self):
        try:
            a=str(self.GPS)
            return True
        except:
            return False
            
    def __repr__(self):
        try:
            return str(self.GPStime)
        except:
            return "undef"
        
    def compute_visibility(self):
        coord=SkyCoord(ra.flatten(),dec.flatten(),unit=u.deg)
        m=Visibility().for_time("2016-10-09T17:31:06",coord=coord)

        figure(figsize=(20,10))
        scatter(ra,dec,s=100,c=m,lw=0,alpha=0.4)
        
    def compute_extend(self):
        # how many points
        pass

        

def interate_entries():
    gw_table=[]

    for l in open(rootd+"/sim_20160929/summary_sim_20160929.txt"):
        if len(gw_table)>20: continue
               
        gw=GWEntry(l)
        if not gw: continue
            
        gw_table.append(gw)
        
        
        

