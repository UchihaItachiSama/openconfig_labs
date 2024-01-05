# Demo-4

In this demo, we will configure BGP peering between the leaf and spine switches in the `ceos-lab` lab.

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

* Navigate to the `demo-4` directory

```shell
cd openconfig-labs/phase-1/demo-4
```

