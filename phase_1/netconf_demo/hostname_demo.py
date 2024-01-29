from oc_system import openconfig_system
from pprint import pprint as pp
from pyangbind.lib.serialise import pybindIETFXMLEncoder
from ncclient import manager

HOSTNAME = 'DC1_LEAF1'
DEVICE_IP = '172.100.100.3'

oc = openconfig_system()

oc.system.config.hostname = HOSTNAME

config = '<config>\n' + pybindIETFXMLEncoder.serialise(oc.system) + '</config>\n'
print(config)

eos = manager.connect(host=DEVICE_IP, port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

print(eos.edit_config(target='running', config=config, default_operation='merge'))