# Demo-1

In this demo, we will take a look at rendering and configuring the hostnames of the Arista cEOS-Lab nodes using `pyangbind` and gNMI.

> Start the lab

```shell
sudo containerlab deploy -t topology.yml
```

> Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $(/usr/bin/env python3 -c 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))') -f pybind -p ../yang_modules/ -o ./oc_system.py ../yang_modules/openconfig-system.yang
```

The above command will generate the Python module `oc_system.py` from the `openconfig-system.yang` file. Run this command to verify

```shell
ls oc_system.py
```
