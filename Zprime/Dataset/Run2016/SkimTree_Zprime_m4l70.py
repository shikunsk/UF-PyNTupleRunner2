from Core.ComponentList import *
from Core.Dataset import Dataset
from Utils.System import system
from Utils.SumWeight import handleSumWeight

#bkgSkimTreeDir      = system.getStoragePath()+"/lucien/Higgs/Zprime-NTuple/20190605/SkimTree_Zprime_Run2017Data_m4l70/"
#bkgSkimTreeDir      = system.getStoragePath()+"/Zprime/20200212_Zto4l/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir      = system.getStoragePath()+"/Zprime/20200212_Zto4l/SkimTree_Run2018_MMM_MC/"
bkgSkimTreeDir      = system.getStoragePath()+"/Zprime/20211023_Zto4l/SkimTree_Run2018_MMM_MC/"
#bkgSkimTreeDir      = system.getStoragePath()+"/Zprime/20200212_Zto4l/mllLowGev/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir      = system.getStoragePath()+"/Zprime/20200212_Zto4l/test_4GeV/SkimTree_Run2017_MMM_MC/"
#bkgSkimTreeDir      = system.getStoragePath()+"/kshi/Zprime/20200212_Zto4l/unskim/SkimTree_Run2017_MMM_MC/"
bkgSkimTreeDir2     = bkgSkimTreeDir
#bkgTreeDir          = "/cmsuf/data/store/user/muahmad/rootfiles_2017/"
bkgTreeDir          = "/cmsuf/data/store/user/t2/users/kshi/Zprime_signal/2018/"
dataTreeDir         = bkgSkimTreeDir
inUFTier2           = False
sumWeightHist       = "Ana/sumWeights"
saveSumWeightTxt    = False

# ____________________________________________________________________________________________________________________________________________ ||
# zpToMuMu
sigSampleDict = {}
zp_mass_points = [
        #1,
        5,
        #50,
        #60,
        #70,
        #10,
        #20,
        #30,
        #15,
        #40,
        #25,
        #35,
        #45,
        #55,
        #65,
        #70,
        ]# + range(20,80,10)

zpToMuMuXS_dict = {
        1: 5.715,
        5: 0.5555*((0.008/0.1)**2),
        10: 0.2173*((0.009/0.1)**2),
        15: 0.1141*((0.01/0.1)**2),
        20: 0.0650*((0.012/0.1)**2),
        25: 0.0382,
        30: 0.0226*((0.02/0.1)**2),
        35: 0.0134,
        40: 0.0079*((0.03/0.1)**2),
        45: 0.0045,
        50: 0.0025*((0.06/0.1)**2),
        55: 0.0014,
        60: 0.0007*((0.15/0.1)**2),
        65: 0.0004,
        70: 0.0002*((0.5/0.1)**2),
        }

# ____________________________________________________________________________________________________________________________________________ ||
for m in zp_mass_points:
    sigSampleDict[m] = Dataset(
        "zpToMuMu_M"+str(m),
        ComponentList([ 
            #Component("zpToMuMu_M"+str(m),bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.root","passedEvents",inUFTier2=inUFTier2),
            Component("zpToMuMu_M"+str(m),bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8_muahmad-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-MINIAOD.root","passedEvents",inUFTier2=inUFTier2),
        ],
        ),
        isMC                = True,
        xs                  = zpToMuMuXS_dict[m],# *((0.01/0.1)**2),
        isSignal            = True,
        )
    handleSumWeight(
        sigSampleDict[m],
        system,
        #bkgTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.root",
        bkgTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8_muahmad-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-MINIAOD.root",
        sumWeightHist,
        True,
        saveSumWeightTxt,
        #bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.txt",
        bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8_muahmad-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-MINIAOD.txt",
        #bkgSkimTreeDir+"ZpTomumu_M"+str(m)+"_13TeV_MadGraph5_pythia8-v4_muahmad-RunIISummer16MiniAODv2.txt",
        )

# ____________________________________________________________________________________________________________________________________________ ||

sigSamples = sigSampleDict.values()

