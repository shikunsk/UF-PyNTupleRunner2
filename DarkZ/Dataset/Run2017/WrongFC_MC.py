
from Core.ComponentList import *
from Core.Dataset import Dataset

bkgSkimTreeDir              = "/raid/raid7/lucien/Higgs/DarkZ-NTuple/20190307/SkimTree_DarkPhoton_WrongFC_Run2017Data_m4l70/"
inUFTier2                   = False

bkgTreeDir_2lskim           = '/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/ZPlusX_Early2017_v1/'
bkgTreeDir_4lskim           = '/cms/data/store/user/t2/users/klo/Higgs/DarkZ/NTuples/BkgMC_Run2017/'
sumWeightHist               = "Ana/sumWeights"

# ____________________________________________________________________________________________________________________________________________ ||
WFC_Reducible_cmpList = ComponentList(
        [
            Component("WFC_Reducible",bkgSkimTreeDir+"Data_Run2017-17Nov2017-v1_noDuplicates_FRWeightFromVukasin.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WFC_Reducible = Dataset(
        "WFC_Reducible",
        WFC_Reducible_cmpList,
        isMC = True,
        skipWeight = True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
# qqZZ
qqZZ_cmpList = ComponentList(
        [ 
            Component("WFC_Irreducible",bkgSkimTreeDir+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )

qqZZTo4L = Dataset(
        "WFC_Irreducible",
        qqZZ_cmpList,
        isMC                = True,
        xs                  = 1.256,
        )
qqZZTo4L.setSumWeight(
        bkgTreeDir_4lskim+"ZZTo4L_13TeV_powheg_pythia8_RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M50",bkgSkimTreeDir+"DYJetsToLL_M50.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M50 = Dataset(
        "DYJetsToLL_M50",
        DYJetsToLL_M50_cmpList,
        isMC = True,
        xs = 6104, 
        )
DYJetsToLL_M50.setSumWeight(
        bkgTreeDir_2lskim+"DYJetsToLL_M50.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
DYJetsToLL_M10To50_cmpList = ComponentList(
        [
            Component("DYJetsToLL_M10To50",bkgSkimTreeDir+"DYJetsToLL_M10To50.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
DYJetsToLL_M10To50 = Dataset(
        "DYJetsToLL_M10To50",
        DYJetsToLL_M10To50_cmpList,
        isMC = True,
        xs = 6104, 
        )
DYJetsToLL_M10To50.setSumWeight(
        bkgTreeDir_2lskim+"DYJetsToLL_M10To50.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
TTJets_cmpList = ComponentList(
        [
            Component("TTJets",bkgSkimTreeDir+"TTJets.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
TTJets = Dataset(
        "TTJets",
        TTJets_cmpList,
        isMC = True,
        xs = 87.31, 
        )
TTJets.setSumWeight(
        bkgTreeDir_2lskim+"TTJets.root",
        sumWeightHist,
        True,
        )

# ____________________________________________________________________________________________________________________________________________ ||
WZTo3LNu_cmpList = ComponentList(
        [
            Component("WZTo3LNu",bkgSkimTreeDir+"WZTo3LNu.root","passedEvents",inUFTier2=inUFTier2),
        ]
        )
WZTo3LNu = Dataset(
        "WZTo3LNu",
        WZTo3LNu_cmpList,
        isMC = True,
        xs = 0.04430, 
        )
WZTo3LNu.setSumWeight(
        bkgTreeDir_2lskim+"WZTo3LNu.root",
        sumWeightHist,
        True,
        )

