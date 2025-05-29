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

# Get Interfaces states
intfStates = """
<interfaces>
    <interface>
        <name>
            Ethernet1
        </name>
        <state>
            <admin-status>
            </admin-status>
            <oper-status>
            </oper-status>
        </state>
    </interface>
    <interface>
        <name>
            Ethernet2
        </name>
        <state>
            <admin-status>
            </admin-status>
            <oper-status>
            </oper-status>
        </state>
    </interface>
</interfaces>
"""

# Get LLDP information
lldp = """
<lldp>
    <interfaces>
        <interface>
            <name>
                Ethernet1
            </name>
            <neighbors>
            </neighbors>
        </interface>
    </interfaces>
</lldp>
"""

# Get all configuration and state data
#reply = eos.get()

print("\n########## SYSTEM STATE ##########\n")
reply = eos.get(filter=("subtree", systemState))
print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

print("\n########## INTERFACES STATE ##########\n")
reply = eos.get(filter=("subtree", intfStates))
print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

print("\n########## LLDP STATE ##########\n")
reply = eos.get(filter=("subtree", lldp))
print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

eos.close_session()