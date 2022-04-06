from __future__ import division
from Core.Module import Module
from Utils.DeltaR import deltaR

class AnalysisSkimmer(Module):
    def __init__(self,name,cutflow="Zprime-SR"):
        super(AnalysisSkimmer,self).__init__(name)
        self.cutflow = cutflow

    def analyze(self,event):
        sigmass = 0
        sigcount = False
        #if event.Event[0] == 175773413:
            #print(event.mass4l[0],event.massZ1[0],event.massZ2[0])
            #print(event.idL1[0],event.idL2[0],event.idL3[0],event.idL4[0])
        if "zpToMuMu_" in self.dataset.name:
            sigcount = True
            sigmass = int(self.dataset.name[10:-2])
        if self.cutflow == "Zprime-SR":
            #if event.pTL1[0] < 20. or event.pTL2[0] < 10.:
                #print(event.pTL1[0],event.pTL2[0],event.mass4l[0])
            if event.pTL1[0] < 20. or event.pTL2[0] < 10.: return False
            #if event.mass4l[0] < 80. or event.mass4l[0] > 100.: return False
            if event.mass4l[0] < 135.: return False
            #if event.mass4l[0] > 118. and event.mass4l[0] < 130.: return False
            #if event.mass4l[0] > 120.: return False
            #if event.mass4l[0] < 118. or event.mass4l[0] > 130.: return False
            if event.massZ1[0] < 12. or event.massZ1[0] > 120.: return False
            if event.massZ2[0] < 4. or event.massZ2[0] > 120.: return False
            #if event.massZ2[0] < 15 * 0.98 or event.massZ2[0] > 15 * 1.02 : return False
            #if sigcount and sigmass < 42:
                #if event.massZ2[0] < sigmass * 0.98 or event.massZ2[0] > sigmass * 1.02 : return False
            #elif sigcount and sigmass > 42:
                #if event.massZ1[0] < sigmass * 0.98 or event.massZ1[0] > sigmass * 1.02 : return False
            #if (event.massZ1[0] < 83.3 or event.massZ1[0] > 86.7) and (event.massZ2[0] < 83.3 or event.massZ2[0] > 86.7) : return False
            event.sy = sigmass
            #if event.Event[0] == 175773413:
                #print(event.mass4l[0],event.massZ1[0],event.massZ2[0],event.passedFullSelection[0],event.pTL3[0],event.pTL4[0],event.phiL3[0],event.phiL4[0],event.etaL3[0],event.etaL4[0])
                #print(event.lep_RelIsoNoFSR[0],event.lep_RelIsoNoFSR[1],event.lep_RelIsoNoFSR[2],event.lep_RelIsoNoFSR[3])
                #print(event.passedZXCRSelection[0])
            if "ZPlusX" not in self.dataset.name and not event.passedFullSelection[0]: return False
            #if "Data" in self.dataset.name:
                #if abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13:
                    #if event.Event[0] == 161799416:
                        #print(event.mass4l[0],event.massZ1[0],event.massZ2[0])
            if event.pTL1[0]<20 and event.pTL2[0]<20 and event.pTL3[0]<20 and event.pTL4[0]<20: print("worng")
            #if event.nZXCRFailedLeptons[0] != 1: return False
            #if event.nZXCRFailedLeptons[0] != 2: return False
            zplep1 = -1
            zplep2 = -1
            if "zpToMuMu" in self.dataset.name:
                for i in range(0,int(event.GENlep_id.size())):
                    if abs(event.GENlep_id[i]) == 13 and event.GENlep_MomId[i] == 999888:
                        if zplep1 == -1:
                            zplep1 = i
                        elif zplep2 == -1:
                            zplep2 = i
                        else:
                            break
                if zplep1 != -1 and zplep2 != -1:
                    event.deltaRGENZpLep = deltaR(event.GENlep_eta[zplep1],event.GENlep_phi[zplep1],event.GENlep_eta[zplep2],event.GENlep_phi[zplep2])
            return True
        return False
