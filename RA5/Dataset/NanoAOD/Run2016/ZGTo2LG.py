from Core.ComponentList import *
from Core.Dataset import Dataset

cmp = Component(
        "ZGTo2LG",
        "/cms/data/store/user/klo/RA5/NTuples/2016/NanoAOD/MC/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/InclusiveSelection_v1/180509_145232/0000/",
        "Events",
        keyword="tree",
        inUFTier2=True,
        )

cmpList = ComponentList(
        [cmp,],
        )

ZGTo2LG = Dataset(
        "ZGTo2LG",
        cmpList,
        xs                  = 123.9, #pb
        )
