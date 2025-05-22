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

# Copy running-config to startup-config
def copyConfig(eos):
    eos.copy_config(target="startup", source="running")
    print("\nCopied running-config to startup-config!\n")

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

def main():
    eos = manager.connect(host='172.100.100.3', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)
    hostname(eos)
    #nameServers('1.1.1.1', eos)
    #nameServers('1.0.0.1', eos)
    #replaceDNS(eos)
    #deleteDNS(eos)
    #runningConfigLock(eos)
    #candidateLockCommit(eos)
    #copyConfig(eos)
    #candidateLockDiscard(eos)
    eos.close_session()

if __name__ == '__main__':
    main()