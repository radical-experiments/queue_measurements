import os
import sys
import json
import random
import radical.pilot as rp

SAMPLE_SIZE = 20
WALLTIME = 120   #In minutes
OVERHEAD = 3    #Overhead incurred throughout the process
CORES = 32
UTIL = 1        #Percent of Cores Utilized

def job_select():
    pass    

if sys.argv[1] == "stampede" or sys.argv[1] == "gordon" or sys.argv[1] == "comet" or sys.argv[1] == "supermic":
    res = sys.argv[1]
    random.seed()
else:
    sys.exit()


for run in range(SAMPLE_SIZE):

    with open('resource_handle.json') as j:
        conf = json.load(j)

    res_conf = conf[res]

    try:    
        session = rp.Session()
        session_id = session.uid
        pmgr = rp.PilotManager(session=session)
        pdescs = list()
    
        pd_init = { 'resource'      :   res_conf['name'],
                    'queue'         :   res_conf['queue'],
                    'access_schema' :   res_conf['access_schema'],
                    'cores'         :   CORES,
                    'runtime'       :   WALLTIME,
                    'project'       :   'TG-MCB090174'
                  }
        pdescs.append(rp.ComputePilotDescription(pd_init))
        pilots = pmgr.submit_pilots(pdescs)
    
        umgr = rp.UnitManager(session=session)
        umgr.add_pilots(pilots)
    
        cuds = list()
    
        for task in range(CORES * UTIL):
            cud = rp.ComputeUnitDescription()
            cud.executable = '/bin/sleep'
            cud.arguments = [(WALLTIME - OVERHEAD) * 60] #/bin/sleep assumes input argument in sec
            cuds.append(cud)
    
        umgr.submit_units(cuds)
        umgr.wait_units()

    except Exception as e:
        print "Caught Exception %s\n" % e

    except(KeyboardInterrupt, SystemExit) as e:
        print "Caught A Keyboard Error"

    finally:
        os.system("radicalpilot-close-session -m export -s {0}".format(session_id))
        os.system("mv {0}.json {1}".format(session_id, res))
        session.close()
