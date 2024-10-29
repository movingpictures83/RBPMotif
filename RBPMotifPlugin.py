import sys
import os
import pandas as pd
import re
import numpy as np
import scipy as sp
from collections import defaultdict
from itertools import islice
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import PyPluMA
import PyIO

class RBPMotifPlugin:
 def input(self, inputfile):
  self.parameters = PyIO.readParameters(inputfile)
 def run(self):
     pass
 def output(self, outputfile):
  expfile = PyPluMA.prefix()+"/"+self.parameters["metastatic"]#'input/high-vs-low_metastatic_lines_GSE59857.txt'
  exp = pd.read_csv(expfile, sep='\t', header=0, index_col=0)
  exp_r = exp
  #RDfile = PyPluMA.prefix()+"/"+self.parameters["logfoldchange"]#'input/high-vs-low_metastatic_lines_GSE59857_logFC_refseq.txt'
  motifs = pd.read_csv(PyPluMA.prefix()+"/"+self.parameters["motifmap"], sep='\t', header=0)
  motifs.set_index('RBP', inplace=True, drop=False)
  motifs['motif'].unique().tofile(outputfile, sep="\n", format="%s")

