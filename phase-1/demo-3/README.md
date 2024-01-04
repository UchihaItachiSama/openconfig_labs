# Demo-3

In this demo, we will configure the L3 interfaces on the leaf and spine switches in the `ceos-lab` lab.

## Requirements

* Install Pyang and Pyangbind

```shell
python3 -m pip install pyang
python3 -m pip install pyangbind
```

* To confirm if already installed:

```shell
python3 -m pip freeze | egrep "pyang|pyangbind"
```

* `containerlab` and `docker` installed
* Arista cEOS-Lab image installed

```shell
$ docker images | egrep "IMAGE|ceosimage"

REPOSITORY               TAG          IMAGE ID       CREATED         SIZE
ceosimage                4.30.1F      72e796e3929e   3 weeks ago     2.44GB
```

## Steps

### Using JSON and gNMIc

* Start the `ceos-lab` lab

```shell
cd openconfig-labs/phase-1/ceos-lab

sudo containerlab deploy -t topology.yml
```

* Navigate to the `demo-3` directory

```shell
cd openconfig-labs/phase-1/demo-3
```

* Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $(/usr/bin/env python3 -c 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))') -f pybind -p ../yang_modules/ -o ./oc_intf.py ../yang_modules/openconfig-interfaces.yang
```

* The above command will generate the Python module `oc_intf.py` from the `openconfig-interfaces.yang` file. Run this command to verify the file.

```shell
ls oc_intf.py
```
