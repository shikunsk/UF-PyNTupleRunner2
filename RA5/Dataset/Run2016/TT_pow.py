from Core.ComponentList import *
from Core.Dataset import Dataset
from Core.Utils.MakeComponent import makeComponents
from DataMC.Heppy.Run2016.HaddMC import TT_pow

sampleName   = "TT_pow"
#fileName     = "treeProducerSusyRA5.root"
#TreeDir      = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1_LeptonJetRecleaner_TT_pow/"
#sumweight_path  = "/cms/data/store/user/t2/users/klo/HeppyTree/heppy_80X_RA5_Legacy/July18_v1/"
#inUFTier2    = True
#filePath = os.path.join(sumweight_path,sampleName,fileName)

#cmp = makeComponents(sampleName, TreeDir, "Events", inUFTier2)

TT_pow.componentList = cmpList

#TT_pow= Dataset(
#        "TT_pow",
#        cmpList,
#        isMC                = True,
#        xs                  = 1,
#        )
#TT_pow.setSumWeight(filePath,"SumGenWeights",inUFTier2)

Samples = [
        TT_pow
        ]
