from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2016.SkimTree_Bkg_m4l70 import * 
from Zprime.Dataset.Run2016.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 

from Zprime.StatTools.ParaYieldProducer import ParaYieldProducer

from Zprime.Config.MergeSampleDict import mergeSampleDict

import os

#out_path = "ParaInput/EXO-18-001-Nominal/2019-06-10/"
#out_path = "ParaInput/Run2017/2020-06-25/"
#out_path = "ParaInput/Run2016/2020-11-06/"
#out_path = "ParaInput/Run2016/2020-11-23_coup0.05/"
#out_path = "ParaInput/Run2016/2021-11-09/"
out_path = "ParaInput/Run2016/2022-03-06_ULdata/"

User                    = os.environ['USER']
nCores                  = 5
#lumi                    = 77.3
lumi                    = 35.9
outputDir               = system.getStoragePath()+"/Zprime/Zto4l/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + sigSampleDict.values()
#componentList           = sigSampleDict.values()
componentList           = dataSamples + bkgSamples + sigSamples
justEndSequence         = False
skipGitDetail           = True

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

mu_ch_sel_str = 'abs(event.idL1[0]) == 13 and abs(event.idL2[0]) == 13 and abs(event.idL3[0]) == 13 and abs(event.idL4[0]) == 13'

input_channel_dict      = {
        "4mu": LambdaFunc('event: '+mu_ch_sel_str),
        }

sequence                = signal_sequence
yieldProducer           = ParaYieldProducer("ParaYieldProducer",channelDict=input_channel_dict,)
sequence.add(yieldProducer)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "StatInput.root"

endSequence = EndSequence(skipHadd=justEndSequence)
