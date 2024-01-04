from oc_system import openconfig_system
from pprint import pprint as pp
from pyangbind.lib.serialise import pybindIETFXMLEncoder
from ncclient import manager

HOSTNAME = 'DC1_LEAF1'

oc = openconfig_system()

oc.system.config.hostname = HOSTNAME

config = '<config>\n' + pybindIETFXMLEncoder.serialise(oc.system) + '</config>\n'

pp(config)

eos = manager.connect(host='172.100.100.3', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

pp(eos.edit_config(target='running', config=config, default_operation='merge'))