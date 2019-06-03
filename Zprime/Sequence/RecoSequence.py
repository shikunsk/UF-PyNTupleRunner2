from Core.Sequence import Sequence

from Zprime.Skimmer.AnalysisSkimmer import AnalysisSkimmer
from DarkZ.Weighter.DataMCWeighter import DataMCWeighter
from DarkZ.Weighter.NLOWeighter import NLOWeighter

from NanoAOD.Weighter.XSWeighter import XSWeighter # Stealing module from NanoAOD framework

SRSkimmer               = AnalysisSkimmer("SRSkimmer")

dataMCWeighter          = DataMCWeighter("DataMCWeighter")
nloWeighter             = NLOWeighter("NLOWeighter")
xsWeighter              = XSWeighter("XSWeighter")

signal_sequence = Sequence()
signal_sequence.add(SRSkimmer)
signal_sequence.add(xsWeighter)
signal_sequence.add(dataMCWeighter)
signal_sequence.add(nloWeighter)
