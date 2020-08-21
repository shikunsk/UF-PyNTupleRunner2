from Core.Sequence import Sequence
from Core.EndSequence import EndSequence
from Core.OutputInfo import OutputInfo
from Core.Utils.LambdaFunc import LambdaFunc
from Utils.System import system

from Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 import * 
#from Zprime.Dataset.Run2017.SkimTree_promptCR_Bkg_m4l70 import *
from Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 import * 
from Zprime.Sequence.RecoSequence import * 
from Zprime.Config.PlotDefinition import *

from Plotter.Plotter import Plotter
from Plotter.PlotEndModule import PlotEndModule

from Zprime.Config.MergeSampleDict import mergeSampleDict

User                    = os.environ['USER']
#out_path                = "SR/DataMCDistributions/2019-06-03_Run2017/"
#out_path                = "DataMCDistributions/Run2017/test_3P1F/"
#out_path                = "DataMCDistributions/Run2017/2020-05-14_1Gev_m4l100To120_CR/"
#out_path                = "DataMCDistributions/Run2017/2020-05-15_1Gev_m4lHiggsRange/"
#out_path                = "DataMCDistributions/Run2017/2020-05-22_1To5Gev_m4l80To100_CR/"
#out_path                = "DataMCDistributions/Run2017/2020-06-02_signal5To70Gev_lepeff/"
#out_path                = "DataMCDistributions/Run2017/testforsig/"
out_path                = "DataMCDistributions/Run2017/2020-08-19_1Gev_SR/"
lumi                    = 41.4
nCores                  = 5
outputDir               = system.getStoragePath()+"/"+User+"/Zprime/Zto4l/"+out_path
nEvents                 = -1
disableProgressBar      = False
#componentList           = bkgSamples + [sigSampleDict[m] for m in [10,40,70]]
#componentList           = bkgSamples + sigSampleDict.values()
#componentList           = sigSampleDict.values()
#componentList           = dataSamples + bkgSamples# + dataSamples
componentList           = sigSamples + bkgSamples
justEndSequence         = False

plots = general_4mu_plots

for dataset in componentList:
    if dataset.isMC:
        dataset.lumi = lumi
    for component in dataset.componentList:
        component.maxEvents = nEvents

plotter                 = Plotter("Plotter",plots)

sequence                = signal_sequence
sequence.add(plotter)

outputInfo              = OutputInfo("OutputInfo")
outputInfo.outputDir    = outputDir
outputInfo.TFileName    = "DataMCDistribution.root"

endSequence = EndSequence(skipHadd=justEndSequence)
endModuleOutputDir = system.getPublicHtmlPath()+"/Zprime/Zto4l/"+out_path
endSequence.add(PlotEndModule(endModuleOutputDir,plots,skipSF=False))
