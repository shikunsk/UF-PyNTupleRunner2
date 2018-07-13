import ROOT

from Core.Module import Module

class GenWeightCounter(Module):
    def __init__(self,name,postfix=""):
        super(GenWeightCounter,self).__init__(name)
        self.postfix = postfix

    def begin(self):
        self.writer.book("SumWeight"+self.postfix,"TH1D","SumWeight"+self.postfix,"",1,-0.5,0.5)
        self.writer.book("EventCount"+self.postfix,"TH1D","EventCount"+self.postfix,"",1,-0.5,0.5)
        
    def analyze(self,event):
        self.writer.objs["SumWeight"+self.postfix].Fill(0.,event.genWeight[0])
        self.writer.objs["EventCount"+self.postfix].Fill(0.)
        return True
