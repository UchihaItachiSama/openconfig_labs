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

# Get interface description
intfConfig = """
<interfaces>
    <interface>
        <name>Management1</name>
        <config>
            <description>
            </description>
        </config>
    </interface>
</interfaces>
"""

# Get username

users = """
<system>
    <aaa>
        <authentication>
            <users>
                <user>
                </user>
            </users>
        </authentication>
    </aaa>
</system>
"""

print("\n########## HOSTNAME CONFIGURATION ##########\n")
reply = eos.get_config(source="running", filter=("subtree", hostname))
print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

print("\n########## INTERFACE CONFIGURATION ##########\n")
reply = eos.get_config(source="running", filter=("subtree", intfConfig))
print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

print("\n########## USER CONFIGURATION ##########\n")
reply = eos.get_config(source="running", filter=("subtree", users))
print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

eos.close_session()