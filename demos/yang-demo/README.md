# yang-demo

In this demo we will take a look at:

- YANG tree using `pyang`
- Validating YANG modules
- Convert YANG modules into equivalent YIN module (XML)
- Tree representation of YANG models for quick visualization

## Requirements

- Clone `aristanetworks/yang` into `arista-yang`

```shell
git clone https://github.com/aristanetworks/yang.git demos/arista-yang
```

- Install `pyang` and `pyangbind` if not already installed.

```shell
python3 -m pip freeze | egrep "pyang|pyangbind"

python3 -m pip install pyang
python3 -m pip install pyangbind
```

## YANG tree for better visualization

```shell
pyang -f tree -p demos/public-yang demos/public-yang/openconfig-interfaces.yang

pyang -f flatten -p demos/public-yang demos/public-yang/openconfig-interfaces.yang --flatten-keys-in-xpath

pyang -f tree -p demos/public-yang demos/public-yang/openconfig-interfaces.yang --tree-path=interfaces/interface/state

gnmic path --file demos/public-yang/openconfig-interfaces.yang
```

## Converting YANG module to XML syntax called YIN

```shell
pyang -p demos/public-yang demos/public-yang/openconfig-interfaces.yang -f yin --yin-pretty-strings
```

## Augmentation & Deviation

```shell
pyang -f tree -p demos/public-yang demos/public-yang/openconfig-lldp.yang --tree-path /lldp/config

pyang -f tree -p demos/public-yang demos/public-yang/openconfig-lldp.yang --tree-path /lldp/config --deviation-module demos/arista-yang/EOS-4.34.0F/release/openconfig/models/lldp/arista-lldp-augments.yang

pyang -f tree -p demos/public-yang demos/public-yang/openconfig-lldp.yang --tree-path /lldp/config --deviation-module demos/arista-yang/EOS-4.34.0F/release/openconfig/models/lldp/arista-lldp-deviations.yang
```
