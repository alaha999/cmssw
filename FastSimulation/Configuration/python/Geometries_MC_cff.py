import FWCore.ParameterSet.Config as cms

from FastSimulation.Configuration.Geometries_cff import *

# Apply Tracker and Muon misalignment
misalignedTrackerGeometry.applyAlignment = False
misalignedDTGeometry.applyAlignment = False
misalignedCSCGeometry.applyAlignment = False

#from Geometry.CaloEventSetup.AlignedCaloGeometryDBReader_cfi import*
#HcalGeometryFromDBEP.applyAlignment = False
