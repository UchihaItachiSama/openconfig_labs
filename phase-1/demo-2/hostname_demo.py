#!/usr/bin/python3

from oc_system import openconfig_system
import pyangbind.lib.pybindJSON as pybindJSON
from pprint import pprint as pp

HOSTNAME = 'DC1_SPINE1'

oc_sys = openconfig_system()

oc_sys.system.config.hostname = HOSTNAME

pp(pybindJSON.dumps(oc_sys))

with open("./{}_hostname.json".format(HOSTNAME), "w") as fobj:
    fobj.write(pybindJSON.dumps(oc_sys, mode="ietf"))

fobj.close()