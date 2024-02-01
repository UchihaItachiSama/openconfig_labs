# NETCONF Demo

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

## Starting the lab

* Start the `ceos_lab` lab

```shell
cd openconfig_labs/phase_1/ceos_lab

sudo containerlab deploy -t topology.yml
```

* Navigate to the `netconf_demo` directory

```shell
cd openconfig_labs/phase_1/netconf_demo
```

## Getting Capabilities

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

eos.close_session()
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

## Get the states

* Using the `get_demo.py` script, which uses the ncclient `get` operation to get the state data. It also uses a filter to specify the portion of state data to retrieve.

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

eos.close_session()
```

* Execute the script to retrieve the system state

```xml
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

*NOTE: Replace the variable name to get different states*

## Get Configuration

* Using the `get_config_demo.py` script, which uses ncclient `get-config` operation with a filter to retrieve parts of the configuration

* Example

```python
import xml.dom.minidom
from ncclient import manager

eos = manager.connect(host='172.100.100.2', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

# Get hostname config
hostname = """
<system>
    <config>
        <hostname>
        </hostname>
    </config>
</system>
"""

<--snipped-->

reply = eos.get_config(source="running", filter=("subtree", users))

print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

eos.close_session()
```

* Execute the script to retrieve the configuration

```xml
$ python3 get_config_demo.py

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:5ca1dad0-7550-4bd7-be52-67af33d00b23">
	<data xmlns:netconf="http://arista.com/yang/rpc/netconf" netconf:time-modified="2024-01-30T06:53:00.775202565Z">
		<system xmlns="http://openconfig.net/yang/system">
			<config>
				<hostname>spine1</hostname>
			</config>
		</system>
	</data>
</rpc-reply> 
```

*NOTE: Replace the variable name to get different states*

## Configuring Devices

### Configuring hostname with edit-config & merge

* Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $(/usr/bin/env python3 -c 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))') -f pybind -p ../yang_modules/ -o ./oc_system.py ../yang_modules/openconfig-system.yang
```

* The above command will generate the Python module `oc_system.py` from the `openconfig-system.yang` file. Run this command to verify the file.

```shell
ls oc_system.py
```

* Next, we will use this Python module to generate the JSON data structure and configure the hostname using NETCONF via `ncclient` python library. Here we are using `edit-config` operation with the `merge` operation.

```python
import xml.dom.minidom
from ncclient import manager
from oc_system import openconfig_system
from pyangbind.lib.serialise import pybindIETFXMLEncoder


# Update hostname [ merge ]
def hostname(eos):
    HOSTNAME = 'DC1_LEAF1'
    oc_sys = openconfig_system()
    oc_sys.system.config.hostname = HOSTNAME
    config = '<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">\n' + pybindIETFXMLEncoder.serialise(oc_sys.system) + '</config>'
    #Print generated XML data
    print("\n{}\n".format(config))
    #Apply the configuration on the device
    print(eos.edit_config(target="running", config=config, default_operation="merge"))

<--snipped-->
```

* Execute the script and confirm the hostname has been configured,

```xml
$ python3 config_demo.py

<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
<system xmlns="http://openconfig.net/yang/system">
  <config>
    <hostname>DC1_LEAF1</hostname>
  </config>
</system>
</config>

<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:145227b0-d03a-40a2-821f-ac2170acdece"><ok></ok></rpc-reply>
```

```shell
$ docker exec -it clab-openconfig-lab-leaf1 Cli
DC1_LEAF1>enable
DC1_LEAF1#show running-config section hostname
hostname DC1_LEAF1
DC1_LEAF1#show hostname
Hostname: DC1_LEAF1
FQDN:     DC1_LEAF1
```

### Configuring DNS Servers using edit-config and merge

* Similarly, let's add DNS nameservers using `edit-config` and `merge` operation

```python
# Add DNS [ merge ]
def nameServers(server, eos):
    oc_sys = openconfig_system()
    oc_sys.system.dns.servers.server.add(server)
    dns_srv = oc_sys.system.dns.servers.server[server]
    dns_srv.config.address = server
    dns_srv.config.port = '53'
    config = '<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">\n' + pybindIETFXMLEncoder.serialise(oc_sys.system) + '</config>'
    #Print generated XML data
    print("\n{}\n".format(config))
    #Apply the configuration on the device
    print(eos.edit_config(target="running", config=config, default_operation="merge"))
```

* After the script is executed we can see DNS servers are configured,

```shell
$ docker exec -it clab-openconfig-lab-leaf1 Cli
DC1_LEAF1>enable
DC1_LEAF1#show running-config section name-server
ip name-server vrf default 1.0.0.1
ip name-server vrf default 1.1.1.1
```

### Replacing DNS Servers configuration using edit-config and merge

* Here, we will use the `edit-config` operation with the `replace` operation to replace the DNS configuration,

```python
# Replace DNS configuration
def replaceDNS(eos):
    config = """
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <system xmlns="http://openconfig.net/yang/system">
            <dns>
                <servers nc:operation="replace">
                    <server>
                        <address>9.9.9.9</address>
                        <config>
                            <address>9.9.9.9</address>
                            <port>53</port>
                        </config>
                    </server>
                    <server>
                        <address>8.8.8.8</address>
                        <config>
                            <address>8.8.8.8</address>
                            <port>53</port>
                        </config>
                    </server>
                </servers>
            </dns>
        </system>
    </config>
    """
    print("\n{}\n".format(config))
    #Apply the configuration on the device
    print(eos.edit_config(target="running", config=config, default_operation="none"))
```

* After executing the script we can see the DNS server configuration has been replaced with new servers,

```shell
$ docker exec -it clab-openconfig-lab-leaf1 Cli
DC1_LEAF1>enable
DC1_LEAF1#show running-config section name-server
ip name-server vrf default 8.8.8.8
ip name-server vrf default 9.9.9.9
```

### Deleting DNS Server using edit-config and delete

* Here, we will use the `edit-config` operation with `delete` operation to remove one of the DNS servers,

```python
# Delete operation
def deleteDNS(eos):
    config = """
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <system xmlns="http://openconfig.net/yang/system">
            <dns>
                <servers>
                    <server>
                        <address nc:operation="delete">9.9.9.9</address>
                    </server>
                </servers>
            </dns>
        </system>
    </config>
    """
    print("\n{}\n".format(config))
    #Apply the configuration on the device
    print(eos.edit_config(target="running", config=config, default_operation="none"))
```

* After executing the script, we can see the Quad9 DNS server has been removed.

```shell
$ docker exec -it clab-openconfig-lab-leaf1 Cli
DC1_LEAF1>enable
DC1_LEAF1#show running-config section name-server
ip name-server vrf default 8.8.8.8
```

### Modifying running-config with lock operation

* Here, we will use the `edit-config` operation with the `running` configuration datastore. It uses a `lock` operation.

```python
# Modify running configuration with lock
def runningConfigLock(eos):
    config_intf = """
    <config>
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface>
                <name>
                    Ethernet1
                </name>
                <config>
                    <description>
                        P2P_LINK_TO_DC1_SPINE1_Ethernet1
                    </description>
                </config>
            </interface>
        </interfaces>
    </config>
    """
    print("\n{}\n".format(config_intf))
    #Apply the configuration on the device
    with eos.locked("running"):
        input("\nRunning-config locked! Press any key to continue...")
        print(eos.edit_config(target="running", config=config_intf, default_operation="merge"))
        input("\nRunning-config modified! Press any key to continue...")
    print("\nRunning-config unlocked!\nEND")
```

* When executing the script we can see while the change is being made the `running` datastore gets locked,

```shell
DC1_LEAF1#show configuration lock
       TTY        User       Time Acquired        Location       Transaction    Reason
------------- ----------- ------------------- --------------- ----------------- ------
   NETCONF       admin         0:01:12 ago       127.0.0.1                 -         -

DC1_LEAF1#
DC1_LEAF1#configure terminal
DC1_LEAF1(config)#interface ethernet 1
% Unable to run this command (configuration is locked by another session)
```

* After the script completes we can see the interface description added successfully,

```shell
DC1_LEAF1#show running-config interfaces ethernet 1
interface Ethernet1
   description P2P_LINK_TO_DC1_SPINE1_Ethernet1
```

### Modifying candidate config with lock and commit

* Here, we will use the `edit-config` operation with the `candidate` configuration datastore. It uses a `lock` & `commit` operation.

```python
#Modify candidate config with lock and commit
def candidateLockCommit(eos):
    config_intf = """
    <config>
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface>
                <name>
                    Ethernet2
                </name>
                <config>
                    <description>
                        P2P_LINK_TO_CLIENT1_Ethernet1
                    </description>
                </config>
            </interface>
        </interfaces>
    </config>
    """
    print("\n{}\n".format(config_intf))
    #Apply the configuration on the device
    #eos.discard_changes()
    with eos.locked("candidate"):
        print(eos.edit_config(target="candidate", config=config_intf, default_operation="merge"))
        print(eos.commit())
```

* After the script execution completes we can see interface description is configured

```shell
DC1_LEAF1#show running-config interfaces ethernet 2
interface Ethernet2
   description P2P_LINK_TO_CLIENT1_Ethernet1
```

### Copy running configuration to startup configuration

* Here, we will use the `copy_config` operation to copy the running-config to startup-config

```python
# Copy running-config to startup-config
def copyConfig(eos):
    eos.copy_config(target="startup", source="running")
    print("\nCopied running-config to startup-config!\n")
```

* Before we execute the script we can see the difference between the running-config and the startup-config

```shell
DC1_LEAF1#show running-config diffs
--- flash:/startup-config
+++ system:/running-config
@@ -1,4 +1,4 @@
-! device: leaf1 (cEOSLab, EOS-4.30.1F-32308478.4301F (engineering build))
+! device: DC1-LEAF1 (cEOSLab, EOS-4.30.1F-32308478.4301F (engineering build))
 !
 no aaa root
 !
@@ -8,7 +8,8 @@
 !
 service routing protocols model multi-agent
 !
-hostname leaf1
+hostname DC1_LEAF1
+ip name-server vrf default 8.8.8.8
 !
 spanning-tree mode mstp
 !
@@ -39,8 +40,10 @@
       certificate eAPI.crt key eAPI.key
 !
 interface Ethernet1
+   description P2P_LINK_TO_DC1_SPINE1_Ethernet1
 !
 interface Ethernet2
+   description P2P_LINK_TO_CLIENT1_Ethernet1
 !
 interface Management1
    description oob_management
```

* After the script has executed we can see the startup-config has been synced with running-config

```shell
DC1_LEAF1#show running-config diffs
DC1_LEAF1#
```

### Modifying candidate config with lock and discard

* Here, we will use the `edit-config` operation with the `candidate` configuration datastore. It uses `lock` operation and `discard_change` operation to revert the candidate configuration to the current running configuration (instead of committing the candidate configuration)

```python
# Candidate config discard
def candidateLockDiscard(eos):
    config_sys = """
    <config>
        <system xmlns="http://openconfig.net/yang/system">
            <config>
                <domain-name>
                    blr.aristanetworks.com
                </domain-name>
            </config>
            <ntp>
                <servers>
                    <server>
                        <address>time.google.com</address>
                        <config>
                            <address>time.google.com</address>
                            <iburst>true</iburst>
                            <prefer>true</prefer>
                        </config>
                    </server>
                </servers>
            </ntp>
        </system>
    </config>
    """
    config = """
    <system>
        <config>
            <domain-name>
            </domain-name>
        </config>
        <ntp>
            <servers>
                <server>
                    <address>time.google.com</address>
                    <config></config>
                </server>
            </servers>
        </ntp>
    </system>
    """
    print("\n{}\n".format(config_sys))
    #Apply the configuration on the device
    #eos.discard_changes()
    with eos.locked("candidate"):
        print(eos.edit_config(target="candidate", config=config_sys, default_operation="merge"))
        print("\nPulling candidate configuration\n")
        reply = eos.get_config(source="candidate", filter=("subtree", config))
        print(xml.dom.minidom.parseString(str(reply)).toprettyxml())
        input("\nCandidate config modified! Press any key to continue...")
        print(eos.discard_changes())
    print("\nCandidate config discarded!\n")
```

* Executing the script we can see the configuration is applied in the candidate configuration but not applied on the switch.

```xml
$ python3 config_demo.py

<--snipped-->

Pulling candidate configuration

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:fc5cb1ef-7c57-401c-821e-5dce5ac484b2">
	<data xmlns:netconf="http://arista.com/yang/rpc/netconf" netconf:time-modified="2024-02-01T10:15:47.943749974Z">
		<system xmlns="http://openconfig.net/yang/system">
			<config>
				<domain-name>blr.aristanetworks.com</domain-name>
			</config>
			<ntp>
				<servers>
					<server>
						<address>time.google.com</address>
						<config>
							<address>time.google.com</address>
							<iburst>true</iburst>
							<prefer>true</prefer>
						</config>
					</server>
				</servers>
			</ntp>
		</system>
	</data>
</rpc-reply>


Candidate config modified! Press any key to continue...
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:73602dbd-a2e8-4091-8ca0-5ea015b79b3a"><ok></ok></rpc-reply>

Candidate config discarded!
```

Switch:
```shell
DC1_LEAF1#show running-config section ntp
DC1_LEAF1#
```
