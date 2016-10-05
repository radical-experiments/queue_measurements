import os
import json
import random
import radical.pilot as rp
import karnak_reader as kr

SAMPLE_SIZE = 30
wALLTIME = 30   #In minutes
CORES = 16
UTIL = 1        #Percent of Cores Utilized

def job_select():
    pass    

if sys.argv[1] == "stampede" or sys.argv[1] == "gordon" or sys.argv[1] == "comet" or sys.argv[1] == supermic:
    res = sys.argv[1]
    random.seed()
else:
    sys.exit()


for run in range():

    with open('resource_handle.json') as j:
        conf = json.load(j)

    res_conf = conf[res]

    try:    
        session = rp.Session()
        pmgr = rp.PilotManager(session=session)
        pdesc = list()
    
        pd_init = { 'resource'      :   res_conf['name'],
                    'queue'         :   res_conf['queue'],
                    'access_schema' :   res_conf['access_schema'],
                    'cores'         :   CORE_SIZE,
                    'runtime'       :   wALLTIME,
                    'project'       :   'TG-MCB090174'
                  }
        pdescs.append(rp.ComputePilotDescription(pd_init))
        pilots = pmgr.submit_pilots(pdescs)
    
        umgr = rp.UnitManager(session=session)
        umgr.add_pilots(pilots)
    
        cuds = list()
    
        for task in range(CORE_SIZE * UTIL):
            cud = rp.ComputeUnitDescription()
            cud.executable = '/bin/sleep'
            cud.arguments = [RUN_TIME]
            cuds.append(cud)
    
        umgr.submit_units(cuds)
        umgr.wait_units()

    except Exception as e:
        print "Caught Exception %s\n" % e

    except(KeyboardInterrupt, System) as e:
        print "Caught A Keyboard Error"

    finally:
        os.system("radicalpilot-close-session -m export -s {0}".format(session_id))
        os.system("mv {0}+.json {1}".format(session_id, resource))
        session.close()