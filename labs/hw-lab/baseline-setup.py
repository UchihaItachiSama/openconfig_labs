#!/usr/bin/python3

from pprint import pprint as pp
from jsonrpclib import Server
import ssl
import time
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# Update the credentials based on your Lab Setup
USERNAME = 'admin'
PASSWORD = 'admin'

# Device List (IP/hostname)

devices = [
    's1-spine1',
    's1-spine2',
    's1-leaf1',
    's1-leaf2',
    's1-leaf3',
    's1-leaf4',
    's1-host1',
    's1-host2',
]

# Execute list of commands
def runCommands(device, cmds, format):
    switch = Server( 'https://{}:{}@{}/command-api'.format(USERNAME, PASSWORD, device))
    response = switch.runCmds('latest', cmds, format)
    return response

# Function to configure self signed certificates
def genSSLProfile():
    cfgCmds = [
        'enable',
        'security pki key generate rsa 2048 selfSigned.key',
        'security pki certificate generate self-signed selfSigned.crt key selfSigned.key generate rsa 2048 validity 30000 parameters common-name selfSigned',
    ]
    cfgCmds2 = [
        'enable',
        'configure terminal',
        'management security',
        'ssl profile self-signed',
        'cipher-list HIGH:!eNULL:!aNULL:!MD5:!ADH:!ANULL',
        'certificate selfSigned.crt key selfSigned.key',
        'end'
    ]
    showCmds = [
        "enable",
        "show management security ssl profile"
    ]
    # Run configure loop for generating cert and key file
    print("\n ########## Generating self signed key and certificate ##########\n")
    for device in devices:
        resp = runCommands(device, cfgCmds, 'json')
    
    # Run configure loop for creating the profile
    print("\n ########## Configuring SSL profile ##########\n")
    for device in devices:
        resp = runCommands(device, cfgCmds2, 'json')  
    
    # Wait for few sec for config to take effect
    print("\n ########## Waiting for few seconds ##########\n")
    time.sleep(15) 

    # Run check loop
    for device in devices:
        resp = runCommands(device, showCmds, 'text')
        print("\n ########## {} ##########\n".format(device))
        print(resp[-1]['output'])

def genTransports():
    cfgCmds = [
        'enable',
        'configure session oc-transports',
        'management api gnmi',
        'provider eos-native',
        'transport grpc oob',
        'management api netconf',
        'transport ssh oob',
        'management api restconf',
        'transport https oob',
        'ssl profile self-signed',
        'port 5900',
        'end',
        'configure session oc-transports commit'
    ]
    showCmds = [
        "enable",
        "show management api gnmi",
        "show management api netconf",
        "show management api restconf"
    ]

    # Run configure loop for setting up oc transports
    print("\n ########## Configuring OC Transports ##########\n")
    for device in devices:
        resp = runCommands(device, cfgCmds, 'json')
    
    # Wait for few sec for config to take effect
    print("\n ########## Waiting for few seconds ##########\n")
    time.sleep(15)

    # Run check loop
    for device in devices:
        resp = runCommands(device, showCmds, 'text')
        print("\n ########## {} ##########\n".format(device))
        print("\n ########## {} ##########\n".format('show management api gnmi'))
        print(resp[1]['output'])
        print("\n ########## {} ##########\n".format('show management api netconf'))
        print(resp[2]['output'])
        print("\n ########## {} ##########\n".format('show management api restconf'))
        print(resp[3]['output'])

def main():
    genSSLProfile()
    genTransports()

if __name__ == '__main__':
    main()