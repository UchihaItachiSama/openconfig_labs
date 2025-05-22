# yang-demo

- [yang-demo](#yang-demo)
  - [Requirements](#requirements)
  - [YANG tree for better visualization](#yang-tree-for-better-visualization)
  - [Converting YANG module to XML syntax YIN](#converting-yang-module-to-xml-syntax-yin)
  - [Augmentation \& Deviation](#augmentation--deviation)

In this demo we will take a look at:

- YANG tree using `pyang`
- Convert YANG modules into equivalent YIN module (XML)
- Tree/XPATH representation of YANG models for quick visualization

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
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
module: openconfig-interfaces
  +--rw interfaces
     +--rw interface* [name]
        +--rw name                  -> ../config/name
        +--rw config
        |  +--rw name?            string
        |  +--rw type             identityref
        |  +--rw mtu?             uint16
        |  +--rw loopback-mode?   oc-opt-types:loopback-mode-type
        |  +--rw description?     string
        |  +--rw enabled?         boolean
        +--ro state
        |  +--ro name?            string
        |  +--ro type             identityref
        |  +--ro mtu?             uint16
        |  +--ro loopback-mode?   oc-opt-types:loopback-mode-type
        |  +--ro description?     string
        |  +--ro enabled?         boolean
        |  +--ro ifindex?         uint32
        |  +--ro admin-status     enumeration
        |  +--ro oper-status      enumeration
        |  +--ro last-change?     oc-types:timeticks64
        |  +--ro logical?         boolean
        |  +--ro management?      boolean
        |  +--ro cpu?             boolean
        |  +--ro counters
        |     +--ro in-octets?               oc-yang:counter64
        |     +--ro in-pkts?                 oc-yang:counter64
        |     +--ro in-unicast-pkts?         oc-yang:counter64
        |     +--ro in-broadcast-pkts?       oc-yang:counter64
        |     +--ro in-multicast-pkts?       oc-yang:counter64
        |     +--ro in-errors?               oc-yang:counter64
        |     +--ro in-discards?             oc-yang:counter64
        |     +--ro out-octets?              oc-yang:counter64
        |     +--ro out-pkts?                oc-yang:counter64
        |     +--ro out-unicast-pkts?        oc-yang:counter64
        |     +--ro out-broadcast-pkts?      oc-yang:counter64
        |     +--ro out-multicast-pkts?      oc-yang:counter64
        |     +--ro out-discards?            oc-yang:counter64
        |     +--ro out-errors?              oc-yang:counter64
        |     +--ro last-clear?              oc-types:timeticks64
        |     +--ro in-unknown-protos?       oc-yang:counter64
        |     +--ro in-fcs-errors?           oc-yang:counter64
        |     x--ro carrier-transitions?     oc-yang:counter64
        |     +--ro interface-transitions?   oc-yang:counter64
        |     +--ro link-transitions?        oc-yang:counter64
        |     +--ro resets?                  oc-yang:counter64
        +--rw hold-time
        |  +--rw config
        |  |  +--rw up?     uint32
        |  |  +--rw down?   uint32
        |  +--ro state
        |     +--ro up?     uint32
        |     +--ro down?   uint32
        +--rw penalty-based-aied
        |  +--rw config
        |  |  +--rw max-suppress-time?    uint32
        |  |  +--rw decay-half-life?      uint32
        |  |  +--rw suppress-threshold?   uint32
        |  |  +--rw reuse-threshold?      uint32
        |  |  +--rw flap-penalty?         uint32
        |  +--ro state
        |     +--ro max-suppress-time?    uint32
        |     +--ro decay-half-life?      uint32
        |     +--ro suppress-threshold?   uint32
        |     +--ro reuse-threshold?      uint32
        |     +--ro flap-penalty?         uint32
        +--rw subinterfaces
           +--rw subinterface* [index]
              +--rw index     -> ../config/index
              +--rw config
              |  +--rw index?         uint32
              |  +--rw description?   string
              |  +--rw enabled?       boolean
              +--ro state
                 +--ro index?          uint32
                 +--ro description?    string
                 +--ro enabled?        boolean
                 +--ro name?           string
                 +--ro ifindex?        uint32
                 +--ro admin-status    enumeration
                 +--ro oper-status     enumeration
                 +--ro last-change?    oc-types:timeticks64
                 +--ro logical?        boolean
                 +--ro management?     boolean
                 +--ro cpu?            boolean
                 +--ro counters
                    +--ro in-octets?             oc-yang:counter64
                    +--ro in-pkts?               oc-yang:counter64
                    +--ro in-unicast-pkts?       oc-yang:counter64
                    +--ro in-broadcast-pkts?     oc-yang:counter64
                    +--ro in-multicast-pkts?     oc-yang:counter64
                    +--ro in-errors?             oc-yang:counter64
                    +--ro in-discards?           oc-yang:counter64
                    +--ro out-octets?            oc-yang:counter64
                    +--ro out-pkts?              oc-yang:counter64
                    +--ro out-unicast-pkts?      oc-yang:counter64
                    +--ro out-broadcast-pkts?    oc-yang:counter64
                    +--ro out-multicast-pkts?    oc-yang:counter64
                    +--ro out-discards?          oc-yang:counter64
                    +--ro out-errors?            oc-yang:counter64
                    +--ro last-clear?            oc-types:timeticks64
                    x--ro in-unknown-protos?     oc-yang:counter64
                    x--ro in-fcs-errors?         oc-yang:counter64
                    x--ro carrier-transitions?   oc-yang:counter64
```

</p>
</details></br>

```shell
pyang -f flatten -p demos/public-yang demos/public-yang/openconfig-interfaces.yang --flatten-keys-in-xpath
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
xpath
/openconfig-interfaces:interfaces
/openconfig-interfaces:interfaces/interface[name]
/openconfig-interfaces:interfaces/interface[name]/config
/openconfig-interfaces:interfaces/interface[name]/config/description
/openconfig-interfaces:interfaces/interface[name]/config/enabled
/openconfig-interfaces:interfaces/interface[name]/config/loopback-mode
/openconfig-interfaces:interfaces/interface[name]/config/mtu
/openconfig-interfaces:interfaces/interface[name]/config/name
/openconfig-interfaces:interfaces/interface[name]/config/type
/openconfig-interfaces:interfaces/interface[name]/hold-time
/openconfig-interfaces:interfaces/interface[name]/hold-time/config
/openconfig-interfaces:interfaces/interface[name]/hold-time/config/down
/openconfig-interfaces:interfaces/interface[name]/hold-time/config/up
/openconfig-interfaces:interfaces/interface[name]/hold-time/state
/openconfig-interfaces:interfaces/interface[name]/hold-time/state/down
/openconfig-interfaces:interfaces/interface[name]/hold-time/state/up
/openconfig-interfaces:interfaces/interface[name]/name
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/config
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/config/decay-half-life
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/config/flap-penalty
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/config/max-suppress-time
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/config/reuse-threshold
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/config/suppress-threshold
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/state
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/state/decay-half-life
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/state/flap-penalty
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/state/max-suppress-time
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/state/reuse-threshold
/openconfig-interfaces:interfaces/interface[name]/penalty-based-aied/state/suppress-threshold
/openconfig-interfaces:interfaces/interface[name]/state
/openconfig-interfaces:interfaces/interface[name]/state/admin-status
/openconfig-interfaces:interfaces/interface[name]/state/counters
/openconfig-interfaces:interfaces/interface[name]/state/counters/carrier-transitions
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-broadcast-pkts
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-discards
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-errors
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-fcs-errors
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-multicast-pkts
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-octets
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-pkts
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-unicast-pkts
/openconfig-interfaces:interfaces/interface[name]/state/counters/in-unknown-protos
/openconfig-interfaces:interfaces/interface[name]/state/counters/interface-transitions
/openconfig-interfaces:interfaces/interface[name]/state/counters/last-clear
/openconfig-interfaces:interfaces/interface[name]/state/counters/link-transitions
/openconfig-interfaces:interfaces/interface[name]/state/counters/out-broadcast-pkts
/openconfig-interfaces:interfaces/interface[name]/state/counters/out-discards
/openconfig-interfaces:interfaces/interface[name]/state/counters/out-errors
/openconfig-interfaces:interfaces/interface[name]/state/counters/out-multicast-pkts
/openconfig-interfaces:interfaces/interface[name]/state/counters/out-octets
/openconfig-interfaces:interfaces/interface[name]/state/counters/out-pkts
/openconfig-interfaces:interfaces/interface[name]/state/counters/out-unicast-pkts
/openconfig-interfaces:interfaces/interface[name]/state/counters/resets
/openconfig-interfaces:interfaces/interface[name]/state/cpu
/openconfig-interfaces:interfaces/interface[name]/state/description
/openconfig-interfaces:interfaces/interface[name]/state/enabled
/openconfig-interfaces:interfaces/interface[name]/state/ifindex
/openconfig-interfaces:interfaces/interface[name]/state/last-change
/openconfig-interfaces:interfaces/interface[name]/state/logical
/openconfig-interfaces:interfaces/interface[name]/state/loopback-mode
/openconfig-interfaces:interfaces/interface[name]/state/management
/openconfig-interfaces:interfaces/interface[name]/state/mtu
/openconfig-interfaces:interfaces/interface[name]/state/name
/openconfig-interfaces:interfaces/interface[name]/state/oper-status
/openconfig-interfaces:interfaces/interface[name]/state/type
/openconfig-interfaces:interfaces/interface[name]/subinterfaces
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/config
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/config/description
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/config/enabled
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/config/index
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/index
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/admin-status
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/carrier-transitions
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-broadcast-pkts
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-discards
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-errors
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-fcs-errors
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-multicast-pkts
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-octets
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-pkts
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-unicast-pkts
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/in-unknown-protos
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/last-clear
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/out-broadcast-pkts
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/out-discards
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/out-errors
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/out-multicast-pkts
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/out-octets
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/out-pkts
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/counters/out-unicast-pkts
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/cpu
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/description
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/enabled
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/ifindex
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/index
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/last-change
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/logical
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/management
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/name
/openconfig-interfaces:interfaces/interface[name]/subinterfaces/subinterface[index]/state/oper-status
```

</p>
</details></br>

```shell
pyang -f tree -p demos/public-yang demos/public-yang/openconfig-interfaces.yang --tree-path=interfaces/interface/state
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
module: openconfig-interfaces
  +--rw interfaces
     +--rw interface* [name]
        +--ro state
           +--ro name?            string
           +--ro type             identityref
           +--ro mtu?             uint16
           +--ro loopback-mode?   oc-opt-types:loopback-mode-type
           +--ro description?     string
           +--ro enabled?         boolean
           +--ro ifindex?         uint32
           +--ro admin-status     enumeration
           +--ro oper-status      enumeration
           +--ro last-change?     oc-types:timeticks64
           +--ro logical?         boolean
           +--ro management?      boolean
           +--ro cpu?             boolean
           +--ro counters
              +--ro in-octets?               oc-yang:counter64
              +--ro in-pkts?                 oc-yang:counter64
              +--ro in-unicast-pkts?         oc-yang:counter64
              +--ro in-broadcast-pkts?       oc-yang:counter64
              +--ro in-multicast-pkts?       oc-yang:counter64
              +--ro in-errors?               oc-yang:counter64
              +--ro in-discards?             oc-yang:counter64
              +--ro out-octets?              oc-yang:counter64
              +--ro out-pkts?                oc-yang:counter64
              +--ro out-unicast-pkts?        oc-yang:counter64
              +--ro out-broadcast-pkts?      oc-yang:counter64
              +--ro out-multicast-pkts?      oc-yang:counter64
              +--ro out-discards?            oc-yang:counter64
              +--ro out-errors?              oc-yang:counter64
              +--ro last-clear?              oc-types:timeticks64
              +--ro in-unknown-protos?       oc-yang:counter64
              +--ro in-fcs-errors?           oc-yang:counter64
              x--ro carrier-transitions?     oc-yang:counter64
              +--ro interface-transitions?   oc-yang:counter64
              +--ro link-transitions?        oc-yang:counter64
              +--ro resets?                  oc-yang:counter64
```

</p>
</details></br>

```shell
gnmic path --file demos/public-yang/openconfig-interfaces.yang
```

<details>
<summary>Reveal Output</summary>
<p>

```json
/interfaces-state/interface[name=*]/admin-status
/interfaces-state/interface[name=*]/higher-layer-if
/interfaces-state/interface[name=*]/if-index
/interfaces-state/interface[name=*]/last-change
/interfaces-state/interface[name=*]/lower-layer-if
/interfaces-state/interface[name=*]/name
/interfaces-state/interface[name=*]/oper-status
/interfaces-state/interface[name=*]/phys-address
/interfaces-state/interface[name=*]/speed
/interfaces-state/interface[name=*]/statistics/discontinuity-time
/interfaces-state/interface[name=*]/statistics/in-broadcast-pkts
/interfaces-state/interface[name=*]/statistics/in-discards
/interfaces-state/interface[name=*]/statistics/in-errors
/interfaces-state/interface[name=*]/statistics/in-multicast-pkts
/interfaces-state/interface[name=*]/statistics/in-octets
/interfaces-state/interface[name=*]/statistics/in-unicast-pkts
/interfaces-state/interface[name=*]/statistics/in-unknown-protos
/interfaces-state/interface[name=*]/statistics/out-broadcast-pkts
/interfaces-state/interface[name=*]/statistics/out-discards
/interfaces-state/interface[name=*]/statistics/out-errors
/interfaces-state/interface[name=*]/statistics/out-multicast-pkts
/interfaces-state/interface[name=*]/statistics/out-octets
/interfaces-state/interface[name=*]/statistics/out-unicast-pkts
/interfaces-state/interface[name=*]/type
/interfaces/interface[name=*]/admin-status
/interfaces/interface[name=*]/config/description
/interfaces/interface[name=*]/config/enabled
/interfaces/interface[name=*]/config/loopback-mode
/interfaces/interface[name=*]/config/mtu
/interfaces/interface[name=*]/config/name
/interfaces/interface[name=*]/config/type
/interfaces/interface[name=*]/description
/interfaces/interface[name=*]/enabled
/interfaces/interface[name=*]/higher-layer-if
/interfaces/interface[name=*]/hold-time/config/down
/interfaces/interface[name=*]/hold-time/config/up
/interfaces/interface[name=*]/hold-time/state/down
/interfaces/interface[name=*]/hold-time/state/up
/interfaces/interface[name=*]/if-index
/interfaces/interface[name=*]/last-change
/interfaces/interface[name=*]/link-up-down-trap-enable
/interfaces/interface[name=*]/lower-layer-if
/interfaces/interface[name=*]/name
/interfaces/interface[name=*]/name
/interfaces/interface[name=*]/oper-status
/interfaces/interface[name=*]/penalty-based-aied/config/decay-half-life
/interfaces/interface[name=*]/penalty-based-aied/config/flap-penalty
/interfaces/interface[name=*]/penalty-based-aied/config/max-suppress-time
/interfaces/interface[name=*]/penalty-based-aied/config/reuse-threshold
/interfaces/interface[name=*]/penalty-based-aied/config/suppress-threshold
/interfaces/interface[name=*]/penalty-based-aied/state/decay-half-life
/interfaces/interface[name=*]/penalty-based-aied/state/flap-penalty
/interfaces/interface[name=*]/penalty-based-aied/state/max-suppress-time
/interfaces/interface[name=*]/penalty-based-aied/state/reuse-threshold
/interfaces/interface[name=*]/penalty-based-aied/state/suppress-threshold
/interfaces/interface[name=*]/phys-address
/interfaces/interface[name=*]/speed
/interfaces/interface[name=*]/state/admin-status
/interfaces/interface[name=*]/state/counters/carrier-transitions
/interfaces/interface[name=*]/state/counters/in-broadcast-pkts
/interfaces/interface[name=*]/state/counters/in-discards
/interfaces/interface[name=*]/state/counters/in-errors
/interfaces/interface[name=*]/state/counters/in-fcs-errors
/interfaces/interface[name=*]/state/counters/in-multicast-pkts
/interfaces/interface[name=*]/state/counters/in-octets
/interfaces/interface[name=*]/state/counters/in-pkts
/interfaces/interface[name=*]/state/counters/in-unicast-pkts
/interfaces/interface[name=*]/state/counters/in-unknown-protos
/interfaces/interface[name=*]/state/counters/interface-transitions
/interfaces/interface[name=*]/state/counters/last-clear
/interfaces/interface[name=*]/state/counters/link-transitions
/interfaces/interface[name=*]/state/counters/out-broadcast-pkts
/interfaces/interface[name=*]/state/counters/out-discards
/interfaces/interface[name=*]/state/counters/out-errors
/interfaces/interface[name=*]/state/counters/out-multicast-pkts
/interfaces/interface[name=*]/state/counters/out-octets
/interfaces/interface[name=*]/state/counters/out-pkts
/interfaces/interface[name=*]/state/counters/out-unicast-pkts
/interfaces/interface[name=*]/state/counters/resets
/interfaces/interface[name=*]/state/cpu
/interfaces/interface[name=*]/state/description
/interfaces/interface[name=*]/state/enabled
/interfaces/interface[name=*]/state/ifindex
/interfaces/interface[name=*]/state/last-change
/interfaces/interface[name=*]/state/logical
/interfaces/interface[name=*]/state/loopback-mode
/interfaces/interface[name=*]/state/management
/interfaces/interface[name=*]/state/mtu
/interfaces/interface[name=*]/state/name
/interfaces/interface[name=*]/state/oper-status
/interfaces/interface[name=*]/state/type
/interfaces/interface[name=*]/statistics/discontinuity-time
/interfaces/interface[name=*]/statistics/in-broadcast-pkts
/interfaces/interface[name=*]/statistics/in-discards
/interfaces/interface[name=*]/statistics/in-errors
/interfaces/interface[name=*]/statistics/in-multicast-pkts
/interfaces/interface[name=*]/statistics/in-octets
/interfaces/interface[name=*]/statistics/in-unicast-pkts
/interfaces/interface[name=*]/statistics/in-unknown-protos
/interfaces/interface[name=*]/statistics/out-broadcast-pkts
/interfaces/interface[name=*]/statistics/out-discards
/interfaces/interface[name=*]/statistics/out-errors
/interfaces/interface[name=*]/statistics/out-multicast-pkts
/interfaces/interface[name=*]/statistics/out-octets
/interfaces/interface[name=*]/statistics/out-unicast-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/config/description
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/config/enabled
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/config/index
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/index
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/admin-status
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/carrier-transitions
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-broadcast-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-discards
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-errors
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-fcs-errors
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-multicast-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-octets
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-unicast-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/in-unknown-protos
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/last-clear
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/out-broadcast-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/out-discards
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/out-errors
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/out-multicast-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/out-octets
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/out-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/counters/out-unicast-pkts
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/cpu
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/description
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/enabled
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/ifindex
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/index
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/last-change
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/logical
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/management
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/name
/interfaces/interface[name=*]/subinterfaces/subinterface[index=*]/state/oper-status
/interfaces/interface[name=*]/type
```

</p>
</details>

## Converting YANG module to XML syntax YIN

```shell
pyang -p demos/public-yang demos/public-yang/openconfig-interfaces.yang -f yin --yin-pretty-strings
```

<details>
<summary>Reveal Output</summary>
<p>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<module name="openconfig-interfaces"
        xmlns="urn:ietf:params:xml:ns:yang:yin:1"
        xmlns:oc-if="http://openconfig.net/yang/interfaces"
        xmlns:ietf-if="urn:ietf:params:xml:ns:yang:ietf-interfaces"
        xmlns:oc-yang="http://openconfig.net/yang/types/yang"
        xmlns:oc-types="http://openconfig.net/yang/openconfig-types"
        xmlns:oc-ext="http://openconfig.net/yang/openconfig-ext"
        xmlns:oc-opt-types="http://openconfig.net/yang/transport-types">
  <yang-version value="1"/>
  <namespace uri="http://openconfig.net/yang/interfaces"/>
  <prefix value="oc-if"/>
  <import module="ietf-interfaces">
    <prefix value="ietf-if"/>
  </import>
  <import module="openconfig-yang-types">
    <prefix value="oc-yang"/>
  </import>
  <import module="openconfig-types">
    <prefix value="oc-types"/>
  </import>
  <import module="openconfig-extensions">
    <prefix value="oc-ext"/>
  </import>
  <import module="openconfig-transport-types">
    <prefix value="oc-opt-types"/>
  </import>
  <organization>
    <text>
      OpenConfig working group
    </text>
  </organization>
  <contact>
    <text>
      OpenConfig working group
      netopenconfig@googlegroups.com
    </text>
  </contact>
  <description>
    <text>
      Model for managing network interfaces and subinterfaces.  This
      module also defines convenience types / groupings for other
      models to create references to interfaces:

       base-interface-ref (type) -  reference to a base interface
       interface-ref (grouping) -  container for reference to a
         interface + subinterface
       interface-ref-state (grouping) - container for read-only
         (opstate) reference to interface + subinterface

      This model reuses data items defined in the IETF YANG model for
      interfaces described by RFC 7223 with an alternate structure
      (particularly for operational state data) and with
      additional configuration items.

      Portions of this code were derived from IETF RFC 7223.
      Please reproduce this note if possible.

      IETF code is subject to the following copyright and license:
      Copyright (c) IETF Trust and the persons identified as authors of
      the code.
      All rights reserved.

      Redistribution and use in source and binary forms, with or without
      modification, is permitted pursuant to, and subject to the license
      terms contained in, the Simplified BSD License set forth in
      Section 4.c of the IETF Trust's Legal Provisions Relating
      to IETF Documents (http://trustee.ietf.org/license-info).
    </text>
  </description>
  <oc-ext:openconfig-version semver="3.8.0"/>
  <revision date="2024-12-05">
    <description>
      <text>
        Add interface-transitions and link-transitions counters
      </text>
    </description>
    <reference>
      <text>
        3.8.0
      </text>
    </reference>
  </revision>
  <revision date="2024-12-05">
    <description>
      <text>
        Description typo for unnumbered/interface-ref/config/subinterface leaf
      </text>
    </description>
    <reference>
      <text>
        3.7.2
      </text>
    </reference>
  </revision>
  <revision date="2024-04-04">
    <description>
      <text>
        Use single quotes in descriptions.
      </text>
    </description>
    <reference>
      <text>
        3.7.1
      </text>
    </reference>
  </revision>
  <revision date="2023-11-06">
    <description>
      <text>
        Clarify description for admin-status TESTING.
      </text>
    </description>
    <reference>
      <text>
        3.7.0
      </text>
    </reference>
  </revision>
  <revision date="2023-08-29">
    <description>
      <text>
        Add augment for penalty-based additive-increase, exponential-decrease link damping algorithm.
      </text>
    </description>
    <reference>
      <text>
        3.6.0
      </text>
    </reference>
  </revision>
  <revision date="2023-07-14">
    <description>
      <text>
        Move counters which apply to both interfaces and subinterfaces to
        a common grouping.  Deprecate physical counters from subinterface
      </text>
    </description>
    <reference>
      <text>
        3.5.0
      </text>
    </reference>
  </revision>
  <revision date="2023-02-06">
    <description>
      <text>
        Add further specification to interface-ref type to
        clarify that the interface and subinterface leaves
        are how an interface is referenced, regardless of
        context.
      </text>
    </description>
    <reference>
      <text>
        3.0.2
      </text>
    </reference>
  </revision>
  <revision date="2022-10-25">
    <description>
      <text>
        change loopback-mode to align with available modes
      </text>
    </description>
    <reference>
      <text>
        3.0.1
      </text>
    </reference>
  </revision>
  <revision date="2021-04-06">
    <description>
      <text>
        Add leaves for management and cpu interfaces
      </text>
    </description>
    <reference>
      <text>
        2.5.0
      </text>
    </reference>
  </revision>
  <revision date="2019-11-19">
    <description>
      <text>
        Update description of interface name.
      </text>
    </description>
    <reference>
      <text>
        2.4.3
      </text>
    </reference>
  </revision>
  <revision date="2019-07-10">
    <description>
      <text>
        Remove redundant nanosecond units statements to reflect
        universal definition of timeticks64 type.
      </text>
    </description>
    <reference>
      <text>
        2.4.2
      </text>
    </reference>
  </revision>
  <revision date="2018-11-21">
    <description>
      <text>
        Add OpenConfig module metadata extensions.
      </text>
    </description>
    <reference>
      <text>
        2.4.1
      </text>
    </reference>
  </revision>
  <revision date="2018-08-07">
    <description>
      <text>
        Add leaf to indicate whether an interface is physical or
        logical.
      </text>
    </description>
    <reference>
      <text>
        2.4.0
      </text>
    </reference>
  </revision>
  <revision date="2018-07-02">
    <description>
      <text>
        Add in-pkts and out-pkts in counters
      </text>
    </description>
    <reference>
      <text>
        2.3.2
      </text>
    </reference>
  </revision>
  <revision date="2018-04-24">
    <description>
      <text>
        Clarified behavior of last-change state leaf
      </text>
    </description>
    <reference>
      <text>
        2.3.1
      </text>
    </reference>
  </revision>
  <revision date="2018-01-05">
    <description>
      <text>
        Add logical loopback to interface.
      </text>
    </description>
    <reference>
      <text>
        2.3.0
      </text>
    </reference>
  </revision>
  <revision date="2017-12-22">
    <description>
      <text>
        Add IPv4 proxy ARP configuration.
      </text>
    </description>
    <reference>
      <text>
        2.2.0
      </text>
    </reference>
  </revision>
  <revision date="2017-12-21">
    <description>
      <text>
        Added IPv6 router advertisement configuration.
      </text>
    </description>
    <reference>
      <text>
        2.1.0
      </text>
    </reference>
  </revision>
  <revision date="2017-07-14">
    <description>
      <text>
        Added Ethernet/IP state data; Add dhcp-client;
        migrate to OpenConfig types modules; Removed or
        renamed opstate values
      </text>
    </description>
    <reference>
      <text>
        2.0.0
      </text>
    </reference>
  </revision>
  <revision date="2017-04-03">
    <description>
      <text>
        Update copyright notice.
      </text>
    </description>
    <reference>
      <text>
        1.1.1
      </text>
    </reference>
  </revision>
  <revision date="2016-12-22">
    <description>
      <text>
        Fixes to Ethernet interfaces model
      </text>
    </description>
    <reference>
      <text>
        1.1.0
      </text>
    </reference>
  </revision>
  <oc-ext:regexp-posix/>
  <oc-ext:catalog-organization org="openconfig"/>
  <oc-ext:origin origin="openconfig"/>
  <typedef name="base-interface-ref">
    <type name="leafref">
      <path value="/oc-if:interfaces/oc-if:interface/oc-if:name"/>
    </type>
    <description>
      <text>
        Reusable type for by-name reference to a base interface.
        This type may be used in cases where ability to reference
        a subinterface is not required.
      </text>
    </description>
  </typedef>
  <typedef name="interface-id">
    <type name="string"/>
    <description>
      <text>
        User-defined identifier for an interface, generally used to
        name a interface reference.  The id can be arbitrary but a
        useful convention is to use a combination of base interface
        name and subinterface index.
      </text>
    </description>
  </typedef>
  <grouping name="interface-ref-common">
    <description>
      <text>
        Reference leafrefs to interface / subinterface
      </text>
    </description>
    <leaf name="interface">
      <type name="leafref">
        <path value="/oc-if:interfaces/oc-if:interface/oc-if:name"/>
      </type>
      <description>
        <text>
          Reference to a base interface.  If a reference to a
          subinterface is required, this leaf must be specified
          to indicate the base interface.
        </text>
      </description>
    </leaf>
    <leaf name="subinterface">
      <type name="leafref">
        <path value="/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index"/>
      </type>
      <description>
        <text>
          Reference to a subinterface -- this requires the base
          interface to be specified using the interface leaf in
          this container.  If only a reference to a base interface
          is required, this leaf should not be set.
        </text>
      </description>
    </leaf>
  </grouping>
  <grouping name="interface-ref-state-container">
    <description>
      <text>
        Reusable opstate w/container for a reference to an
        interface or subinterface
      </text>
    </description>
    <container name="state">
      <config value="false"/>
      <description>
        <text>
          Operational state for interface-ref
        </text>
      </description>
      <uses name="interface-ref-common"/>
    </container>
  </grouping>
  <grouping name="interface-ref">
    <description>
      <text>
        Reusable definition for a reference to an interface or
        subinterface
      </text>
    </description>
    <container name="interface-ref">
      <description>
        <text>
          Reference to an interface or subinterface. The interface
          that is being referenced is uniquely referenced based on
          the specified interface and subinterface leaves. In contexts
          where a Layer 3 interface is to be referenced, both the
          interface and subinterface leaves must be populated, as
          Layer 3 configuration within the OpenConfig models is
          associated with a subinterface. In the case where a
          Layer 2 interface is to be referenced, only the
          interface is specified.

          The interface/subinterface leaf tuple must be used as
          the means by which the interface is specified, regardless
          of any other context information (e.g., key in a list).
        </text>
      </description>
      <container name="config">
        <description>
          <text>
            Configured reference to interface / subinterface
          </text>
        </description>
        <oc-ext:telemetry-on-change/>
        <uses name="interface-ref-common"/>
      </container>
      <uses name="interface-ref-state-container"/>
    </container>
  </grouping>
  <grouping name="interface-ref-state">
    <description>
      <text>
        Reusable opstate w/container for a reference to an
        interface or subinterface
      </text>
    </description>
    <container name="interface-ref">
      <description>
        <text>
          Reference to an interface or subinterface
        </text>
      </description>
      <uses name="interface-ref-state-container"/>
    </container>
  </grouping>
  <grouping name="base-interface-ref-state">
    <description>
      <text>
        Reusable opstate w/container for a reference to a
        base interface (no subinterface).
      </text>
    </description>
    <container name="state">
      <config value="false"/>
      <description>
        <text>
          Operational state for base interface reference
        </text>
      </description>
      <leaf name="interface">
        <type name="base-interface-ref"/>
        <description>
          <text>
            Reference to a base interface.
          </text>
        </description>
      </leaf>
    </container>
  </grouping>
  <grouping name="interface-common-config">
    <description>
      <text>
        Configuration data data nodes common to physical interfaces
        and subinterfaces
      </text>
    </description>
    <leaf name="description">
      <type name="string"/>
      <description>
        <text>
          A textual description of the interface.

          A server implementation MAY map this leaf to the ifAlias
          MIB object.  Such an implementation needs to use some
          mechanism to handle the differences in size and characters
          allowed between this leaf and ifAlias.  The definition of
          such a mechanism is outside the scope of this document.

          Since ifAlias is defined to be stored in non-volatile
          storage, the MIB implementation MUST map ifAlias to the
          value of 'description' in the persistently stored
          datastore.

          Specifically, if the device supports ':startup', when
          ifAlias is read the device MUST return the value of
          'description' in the 'startup' datastore, and when it is
          written, it MUST be written to the 'running' and 'startup'
          datastores.  Note that it is up to the implementation to

          decide whether to modify this single leaf in 'startup' or
          perform an implicit copy-config from 'running' to
          'startup'.

          If the device does not support ':startup', ifAlias MUST
          be mapped to the 'description' leaf in the 'running'
          datastore.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifAlias
        </text>
      </reference>
    </leaf>
    <leaf name="enabled">
      <type name="boolean"/>
      <default value="true"/>
      <description>
        <text>
          This leaf contains the configured, desired state of the
          interface.

          Systems that implement the IF-MIB use the value of this
          leaf in the 'running' datastore to set
          IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
          has been initialized, as described in RFC 2863.

          Changes in this leaf in the 'running' datastore are
          reflected in ifAdminStatus, but if ifAdminStatus is
          changed over SNMP, this leaf is not affected.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifAdminStatus
        </text>
      </reference>
    </leaf>
  </grouping>
  <grouping name="interface-phys-config">
    <description>
      <text>
        Configuration data for physical interfaces
      </text>
    </description>
    <leaf name="name">
      <type name="string"/>
      <description>
        <text>
          The name of the interface.

          A device MAY restrict the allowed values for this leaf,
          possibly depending on the type of the interface.
          For system-controlled interfaces, this leaf is the
          device-specific name of the interface.  The 'config false'
          list interfaces/interface[name]/state contains the currently
          existing interfaces on the device.

          If a client tries to create configuration for a
          system-controlled interface that is not present in the
          corresponding state list, the server MAY reject
          the request if the implementation does not support
          pre-provisioning of interfaces or if the name refers to
          an interface that can never exist in the system.  A
          NETCONF server MUST reply with an rpc-error with the
          error-tag 'invalid-value' in this case.

          The IETF model in RFC 7223 provides YANG features for the
          following (i.e., pre-provisioning and arbitrary-names),
          however they are omitted here:

           If the device supports pre-provisioning of interface
           configuration, the 'pre-provisioning' feature is
           advertised.

           If the device allows arbitrarily named user-controlled
           interfaces, the 'arbitrary-names' feature is advertised.

          When a configured user-controlled interface is created by
          the system, it is instantiated with the same name in the
          /interfaces/interface[name]/state list.
        </text>
      </description>
    </leaf>
    <leaf name="type">
      <type name="identityref">
        <base name="ietf-if:interface-type"/>
      </type>
      <mandatory value="true"/>
      <description>
        <text>
          The type of the interface.

          When an interface entry is created, a server MAY
          initialize the type leaf with a valid value, e.g., if it
          is possible to derive the type from the name of the
          interface.

          If a client tries to set the type of an interface to a
          value that can never be used by the system, e.g., if the
          type is not supported or if the type does not match the
          name of the interface, the server MUST reject the request.
          A NETCONF server MUST reply with an rpc-error with the
          error-tag 'invalid-value' in this case.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifType
        </text>
      </reference>
    </leaf>
    <leaf name="mtu">
      <type name="uint16"/>
      <description>
        <text>
          Set the max transmission unit size in octets
          for the physical interface.  If this is not set, the mtu is
          set to the operational default -- e.g., 1514 bytes on an
          Ethernet interface.
        </text>
      </description>
    </leaf>
    <leaf name="loopback-mode">
      <type name="oc-opt-types:loopback-mode-type"/>
      <description>
        <text>
          Sets the loopback type on the interface. Setting the
          mode to something besides NONE activates the loopback in
          the specified mode.
        </text>
      </description>
    </leaf>
    <uses name="interface-common-config"/>
  </grouping>
  <grouping name="interface-phys-holdtime-config">
    <description>
      <text>
        Configuration data for interface hold-time settings --
        applies to physical interfaces.
      </text>
    </description>
    <leaf name="up">
      <type name="uint32"/>
      <units name="milliseconds"/>
      <default value="0"/>
      <description>
        <text>
          Dampens advertisement when the interface
          transitions from down to up.  A zero value means dampening
          is turned off, i.e., immediate notification.
        </text>
      </description>
    </leaf>
    <leaf name="down">
      <type name="uint32"/>
      <units name="milliseconds"/>
      <default value="0"/>
      <description>
        <text>
          Dampens advertisement when the interface transitions from
          up to down.  A zero value means dampening is turned off,
          i.e., immediate notification.
        </text>
      </description>
    </leaf>
  </grouping>
  <grouping name="interface-phys-holdtime-state">
    <description>
      <text>
        Operational state data for interface hold-time.
      </text>
    </description>
  </grouping>
  <grouping name="interface-phys-holdtime-top">
    <description>
      <text>
        Top-level grouping for setting link transition
        dampening on physical and other types of interfaces.
      </text>
    </description>
    <container name="hold-time">
      <description>
        <text>
          Top-level container for hold-time settings to enable
          dampening advertisements of interface transitions.
        </text>
      </description>
      <container name="config">
        <description>
          <text>
            Configuration data for interface hold-time settings.
          </text>
        </description>
        <oc-ext:telemetry-on-change/>
        <uses name="interface-phys-holdtime-config"/>
      </container>
      <container name="state">
        <config value="false"/>
        <description>
          <text>
            Operational state data for interface hold-time.
          </text>
        </description>
        <uses name="interface-phys-holdtime-config"/>
        <uses name="interface-phys-holdtime-state"/>
      </container>
    </container>
  </grouping>
  <grouping name="interface-link-damping-config">
    <description>
      <text>
        Configuration data for interface link damping settings.
      </text>
    </description>
    <leaf name="max-suppress-time">
      <type name="uint32"/>
      <units name="milliseconds"/>
      <default value="0"/>
      <description>
        <text>
          Maximum time an interface can remain damped since the last link down event no matter how unstable it has been prior to this period of stability. In a damped state, the interface's state change will not be advertised.
        </text>
      </description>
    </leaf>
    <leaf name="decay-half-life">
      <type name="uint32"/>
      <units name="milliseconds"/>
      <default value="0"/>
      <description>
        <text>
          The amount of time after which an interface's penalty is decreased by half. Decay-half-time should not be more than max-suppress-time.
        </text>
      </description>
    </leaf>
    <leaf name="suppress-threshold">
      <type name="uint32"/>
      <default value="0"/>
      <description>
        <text>
          The accumulated penalty that triggers the damping of an interface. A value of 0 indicates config is disabled.
        </text>
      </description>
    </leaf>
    <leaf name="reuse-threshold">
      <type name="uint32"/>
      <default value="0"/>
      <description>
        <text>
          When the accumulated penalty decreases to this reuse threshold, the interface is not damped anymore. Interface state changes are advertised to applications. A value of 0 indicates config is disabled.
        </text>
      </description>
    </leaf>
    <leaf name="flap-penalty">
      <type name="uint32"/>
      <default value="0"/>
      <description>
        <text>
          A penalty that each down event costs. A value of 0 indicates the config is disabled.
        </text>
      </description>
    </leaf>
  </grouping>
  <grouping name="interface-link-damping-state">
    <description>
      <text>
        Operational state data for interface link damping settings.
      </text>
    </description>
  </grouping>
  <grouping name="link-damping-top">
    <description>
      <text>
        Top level grouping for link damping parameters.
      </text>
    </description>
    <container name="penalty-based-aied">
      <description>
        <text>
          Top level container to suppress UP-&gt;DOWN link events using a penalty based additive-increase, exponential-decrease algorithm.
        </text>
      </description>
      <container name="config">
        <description>
          <text>
            Configuration data for link damping settings.
          </text>
        </description>
        <uses name="interface-link-damping-config"/>
      </container>
      <container name="state">
        <config value="false"/>
        <description>
          <text>
            Operational state data for link damping settings.
          </text>
        </description>
        <uses name="interface-link-damping-config"/>
        <uses name="interface-link-damping-state"/>
      </container>
    </container>
  </grouping>
  <grouping name="interface-common-state">
    <description>
      <text>
        Operational state data (in addition to intended configuration)
        at the global level for this interface
      </text>
    </description>
    <oc-ext:operational/>
    <leaf name="ifindex">
      <type name="uint32"/>
      <description>
        <text>
          System assigned number for each interface.  Corresponds to
          ifIndex object in SNMP Interface MIB
        </text>
      </description>
      <reference>
        <text>
          RFC 2863 - The Interfaces Group MIB
        </text>
      </reference>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="admin-status">
      <type name="enumeration">
        <enum name="UP">
          <description>
            <text>
              Ready to pass packets.
            </text>
          </description>
        </enum>
        <enum name="DOWN">
          <description>
            <text>
              Not ready to pass packets and not in some test mode.
            </text>
          </description>
        </enum>
        <enum name="TESTING">
          <description>
            <text>
              The interface should be treated as if in admin-down state for
              control plane protocols.  In addition, while in TESTING state the
              device should remove the interface from aggregate interfaces.
              An interface transition to the TESTING state based on a qualification
              workflow, or internal device triggered action - such as the gNOI Link
              Qualification service
            </text>
          </description>
          <reference>
            <text>
              gNOI Link Qualification Service
              https://github.com/openconfig/gnoi/blob/main/packet_link_qualification/index.md
            </text>
          </reference>
        </enum>
      </type>
      <mandatory value="true"/>
      <description>
        <text>
          The desired state of the interface.  In RFC 7223 this leaf
          has the same read semantics as ifAdminStatus.  Here, it
          reflects the administrative state as set by enabling or
          disabling the interface.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifAdminStatus
        </text>
      </reference>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="oper-status">
      <type name="enumeration">
        <enum name="UP">
          <value value="1"/>
          <description>
            <text>
              Ready to pass packets.
            </text>
          </description>
        </enum>
        <enum name="DOWN">
          <value value="2"/>
          <description>
            <text>
              The interface does not pass any packets.
            </text>
          </description>
        </enum>
        <enum name="TESTING">
          <value value="3"/>
          <description>
            <text>
              In test mode.  No operational packets can
              be passed.
            </text>
          </description>
        </enum>
        <enum name="UNKNOWN">
          <value value="4"/>
          <description>
            <text>
              Status cannot be determined for some reason.
            </text>
          </description>
        </enum>
        <enum name="DORMANT">
          <value value="5"/>
          <description>
            <text>
              Waiting for some external event.
            </text>
          </description>
        </enum>
        <enum name="NOT_PRESENT">
          <value value="6"/>
          <description>
            <text>
              Some component (typically hardware) is missing.
            </text>
          </description>
        </enum>
        <enum name="LOWER_LAYER_DOWN">
          <value value="7"/>
          <description>
            <text>
              Down due to state of lower-layer interface(s).
            </text>
          </description>
        </enum>
      </type>
      <mandatory value="true"/>
      <description>
        <text>
          The current operational state of the interface.

          This leaf has the same semantics as ifOperStatus.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifOperStatus
        </text>
      </reference>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="last-change">
      <type name="oc-types:timeticks64"/>
      <description>
        <text>
          This timestamp indicates the absolute time of the last
          state change of the interface (e.g., up-to-down transition).
          This is different than the SNMP ifLastChange object in the
          standard interface MIB in that it is not relative to the
          system boot time (i.e,. sysUpTime).

          The value is the timestamp in nanoseconds relative to
          the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="logical">
      <type name="boolean"/>
      <description>
        <text>
          When set to true, the interface is a logical interface
          which does not have an associated physical port or
          channel on the system.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="management">
      <type name="boolean"/>
      <description>
        <text>
          When set to true, the interface is a dedicated
          management interface that is not connected to dataplane
          interfaces.  It may be used to connect the system to an
          out-of-band management network, for example.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="cpu">
      <type name="boolean"/>
      <description>
        <text>
          When set to true, the interface is for traffic
          that is handled by the system CPU, sometimes also called the
          control plane interface.  On systems that represent the CPU
          interface as an Ethernet interface, for example, this leaf
          should be used to distinguish the CPU interface from dataplane
          interfaces.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
  </grouping>
  <grouping name="interface-common-counters-state">
    <description>
      <text>
        Operational state representing interface counters and statistics
        applicable to (physical) interfaces and (logical) subinterfaces.
      </text>
    </description>
    <leaf name="in-octets">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The total number of octets received on the interface,
          including framing characters.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifHCInOctets.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="in-pkts">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The total number of packets received on the interface,
          including all unicast, multicast, broadcast and bad packets
          etc.
        </text>
      </description>
      <reference>
        <text>
          RFC 2819: Remote Network Monitoring Management Information Base.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="in-unicast-pkts">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The number of packets, delivered by this sub-layer to a
          higher (sub-)layer, that were not addressed to a
          multicast or broadcast address at this sub-layer.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifHCInUcastPkts.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="in-broadcast-pkts">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The number of packets, delivered by this sub-layer to a
          higher (sub-)layer, that were addressed to a broadcast
          address at this sub-layer.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifHCInBroadcastPkts.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="in-multicast-pkts">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The number of packets, delivered by this sub-layer to a
          higher (sub-)layer, that were addressed to a multicast
          address at this sub-layer.  For a MAC-layer protocol,
          this includes both Group and Functional addresses.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifHCInMulticastPkts.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="in-errors">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          For packet-oriented interfaces, the number of inbound
          packets that contained errors preventing them from being
          deliverable to a higher-layer protocol.  For character-
          oriented or fixed-length interfaces, the number of
          inbound transmission units that contained errors
          preventing them from being deliverable to a higher-layer
          protocol.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifInErrors.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="in-discards">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The number of inbound packets that were chosen to be
          discarded even though no errors had been detected to
          prevent their being deliverable to a higher-layer
          protocol.  One possible reason for discarding such a
          packet could be to free up buffer space.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifInDiscards.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="out-octets">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The total number of octets transmitted out of the
          interface, including framing characters.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifHCOutOctets.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="out-pkts">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The total number of packets transmitted out of the
          interface, including all unicast, multicast, broadcast,
          and bad packets etc.
        </text>
      </description>
      <reference>
        <text>
          RFC 2819: Remote Network Monitoring Management Information Base.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="out-unicast-pkts">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The total number of packets that higher-level protocols
          requested be transmitted, and that were not addressed
          to a multicast or broadcast address at this sub-layer,
          including those that were discarded or not sent.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifHCOutUcastPkts.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="out-broadcast-pkts">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The total number of packets that higher-level protocols
          requested be transmitted, and that were addressed to a
          broadcast address at this sub-layer, including those
          that were discarded or not sent.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifHCOutBroadcastPkts.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="out-multicast-pkts">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The total number of packets that higher-level protocols
          requested be transmitted, and that were addressed to a
          multicast address at this sub-layer, including those
          that were discarded or not sent.  For a MAC-layer
          protocol, this includes both Group and Functional
          addresses.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifHCOutMulticastPkts.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="out-discards">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The number of outbound packets that were chosen to be
          discarded even though no errors had been detected to
          prevent their being transmitted.  One possible reason
          for discarding such a packet could be to free up buffer
          space.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifOutDiscards.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="out-errors">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          For packet-oriented interfaces, the number of outbound
          packets that could not be transmitted because of errors.
          For character-oriented or fixed-length interfaces, the
          number of outbound transmission units that could not be
          transmitted because of errors.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifOutErrors.
          RFC 4293: Management Information Base for the
          Internet Protocol (IP).
        </text>
      </reference>
    </leaf>
    <leaf name="last-clear">
      <type name="oc-types:timeticks64"/>
      <description>
        <text>
          Timestamp of the last time the interface counters were
          cleared.

          The value is the timestamp in nanoseconds relative to
          the Unix Epoch (Jan 1, 1970 00:00:00 UTC).
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
  </grouping>
  <grouping name="interface-counters-state">
    <description>
      <text>
        Operational state representing interface counters
        and statistics.
      </text>
    </description>
    <oc-ext:operational/>
    <leaf name="in-unknown-protos">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          For packet-oriented interfaces, the number of packets
          received via the interface that were discarded because
          of an unknown or unsupported protocol.  For
          character-oriented or fixed-length interfaces that
          support protocol multiplexing, the number of
          transmission units received via the interface that were
          discarded because of an unknown or unsupported protocol.
          For any interface that does not support protocol
          multiplexing, this counter is not present.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifInUnknownProtos
        </text>
      </reference>
    </leaf>
    <leaf name="in-fcs-errors">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          Number of received packets which had errors in the
          frame check sequence (FCS), i.e., framing errors.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
    </leaf>
    <leaf name="carrier-transitions">
      <type name="oc-yang:counter64"/>
      <status value="deprecated"/>
      <description>
        <text>
          Number of times the interface state has transitioned
          between up and down since the time the device restarted
          or the last-clear time, whichever is most recent.

          Please use interface-transitions instead, which has
          similar, but more precisely specified, semantics and a
          clearer name.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="interface-transitions">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          The total number of times the interface state (oper-status)
          has either transitioned to 'UP' state from any other state, or
          from state 'UP' to any other state.  I.e., an interface flap
          from UP to DOWN back to UP increments the counter by 2.
          Transitions between any other interface states other than to
          or from 'UP' state are not included in the counter.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="link-transitions">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          This is the number of times that the underlying link state
          (e.g., at the optical receiver) has transitioned to or from
          'UP' state before any holdtime, dampening, or other processing
          has been applied that could suppress an update to the interface
          'oper-status' and corresponding interface-transitions counter.

          The counter is incremented both when the link transitions
          to 'UP' state from any other link state and also when the link
          transitions from 'UP' state to any other link state, i.e., an
          interface flap from UP to DOWN back to UP increments the
          counter by 2.

          Implementations are not required to count all transitions,
          e.g., if they are below the level of granularity monitored by
          the system, and hence may not tally with the equivalent counter
          on the remote end of the link.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <leaf name="resets">
      <type name="oc-yang:counter64"/>
      <description>
        <text>
          Number of times the interface hardware has been reset.  The
          triggers and effects of this event are hardware-specifc.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
  </grouping>
  <grouping name="subinterfaces-counters-state">
    <description>
      <text>
        Operational state representing counters unique to subinterfaces
      </text>
    </description>
    <oc-ext:operational/>
    <leaf name="in-unknown-protos">
      <type name="oc-yang:counter64"/>
      <status value="deprecated"/>
      <description>
        <text>
          For packet-oriented interfaces, the number of packets
          received via the interface that were discarded because
          of an unknown or unsupported protocol.  For
          character-oriented or fixed-length interfaces that
          support protocol multiplexing, the number of
          transmission units received via the interface that were
          discarded because of an unknown or unsupported protocol.
          For any interface that does not support protocol
          multiplexing, this counter is not present.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
      <reference>
        <text>
          RFC 2863: The Interfaces Group MIB - ifInUnknownProtos
        </text>
      </reference>
    </leaf>
    <leaf name="in-fcs-errors">
      <type name="oc-yang:counter64"/>
      <status value="deprecated"/>
      <description>
        <text>
          Number of received packets which had errors in the
          frame check sequence (FCS), i.e., framing errors.

          Discontinuities in the value of this counter can occur
          at re-initialization of the management system, and at
          other times as indicated by the value of 'last-clear'.
        </text>
      </description>
    </leaf>
    <leaf name="carrier-transitions">
      <type name="oc-yang:counter64"/>
      <status value="deprecated"/>
      <description>
        <text>
          Number of times the interface state has transitioned
          between up and down since the time the device restarted
          or the last-clear time, whichever is most recent.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
  </grouping>
  <grouping name="sub-unnumbered-config">
    <description>
      <text>
        Configuration data for unnumbered subinterfaces
      </text>
    </description>
    <leaf name="enabled">
      <type name="boolean"/>
      <default value="false"/>
      <description>
        <text>
          Indicates that the subinterface is unnumbered.  By default
          the subinterface is numbered, i.e., expected to have an
          IP address configuration.
        </text>
      </description>
    </leaf>
  </grouping>
  <grouping name="sub-unnumbered-state">
    <description>
      <text>
        Operational state data unnumbered subinterfaces
      </text>
    </description>
  </grouping>
  <grouping name="sub-unnumbered-top">
    <description>
      <text>
        Top-level grouping unnumbered subinterfaces
      </text>
    </description>
    <container name="unnumbered">
      <description>
        <text>
          Top-level container for setting unnumbered interfaces.
          Includes reference the interface that provides the
          address information
        </text>
      </description>
      <container name="config">
        <description>
          <text>
            Configuration data for unnumbered interface
          </text>
        </description>
        <oc-ext:telemetry-on-change/>
        <uses name="sub-unnumbered-config"/>
      </container>
      <container name="state">
        <config value="false"/>
        <description>
          <text>
            Operational state data for unnumbered interfaces
          </text>
        </description>
        <uses name="sub-unnumbered-config"/>
        <uses name="sub-unnumbered-state"/>
      </container>
      <uses name="oc-if:interface-ref"/>
    </container>
  </grouping>
  <grouping name="subinterfaces-config">
    <description>
      <text>
        Configuration data for subinterfaces
      </text>
    </description>
    <leaf name="index">
      <type name="uint32"/>
      <default value="0"/>
      <description>
        <text>
          The index of the subinterface, or logical interface number.
          On systems with no support for subinterfaces, or not using
          subinterfaces, this value should default to 0, i.e., the
          default subinterface.
        </text>
      </description>
    </leaf>
    <uses name="interface-common-config"/>
  </grouping>
  <grouping name="subinterfaces-state">
    <description>
      <text>
        Operational state data for subinterfaces
      </text>
    </description>
    <oc-ext:operational/>
    <leaf name="name">
      <type name="string"/>
      <description>
        <text>
          The system-assigned name for the sub-interface.  This MAY
          be a combination of the base interface name and the
          subinterface index, or some other convention used by the
          system.
        </text>
      </description>
      <oc-ext:telemetry-on-change/>
    </leaf>
    <uses name="interface-common-state"/>
    <container name="counters">
      <description>
        <text>
          A collection of interface specific statistics entitites which are
          not common to subinterfaces.
        </text>
      </description>
      <uses name="interface-common-counters-state"/>
      <uses name="subinterfaces-counters-state"/>
    </container>
  </grouping>
  <grouping name="subinterfaces-top">
    <description>
      <text>
        Subinterface data for logical interfaces associated with a
        given interface
      </text>
    </description>
    <container name="subinterfaces">
      <description>
        <text>
          Enclosing container for the list of subinterfaces associated
          with a physical interface
        </text>
      </description>
      <list name="subinterface">
        <key value="index"/>
        <description>
          <text>
            The list of subinterfaces (logical interfaces) associated
            with a physical interface
          </text>
        </description>
        <leaf name="index">
          <type name="leafref">
            <path value="../config/index"/>
          </type>
          <description>
            <text>
              The index number of the subinterface -- used to address
              the logical interface
            </text>
          </description>
        </leaf>
        <container name="config">
          <description>
            <text>
              Configurable items at the subinterface level
            </text>
          </description>
          <oc-ext:telemetry-on-change/>
          <uses name="subinterfaces-config"/>
        </container>
        <container name="state">
          <config value="false"/>
          <description>
            <text>
              Operational state data for logical interfaces
            </text>
          </description>
          <uses name="subinterfaces-config"/>
          <uses name="subinterfaces-state"/>
        </container>
      </list>
    </container>
  </grouping>
  <grouping name="interfaces-top">
    <description>
      <text>
        Top-level grouping for interface configuration and
        operational state data
      </text>
    </description>
    <container name="interfaces">
      <description>
        <text>
          Top level container for interfaces, including configuration
          and state data.
        </text>
      </description>
      <list name="interface">
        <key value="name"/>
        <description>
          <text>
            The list of named interfaces on the device.
          </text>
        </description>
        <leaf name="name">
          <type name="leafref">
            <path value="../config/name"/>
          </type>
          <description>
            <text>
              References the name of the interface
            </text>
          </description>
        </leaf>
        <container name="config">
          <description>
            <text>
              Configurable items at the global, physical interface
              level
            </text>
          </description>
          <oc-ext:telemetry-on-change/>
          <uses name="interface-phys-config"/>
        </container>
        <container name="state">
          <config value="false"/>
          <description>
            <text>
              Operational state data at the global interface level
            </text>
          </description>
          <uses name="interface-phys-config"/>
          <uses name="interface-common-state"/>
          <container name="counters">
            <description>
              <text>
                A collection of interface specific statistics entitites which are
                not common to subinterfaces.
              </text>
            </description>
            <uses name="interface-common-counters-state"/>
            <uses name="interface-counters-state"/>
          </container>
        </container>
        <uses name="interface-phys-holdtime-top">
          <when condition="./penalty-based-aied/config/suppress-threshold = 0&#10;or ./penalty-based-aied/config/reuse-threshold = 0&#10;or ./penalty-based-aied/config/flap-penalty = 0">
            <description>
              <text>
                Hold time and penalty-based-aied are two algorithms to suppress
                link transitions and must be mutually exclusive.
              </text>
            </description>
          </when>
        </uses>
        <uses name="link-damping-top"/>
        <uses name="subinterfaces-top"/>
      </list>
    </container>
  </grouping>
  <uses name="interfaces-top"/>
</module>

```

</p>
</details>

## Augmentation & Deviation

```shell
pyang -f tree -p demos/public-yang demos/public-yang/openconfig-lldp.yang --tree-path /lldp/config
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
module: openconfig-lldp
  +--rw lldp
     +--rw config
        +--rw enabled?                      boolean
        +--rw hello-timer?                  uint64
        +--rw suppress-tlv-advertisement*   identityref
        +--rw system-name?                  string
        +--rw system-description?           string
        +--rw chassis-id?                   string
        +--rw chassis-id-type?              oc-lldp-types:chassis-id-type
```

</p>
</details></br>

```shell
pyang -f tree -p demos/public-yang demos/public-yang/openconfig-lldp.yang --tree-path /lldp/config --deviation-module demos/arista-yang/EOS-4.34.0F/release/openconfig/models/lldp/arista-lldp-augments.yang
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
module: openconfig-lldp
  +--rw lldp
     +--rw config
        +--rw enabled?                                   boolean
        +--rw hello-timer?                               uint64
        +--rw suppress-tlv-advertisement*                identityref
        +--rw system-name?                               string
        +--rw system-description?                        string
        +--rw chassis-id?                                string
        +--rw chassis-id-type?                           oc-lldp-types:chassis-id-type
        +--rw arista-lldp-augments:management-address
           +--rw arista-lldp-augments:network-instance?   string
           +--rw arista-lldp-augments:transmit-mode?      transmit-mode-enum
           +--rw arista-lldp-augments:interface?          string
```

</p>
</details></br>

```shell
pyang -f tree -p demos/public-yang demos/public-yang/openconfig-lldp.yang --tree-path /lldp/config --deviation-module demos/arista-yang/EOS-4.34.0F/release/openconfig/models/lldp/arista-lldp-deviations.yang
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
module: openconfig-lldp
  +--rw lldp
     +--rw config
        +--rw enabled?                      boolean
        +--rw hello-timer?                  uint64
        +--rw suppress-tlv-advertisement*   identityref
        +--rw system-name?                  string
        +--rw system-description?           string
        +--ro chassis-id?                   string
        +--ro chassis-id-type?              oc-lldp-types:chassis-id-type
```

</p>
</details>
