# coding: utf-8

import os
import numpy as np
from .. import _base




import numpy as np

class PlantarArchAngle(_base.DatasetT2, _base.Dataset1D):
    def _set_values(self):
        self.datafile = 'C:\\Users\\yiman\\anaconda3\\Lib\\site-packages\\spm1d\\data\\datafiles\\OUKA_XR_FE.txt'
        
        # Load the data from the text file
        Y = np.loadtxt(self.datafile)  # or np.genfromtxt if the file has missing data or complex structure

        self.cite = 'Caravaggi, P., Pataky, T., Günther, M., Savage, R., & Crompton, R. (2010). Dynamics of longitudinal arch support in relation to walking speed: contribution of the plantar aponeurosis. Journal of Anatomy, 217(3), 254–261. http://doi.org/10.1111/j.1469-7580.2010.01261.x'

        # Assuming the data is loaded successfully, split it
        self.YA = Y[0:24]  # Select rows 10 to 19 (adjust as needed)
        self.YB = Y[24:]    # Select rows 20 to the end (adjust as needed)

        # Initialize the other attributes
        self.z = None
        self.df = None
        self.p = None


class SimulatedTwoLocalMax(_base.DatasetT2, _base.Dataset1D):
	def _set_values(self):
		self.datafile = os.path.join(_base.get_datafilepath(), 'ex_sim_twolocalmax.npy')
		Y             = np.load(self.datafile)
		self.YA       = Y[:6]
		self.YB       = Y[6:]
		self.z        = None
		self.df       = None
		self.p        = None









