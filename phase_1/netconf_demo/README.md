# NETCONF-Demo

## Overview

In this demo, we will take a look at few examples related to `NETCONF` using `ncclient` with Arista cEOS-Lab devices.

## Requirements

Confirm the following packages are installed, if not install them using `pip`

```shell
python3 -m pip freeze | egrep "pyang|pyangbind|ncclient"
```

* `containerlab` and `docker` installed
* Arista cEOS-Lab image installed

```shell
$ docker images | egrep "IMAGE|ceosimage"

REPOSITORY               TAG          IMAGE ID       CREATED         SIZE
ceosimage                4.30.1F      72e796e3929e   3 weeks ago     2.44GB
```

## Steps

* Start the `ceos_lab` lab

```shell
cd openconfig-labs/phase-1/ceos_lab

sudo containerlab deploy -t topology.yml
```

* Navigate to the `netconf_demo` directory

```shell
cd openconfig-labs/phase-1/netconf_demo
```

### Getting Capabilities

* Using the following Python file we will get the client and server NETCONF capabilities

```python
from ncclient import manager

eos = manager.connect(host='172.100.100.3', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

print("\n########## CLIENT CAPABILITIES ##########\n")
for item in eos.client_capabilities:
    print(item)

print("\n########## SERVER CAPABILITIES ##########\n")
for item in eos.server_capabilities:
    print(item)
```

* Execute the file and we can see the client and server NETCONF capabilities

```shell
$ python3 capabilites_demo.py

########## CLIENT CAPABILITIES ##########

urn:ietf:params:netconf:base:1.0
urn:ietf:params:netconf:base:1.1
urn:ietf:params:netconf:capability:writable-running:1.0
urn:ietf:params:netconf:capability:candidate:1.0
urn:ietf:params:netconf:capability:confirmed-commit:1.0
urn:ietf:params:netconf:capability:rollback-on-error:1.0
urn:ietf:params:netconf:capability:startup:1.0
urn:ietf:params:netconf:capability:url:1.0?scheme=http,ftp,file,https,sftp
urn:ietf:params:netconf:capability:validate:1.0
urn:ietf:params:netconf:capability:xpath:1.0
urn:ietf:params:netconf:capability:notification:1.0
urn:ietf:params:netconf:capability:interleave:1.0
urn:ietf:params:netconf:capability:with-defaults:1.0

########## SERVER CAPABILITIES ##########

urn:ietf:params:netconf:base:1.0
urn:ietf:params:netconf:base:1.1
urn:ietf:params:xml:ns:netconf:base:1.0
urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring
urn:ietf:params:netconf:capability:writable-running:1.0
urn:ietf:params:netconf:capability:candidate:1.0
urn:ietf:params:netconf:capability:url:1.0?scheme=file,flash,ftp,http
<--snipped-->
```

### Get states

* Using the `get_demo.py` script, which uses ncclient `get` operation to get the state data. It also uses filter to specify the portion of state data to retrieve.

* Example

```python
import xml.dom.minidom
from ncclient import manager

eos = manager.connect(host='172.100.100.2', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

# Get system information
systemState = """
<system>
    <state>
    </state>
</system>
"""

<---snipped--->

reply = eos.get(filter=("subtree", systemState))

print(xml.dom.minidom.parseString(str(reply)).toprettyxml())
```

* Execute the script to retrieve the system state

```shell
$ python3 get_demo.py

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:431b9fed-ab51-4342-8719-e90a543e2a22">
	<data>
		<system xmlns="http://openconfig.net/yang/system">
			<state>
				<boot-time>1706167316567450112</boot-time>
				<current-datetime>2024-01-25T10:33:22Z</current-datetime>
				<hostname>spine1</hostname>
				<last-configuration-timestamp>1706178738766270140</last-configuration-timestamp>
				<software-version>4.30.1F-32308478.4301F (engineering build)</software-version>
			</state>
		</system>
	</data>
</rpc-reply>
```

### Get Configuration

* Using the `get_config_demo.py` script, which uses ncclient `get-config` operation with a filter to retrieve part of the configuration

* Example

```python

```

### Configuring hostname

* Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $(/usr/bin/env python3 -c 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))') -f pybind -p ../yang_modules/ -o ./oc_system.py ../yang_modules/openconfig-system.yang
```

* The above command will generate the Python module `oc_system.py` from the `openconfig-system.yang` file. Run this command to verify the file.

```shell
ls oc_system.py
```

* Next, we will use this Python module to generate the JSON data model and configure it using NETCONF via `ncclient` python library

```python
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
```

* Checking the switch we can see the hostname has been configured

```shell
$ docker exec -it clab-openconfig-lab-leaf1 Cli -c "show hostname"
Hostname: DC1_LEAF1
FQDN:     DC1_LEAF1
```
