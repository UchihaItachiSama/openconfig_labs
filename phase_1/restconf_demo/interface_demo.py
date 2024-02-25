#!/usr/bin/python3

import requests
from requests.auth import HTTPBasicAuth
import json
from pprint import pprint as pp

requests.packages.urllib3.disable_warnings()

headers = {
    'Accept': 'application/yang-data+json'
}

USER="admin"
PASS="admin"

def getState(ip, port):
    url = "https://{}:{}/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/state".format(ip, port)
    result = requests.get(url=url, 
                          auth=HTTPBasicAuth(username=USER, password=PASS), 
                          headers=headers, 
                          verify=False)
    print("\nResult Status Code: {}".format(result.status_code))
    print("\nResult Content:\n")
    pp(result.json())

def interfaceConfig(ip, port):
    url = "https://{}:{}/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/config".format(ip, port)
    config = {
        "openconfig-interfaces:description": "P2P_LINK_TO_DC1_SPINE1_Ethernet2"
    }
    result = requests.post(url=url,
                           auth=HTTPBasicAuth(username=USER, password=PASS),
                           headers=headers,
                           verify=False,
                           json=config)
    print("\nResult Status Code: {}".format(result.status_code))
    print("\nResult Content:\n")
    pp(result.json())

def deleteIntfConfig(ip, port):
    url = "https://{}:{}/restconf/data/openconfig-interfaces:interfaces/interface=Ethernet1/config/description".format(ip, port)
    result = requests.delete(url=url,
                             auth=HTTPBasicAuth(username=USER, password=PASS),
                             headers=headers,
                             verify=False)
    print("\nResult Status Code: {}".format(result.status_code))

def main():
    getState("172.100.100.4", "5900")
    #interfaceConfig("172.100.100.4", "5900")
    #deleteIntfConfig("172.100.100.4", "5900")

if __name__ == "__main__":
    main()
