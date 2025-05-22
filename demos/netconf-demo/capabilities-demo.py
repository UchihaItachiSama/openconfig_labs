from ncclient import manager

eos = manager.connect(host='172.100.100.3', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

print("\n########## CLIENT CAPABILITIES ##########\n")
for item in eos.client_capabilities:
    print(item)

print("\n########## SERVER CAPABILITIES ##########\n")
for item in eos.server_capabilities:
    print(item)

eos.close_session()