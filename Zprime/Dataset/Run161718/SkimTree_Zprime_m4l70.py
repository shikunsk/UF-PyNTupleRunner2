import Zprime.Dataset.Run2016.SkimTree_Bkg_m4l70 as sample2016
import Zprime.Dataset.Run2016.SkimTree_Zprime_m4l70 as sampleSig2016
import Zprime.Dataset.Run2017.SkimTree_Bkg_m4l70 as sample2017
import Zprime.Dataset.Run2017.SkimTree_Zprime_m4l70 as sampleSig2017
import Zprime.Dataset.Run2018.SkimTree_Bkg_m4l70 as sample2018
import Zprime.Dataset.Run2018.SkimTree_Zprime_m4l70 as sampleSig2018

for sample in sample2016.bkgSamples:
    sample.name += "_Run2016"
    sample.lumi = 35.9
for sample in sample2017.bkgSamples:
    sample.name += "_Run2017"
    sample.lumi = 41.4
for sample in sample2018.bkgSamples:
    sample.name += "_Run2018"
    sample.lumi = 59.7

bkgSamples = sample2016.bkgSamples + sample2017.bkgSamples + sample2018.bkgSamples


for sample in sampleSig2016.sigSamples:
    #sample.name += "_Run2016"
    #sample.lumi = 35.9
    sample.lumi = 137
for sample in sampleSig2017.sigSamples:
    #sample.name += "_Run2017"
    sample.lumi = 41.4
for sample in sampleSig2018.sigSamples:
    #sample.name += "_Run2018"
    sample.lumi = 59.7

sigSamples = sampleSig2016.sigSamples# + sampleSig2017.sigSamples + sampleSig2018.sigSamples
#for sample in sigSamples:
    #sample.lumi = 137


#dataSamples = [sample2016.data2016,sample2017.data2017,sample2018.data2018,]
dataSamples = [sample2016.data2016,sample2017.data2017,sample2018.data2018]
