#!/usr/bin/env python

from Gaudi.Configuration import *

from Configurables import CEPCDataSvc
dsvc = CEPCDataSvc("EventDataSvc")

from Configurables import PlcioWriteAlg
alg = PlcioWriteAlg("PlcioWriteAlg")
alg.OutputCol.Path = "MCParticleCol"

from Configurables import PodioOutput
out = PodioOutput("out")
out.filename = "test.root"
out.outputCommands = ["keep *"]

# ApplicationMgr
from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = [alg, out],
                EvtSel = 'NONE',
                EvtMax = 10,
                ExtSvc=[dsvc],
                OutputLevel=DEBUG
)
