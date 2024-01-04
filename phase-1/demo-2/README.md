# Demo-2

## Overview

In this demo, we will take a look at rendering and configuring the hostnames of the Arista cEOS-Lab nodes using `pyangbind` and gNMI.

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

* Start the `ceos-lab` lab

```shell
cd openconfig-labs/phase-1/ceos-lab

sudo containerlab deploy -t topology.yml
```

* Navigate to the `demo-2` directory

```shell
cd openconfig-labs/phase-1/demo-2
```

* Use Pyangbind to generate a Python module from a YANG module

```shell
pyang --plugindir $(/usr/bin/env python3 -c 'import pyangbind; import os; print ("{}/plugin".format(os.path.dirname(pyangbind.__file__)))') -f pybind -p ../yang_modules/ -o ./oc_system.py ../yang_modules/openconfig-system.yang
```

* The above command will generate the Python module `oc_system.py` from the `openconfig-system.yang` file. Run this command to verify the file.

```shell
ls oc_system.py
```

* Next, we will use this Python module to generate the JSON file

```python
$ cat hostname_demo.py

#!/usr/bin/python3

from oc_system import openconfig_system
import pyangbind.lib.pybindJSON as pybindJSON
from pprint import pprint as pp

HOSTNAME = 'DC1_SPINE1'

oc_sys = openconfig_system()

oc_sys.system.config.hostname = HOSTNAME

pp(pybindJSON.dumps(oc_sys))

with open("./{}_hostname.json".format(HOSTNAME), "w") as fobj:
    fobj.write(pybindJSON.dumps(oc_sys, mode="ietf"))

fobj.close()
```

* Execute the file and we can now see the JSON file is generated.

```shell
$ python3 hostname_demo.py
('{\n'
 '    "system": {\n'
 '        "config": {\n'
 '            "hostname": "DC1_SPINE1"\n'
 '        }\n'
 '    }\n'
 '}')

---

$ cat DC1_SPINE1_hostname.json | jq
{
  "openconfig-system:system": {
    "config": {
      "hostname": "DC1_SPINE1"
    }
  }
}
```

* Using gNMIc we will configure the hostname

> Before

```shell
gnmic -a 172.100.100.2:6030 -u admin -p admin --insecure --gzip get --path '/system/state/hostname'

[
  {
    "source": "172.100.100.2:6030",
    "timestamp": 1704283677051281436,
    "time": "2024-01-03T17:37:57.051281436+05:30",
    "updates": [
      {
        "Path": "system/state/hostname",
        "values": {
          "system/state/hostname": "spine1"
        }
      }
    ]
  }
]
```

> Configuration

```shell
gnmic -a 172.100.100.2:6030 -u admin -p admin --insecure --gzip set --update-path '/' --update-file DC1_SPINE1_hostname.json

{
  "source": "172.100.100.2:6030",
  "timestamp": 1704283724018948761,
  "time": "2024-01-03T17:38:44.018948761+05:30",
  "results": [
    {
      "operation": "UPDATE"
    }
  ]
}
```

> After

```shell
gnmic -a 172.100.100.2:6030 -u admin -p admin --insecure --gzip get --path '/system/state/hostname'
[
  {
    "source": "172.100.100.2:6030",
    "timestamp": 1704283746770411595,
    "time": "2024-01-03T17:39:06.770411595+05:30",
    "updates": [
      {
        "Path": "system/state/hostname",
        "values": {
          "system/state/hostname": "DC1_SPINE1"
        }
      }
    ]
  }
]
```
