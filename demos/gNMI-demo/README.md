# gNMI Demo

- [gNMI Demo](#gnmi-demo)
  - [Requirements](#requirements)
  - [Capabilities](#capabilities)
  - [Get](#get)
  - [Set](#set)
  - [Subscribe](#subscribe)
  - [Octa](#octa)
  - [Cli Origin](#cli-origin)
  - [Local gNMI Get Requests](#local-gnmi-get-requests)

In this demo we will take a look at few basic examples of `gNMI` using gnmic client.

## Requirements

Confirm gnmic is installed, else install it using steps mentioned [here](https://gnmic.openconfig.net/install/).

Start the [arista-ceos](../../labs/arista-ceos/) lab using containerlab.

## Capabilities

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip capabilities
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
gNMI version: 0.7.0
supported models:
  - openconfig-qos-types, OpenConfig working group, 0.2.1
  - openconfig-telemetry-types, OpenConfig working group, 0.4.2
  - arista-aft-augments, Arista Networks, Inc., 1.0.1
  - arista-srte-augments, Arista Networks, Inc., 1.1.1
  - arista-lldp-deviations, Arista Networks, Inc., 1.1.0
  - arista-stp-augments, Arista Networks <http://arista.com/>, 0.3.1
  - arista-qos-deviations, Arista Networks, Inc., 1.0.0
  - arista-platform-notsupported-deviations, Arista Networks, Inc., 
  - arista-cli, Arista Networks, Inc., 1.0.0
  - arista-l1-open-config-platform-model-augment, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-network-instance-l3, OpenConfig working group, 2.0.0
  - openconfig-igmp, OpenConfig working group, 0.3.1
  - arista-keychain-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-qos, OpenConfig working group, 0.11.2
  - arista-lldp-notsupported-deviations, Arista Networks, Inc., 
  - arista-system-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-igmp-types, OpenConfig working group, 0.1.1
  - arista-lldp-augments, Arista Networks, Inc., 1.0.1
  - arista-rcf-rcf-open-config, Arista Networks <http://arista.com/>, 1.0.0
  - arista-exp-eos-bgp, Arista Networks, Inc., 1.4.0
  - openconfig-if-poe, OpenConfig working group, 0.1.1
  - openconfig-defined-sets, OpenConfig working group, 1.0.0
  - arista-nat-nat, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-yang-types, OpenConfig working group, 1.0.0
  - arista-system-augments, Arista Networks, Inc., 1.7.1
  - arista-flex-algo-deviations, Arista Networks, Inc., 1.0.0
  - arista-gnoi-cert, Arista Networks, Inc., https://github.com/openconfig/gnoi
  - arista-arnet-vlan-tag, Arista Networks <http://arista.com/>, 1.0.0
  - arista-flex-algo-augments, Arista Networks, Inc., 1.0.0
  - arista-bgp-augments, Arista Networks, Inc., 2.27.0
  - openconfig-alarm-types, OpenConfig working group, 0.2.1
  - openconfig-ospf-policy, OpenConfig working group, 0.1.3
  - openconfig-platform-integrated-circuit, OpenConfig working group, 0.3.1
  - openconfig-spanning-tree-types, OpenConfig working group, 0.4.1
  - arista-relay-agent-deviations, Arista Networks <http://arista.com/>, 1.0.1
  - openconfig-platform-healthz, OpenConfig working group, 0.1.1
  - openconfig-programming-errors, OpenConfig working group, 0.1.0
  - arista-arnet-vrf-name, Arista Networks <http://arista.com/>, 0.1.0
  - openconfig-pf-srte, OpenConfig working group, 0.2.0
  - openconfig-aft-network-instance, OpenConfig working group, 0.3.1
  - arista-srte-deviations, Arista Networks, Inc., 1.1.2
  - openconfig-isis-policy, OpenConfig working group, 0.8.0
  - arista-exp-eos-vxlan, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-srte-policy, OpenConfig working group, 0.2.3
  - openconfig-vlan, OpenConfig working group, 3.2.2
  - arista-vlan-deviations, Arista Networks <http://arista.com/>, 1.0.2
  - arista-arnet-ip, Arista Networks <http://arista.com/>, 0.1.0
  - openconfig-routing-policy, OpenConfig working group, 3.5.0
  - arista-local-routing-deviations, Arista Networks, Inc., 1.0.5
  - arista-bfd-deviations, Arista Networks, Inc., 1.0.1
  - arista-arnet-rate, Arista Networks <http://arista.com/>, 0.1.0
  - openconfig-gnsi-acctz, OpenConfig Working Group, 0.4.0
  - openconfig-platform-port, OpenConfig working group, 1.0.1
  - ietf-yang-metadata, IETF NETMOD (NETCONF Data Modeling Language) Working Group, 
  - openconfig-if-sdn-ext, OpenConfig working group, 0.2.0
  - arista-rpc-netconf, Arista Networks, Inc., 
  - arista-fhrp-lib-varp-status, Arista Networks <http://arista.com/>, 1.0.0
  - arista-ospf-augments, Arista Networks, Inc., 4.2.0
  - openconfig-system-grpc, OpenConfig working group, 1.1.0
  - arista-lacp-deviations, Arista Networks, Inc., 1.1.4
  - arista-ale-counters-open-config-fap-fe-serdes-info-augment, Arista Networks <http://arista.com/>, 0.0.0
  - arista-qos-augments, Arista Networks, Inc., 0.0.4
  - openconfig-system, OpenConfig working group, 2.3.0
  - openconfig-types, OpenConfig working group, 1.0.0
  - arista-exp-eos-qos, Arista Networks <http://arista.com/>, 
  - openconfig-platform-psu, OpenConfig working group, 0.2.1
  - arista-intf-deviations, Arista Networks, Inc., 1.0.6
  - openconfig-icmpv4-types, OpenConfig working group, 0.1.0
  - openconfig-acl, OpenConfig working group, 1.3.3
  - arista-qos-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-policy-types, OpenConfig working group, 3.3.0
  - openconfig-bgp, OpenConfig working group, 9.8.0
  - openconfig-lldp, OpenConfig working group, 0.2.1
  - arista-pim-augments, Arista Networks <http://arista.com/>, 1.4.0
  - openconfig-mpls-rsvp, OpenConfig working group, 4.0.1
  - openconfig-license, OpenConfig working group, 0.2.0
  - arista-exp-eos-vxlan-config, Arista Networks <http://arista.com/>, 0.2.1
  - arista-ebra-intf-encap, Arista Networks <http://arista.com/>, 1.0.0
  - arista-rpol-augments, Arista Networks <http://arista.com/>, 1.5.1
  - arista-defined-sets-notsupported-deviations, Arista Networks, Inc., 
  - arista-spanning-tree-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-pcep, OpenConfig working group, 0.1.1
  - openconfig-aft-summary, OpenConfig working group, 0.2.0
  - ietf-netconf, IETF NETCONF (Network Configuration) Working Group, 
  - openconfig-network-instance-types, OpenConfig working group, 0.9.3
  - arista-qos-interface-queue-state-augment, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-segment-routing-types, OpenConfig working group, 0.2.0
  - arista-system-session, Arista Networks <http://arista.com/>, 0.1.0
  - arista-exp-eos-l2protocolforwarding, Arista Networks, Inc., 1.1.0
  - openconfig-vlan-types, OpenConfig working group, 3.2.0
  - openconfig-isis-lsdb-types, OpenConfig working group, 0.4.2
  - arista-interfaces-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-rib-bgp-ext, OpenConfig working group, 0.6.0
  - arista-isis-augments, Arista Networks, Inc., 1.14.0
  - arista-tunnel-tunnel-basic-types, Arista Networks <http://arista.com/>, 1.0.0
  - arista-netinst-augments, Arista Networks <http://arista.com/>, 1.3.0
  - openconfig-isis, OpenConfig working group, 1.7.0
  - openconfig-keychain, OpenConfig working group, 0.5.0
  - arista-traffic-policy, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-relay-agent, OpenConfig working group, 0.1.2
  - arista-l1-open-config-xcvr-oc-types, Arista Networks <http://arista.com/>, 1.0.0
  - arista-ale-counters-open-config-specialized-counters, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-isis-flex-algo, Arista Networks <http://arista.com/>, 0.6.1
  - openconfig-if-ethernet, OpenConfig working group, 2.14.0
  - openconfig-flexalgo, OpenConfig working group, 0.1.0
  - openconfig-procmon, OpenConfig working group, 0.4.0
  - openconfig-inet-types, OpenConfig working group, 0.7.0
  - openconfig-bgp-policy, OpenConfig working group, 8.1.0
  - gnsi-authz, Google LLC, 
  - openconfig-aaa, OpenConfig working group, 1.0.0
  - arista-pseudowire-pseudowire-status, Arista Networks <http://arista.com/>, 1.0.0
  - arista-lacp-augments, Arista Networks <http://arista.com/>, 1.1.0
  - arista-acl-spec, Arista Networks <http://arista.com/>, 0.1.0
  - arista-pfc-buffer-counters-augment, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-platform-types, OpenConfig working group, 1.9.0
  - arista-exp-eos-evpn, Arista Networks, Inc., 
  - arista-network-instance-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-if-ip, OpenConfig working group, 3.6.0
  - arista-rpol-deviations, Arista Networks, Inc., 1.10.1
  - arista-sflow-deviations, Arista Networks, Inc., 1.0.2
  - arista-mpls-augments, Arista Networks <http://arista.com/>, 1.4.3
  - arista-lacp-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-platform-fan, OpenConfig working group, 0.1.1
  - arista-qos-voq-augments, Arista Networks, Inc., 1.0.0
  - arista-ebra-octap-agg-port-config, Arista Networks <http://arista.com/>, 1.0.0
  - arista-bgp-common-augments, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-metadata, OpenConfig working group, 0.1.0
  - iana-if-type, IANA, 
  - ietf-netconf-monitoring, IETF NETCONF (Network Configuration) Working Group, 
  - arista-acl-deviations, Arista Networks, Inc., 1.1.0
  - openconfig-policy-forwarding, OpenConfig working group, 0.7.0
  - openconfig-platform-cpu, OpenConfig working group, 0.1.1
  - openconfig-system-controlplane, OpenConfig working group, 0.2.0
  - openconfig-mpls-ldp, OpenConfig working group, 3.2.1
  - openconfig-aft-types, OpenConfig Working Group, 1.3.0
  - arista-bgp-deviations, Arista Networks, Inc., 1.29.0
  - arista-macsec-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-rib-bgp, OpenConfig working group, 0.9.0
  - openconfig-macsec-types, OpenConfig working group, 0.1.0
  - arista-sand-hardware-drop-counters, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-system-logging, OpenConfig working group, 0.7.0
  - openconfig-sampling-sflow, OpenConfig working group, 1.0.0
  - openconfig-openflow-types, OpenConfig working group, 0.2.0
  - openconfig-platform-transceiver, OpenConfig working group, 0.16.0
  - openconfig-telemetry, OpenConfig working group, 0.5.1
  - openconfig-interfaces, OpenConfig working group, 3.7.2
  - arista-arnet-vlan-tpid, Arista Networks <http://arista.com/>, 1.0.0
  - arista-sampling-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-evpn, OpenConfig working group, 0.11.0
  - arista-mpls-mpls-open-config-static-augment, Arista Networks <http://arista.com/>, 3.4.0
  - openconfig-system-utilization, OpenConfig working group, 0.1.0
  - openconfig-keychain-types, OpenConfig working group, 0.3.1
  - gnsi-credentialz, Google LLC, 
  - arista-vlan-augments, Arista Networks <http://arista.com/>, 1.1.2
  - arista-acl-notsupported-deviations, Arista Networks, Inc., 
  - arista-netinst-deviations, Arista Networks, Inc., 1.4.0
  - openconfig-system-terminal, OpenConfig working group, 0.3.1
  - openconfig-ospf-types, OpenConfig working group, 0.1.3
  - gnsi-certz, Google LLC, 
  - arista-eos-types, Arista Networks <http://arista.com/>, 
  - ietf-interfaces, IETF NETMOD (Network Modeling) Working Group, 
  - openconfig-platform-software, OpenConfig working group, 0.1.1
  - openconfig-aft, OpenConfig working group, 3.0.0
  - openconfig-bfd, OpenConfig working group, 0.4.0
  - openconfig-alarms, OpenConfig working group, 0.3.2
  - openconfig-packet-match, OpenConfig working group, 2.1.0
  - openconfig-rib-bgp-types, OpenConfig working group, 0.5.0
  - openconfig-platform-pipeline-counters, OpenConfig working group, 0.5.1
  - arista-ale-counters-open-config-control-plane-traffic-counters, Arista Networks <http://arista.com/>, 1.0.0
  - arista-platform-augments, Arista Networks <http://arista.com/>, 1.1.0
  - arista-ale-counters-open-config-hardware-drop-counters, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-evpn-types, OpenConfig working group, 0.2.0
  - ietf-inet-types, IETF NETMOD (NETCONF Data Modeling Language) Working Group, 
  - arista-telemetry-augments, Arista Networks, Inc., 1.0.0
  - arista-mirroring-mirroring-open-config, Arista Networks <http://arista.com/>, 1.0.0
  - arista-mirroring-tap-agg-common, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-openflow, OpenConfig working group, 0.1.2
  - openconfig-platform-controller-card, OpenConfig working group, 0.2.0
  - arista-sand-control-plane-traffic-counters, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-lacp, OpenConfig working group, 2.1.0
  - arista-isis-deviations, Arista Networks, Inc., 1.13.0
  - openconfig-network-instance, OpenConfig working group, 4.5.0
  - openconfig-hercules-qos, OpenConfig Hercules Working Group, 0.1.0
  - openconfig-transport-types, OpenConfig working group, 1.1.0
  - openconfig-packet-match-types, OpenConfig working group, 1.3.3
  - arista-fhrp-fhrp-config, Arista Networks <http://arista.com/>, 1.0.0
  - arista-exp-eos-qos-config, Arista Networks <http://arista.com/>, 0.2.0
  - arista-terminal-device-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-platform, OpenConfig working group, 0.31.0
  - arista-pim-deviations, Arista Networks, Inc., 1.2.0
  - openconfig-sampling, OpenConfig working group, 0.1.0
  - arista-interfaces-rates, Arista Networks <http://arista.com/>, 0.1.0
  - arista-macsec-deviations, Arista Networks, Inc., 1.0.0
  - arista-connectivity-monitor-types-connectivity-monitor-types, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-segment-routing, OpenConfig working group, 0.4.1
  - openconfig-network-instance-static, OpenConfig working group, 0.1.0
  - arista-mpls-deviations, Arista Networks, Inc., 1.0.3
  - arista-nat-nat-dynamic, Arista Networks <http://arista.com/>, 0.1.0
  - arista-exp-eos-qos-acl-config, Arista Networks <http://arista.com/>, 
  - arista-bfd-notsupported-deviations, Arista Networks, Inc., 
  - openconfig-ospfv2, OpenConfig working group, 0.5.2
  - openconfig-mpls, OpenConfig working group, 3.6.0
  - arista-exp-eos-varp-intf, Arista Networks <http://arista.com/>, 
  - openconfig-messages, OpenConfig working group, 0.1.0
  - openconfig-hercules-interfaces, OpenConfig Hercules Working Group, 0.2.0
  - openconfig-hercules-platform, OpenConfig Hercules Working Group, 0.2.0
  - arista-telemetry-notsupported-deviations, Arista Networks, Inc., 
  - arista-intf-intf, Arista Networks <http://arista.com/>, 0.1.0
  - openconfig-local-routing, OpenConfig working group, 2.1.0
  - openconfig-platform-linecard, OpenConfig working group, 1.2.0
  - arista-stp-deviations, Arista Networks, Inc., 1.0.0
  - openconfig-aaa-types, OpenConfig working group, 0.4.1
  - arista-system-deviations, Arista Networks, Inc., 1.4.0
  - openconfig-if-tunnel, OpenConfig working group, 0.1.1
  - arista-sflow-augments, Arista Networks, Inc., 1.1.0
  - arista-exp-eos-multicast, Arista Networks <http://arista.com/>, 0.0.1
  - openconfig-p4rt, OpenConfig Working Group, 1.0.0
  - openconfig-macsec, OpenConfig working group, 1.2.0
  - openconfig-spanning-tree, OpenConfig working group, 0.3.1
  - openconfig-isis-types, OpenConfig working group, 0.6.0
  - arista-routing-policy-notsupported-deviations, Arista Networks, Inc., 
  - ietf-yang-types, IETF NETMOD (NETCONF Data Modeling Language) Working Group, 
  - arista-exp-eos, Arista Networks <http://arista.com/>, 
  - openconfig-icmpv6-types, OpenConfig working group, 0.1.1
  - arista-ospf-deviations, Arista Networks, Inc., 4.2.0
  - arista-bfd-augments, Arista Networks <http://arista.com/>, 1.1.0
  - arista-segmentation.v1, Arista Networks, 1.0.0
  - openconfig-pim, OpenConfig working group, 0.4.4
  - arista-arnet-conn-tuple, Arista Networks <http://arista.com/>, 0.1.0
  - openconfig-gnsi, OpenConfig Working Group, 0.1.0
  - arista-l1-open-config-phy-model, Arista Networks <http://arista.com/>, 1.0.0
  - openconfig-terminal-device, OpenConfig working group, 1.9.2
  - openconfig-if-aggregate, OpenConfig working group, 2.4.4
  - arista-ale-counters-open-config-interrupt-counters, Arista Networks <http://arista.com/>, 1.0.0
  - arista-l1-open-config-optical-channel-model-augment, Arista Networks <http://arista.com/>, 1.0.0
  - vlan-translation, Arista Networks, 1.0.2
  - arista-macsec-macsec-open-config-state-augment, Arista Networks <http://arista.com/>, 1.0.0
  - arista-ntp-augments, Arista Networks, Inc., 2.0.0
  - openconfig-extensions, OpenConfig working group, 0.6.0
  - arista-exp-eos-igmpsnooping, Arista Networks <http://arista.com/>, 
  - openconfig-mpls-types, OpenConfig working group, 3.5.0
  - openconfig-platform-fabric, OpenConfig working group, 0.1.0
  - openconfig-bgp-types, OpenConfig working group, 6.1.0
  - arista-openflow-deviations, Arista Networks, Inc., 1.1.1
  - arista-exp-eos-mlag, Arista Networks <http://arista.com/>, 1.0.2
  - openconfig-pim-types, OpenConfig working group, 0.1.2
  - arista-classification-controller-field-set-open-config, Arista Networks <http://arista.com/>, 1.0.0
  - arista-intf-augments, Arista Networks <http://arista.com/>, 1.7.5
  - openconfig-lldp-types, OpenConfig working group, 0.1.1
  - openconfig-mpls-sr, OpenConfig working group, 3.0.1
supported encodings:
  - JSON
  - JSON_IETF
  - ASCII
```

</p>
</details>

## Get

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip get --path 'interfaces/interface[name=Management1]/state' | jq
```

<details>
<summary>Reveal Output</summary>
<p>

```json
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747922758235949800,
    "time": "2025-05-22T14:05:58.235949754Z",
    "updates": [
      {
        "Path": "interfaces/interface[name=Management1]/state",
        "values": {
          "interfaces/interface/state": {
            "arista-intf-augments:inactive": false,
            "openconfig-interfaces:admin-status": "UP",
            "openconfig-interfaces:counters": {
              "carrier-transitions": "3",
              "in-broadcast-pkts": "0",
              "in-discards": "0",
              "in-errors": "0",
              "in-fcs-errors": "0",
              "in-multicast-pkts": "0",
              "in-octets": "21581",
              "in-pkts": "176",
              "in-unicast-pkts": "176",
              "out-broadcast-pkts": "0",
              "out-discards": "0",
              "out-errors": "0",
              "out-multicast-pkts": "0",
              "out-octets": "5268",
              "out-pkts": "44",
              "out-unicast-pkts": "44"
            },
            "openconfig-interfaces:description": "oob_management",
            "openconfig-interfaces:ifindex": 999001,
            "openconfig-interfaces:last-change": "1747922622522420883",
            "openconfig-interfaces:management": true,
            "openconfig-interfaces:mtu": 0,
            "openconfig-interfaces:name": "Management1",
            "openconfig-interfaces:oper-status": "UP",
            "openconfig-interfaces:type": "iana-if-type:ethernetCsmacd"
          }
        }
      }
    ]
  }
```

</p>
</details></br>

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip get --path 'interfaces/interface[name=Management1]/state/oper-status' \
                                                                        --path '/system/state/software-version' | jq
```

<details>
<summary>Reveal Output</summary>
<p>

```json
[
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747922949734307800,
    "time": "2025-05-22T14:09:09.734307968Z",
    "updates": [
      {
        "Path": "interfaces/interface[name=Management1]/state/oper-status",
        "values": {
          "interfaces/interface/state/oper-status": "UP"
        }
      }
    ]
  },
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747922949734307800,
    "time": "2025-05-22T14:09:09.734307968Z",
    "updates": [
      {
        "Path": "system/state/software-version",
        "values": {
          "system/state/software-version": "4.34.1F-41757195 (engineering build)"
        }
      }
    ]
  }
]
```

</p>
</details>

## Set

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip set --update-path 'interfaces/interface[name=Ethernet2]/config/description' --update-value 'P2P_LINK_TO_LEAF2'
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "source": "clab-arlab-spine1:6030",
  "timestamp": 1747924358261510425,
  "time": "2025-05-22T14:32:38.261510425Z",
  "results": [
    {
      "operation": "UPDATE",
      "path": "interfaces/interface[name=Ethernet2]/config/description"
    }
  ]
}
```

</p>
</details></br>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
spine1#show running-config interfaces Ethernet 2
interface Ethernet2
   description P2P_LINK_TO_LEAF2

spine1#show interfaces description 
Interface                      Status         Protocol           Description
Et1                            up             up                 
Et2                            up             up                 P2P_LINK_TO_LEAF2
Ma1                            up             up                 oob_management

--- aaa accounting logs ---

2025 May 22 14:32:38 admin    GNMI        172.100.100.1:56384 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 14:32:38 admin    GNMI        172.100.100.1:56384 stop   service=shell priv-lvl=15 cmd=configure session session39809301962348
2025 May 22 14:32:38 admin    GNMI        172.100.100.1:56384 stop   service=shell priv-lvl=15 cmd=interface Ethernet2
2025 May 22 14:32:39 admin    GNMI        172.100.100.1:56384 stop   service=shell priv-lvl=15 cmd=description P2P_LINK_TO_LEAF2
2025 May 22 14:32:39 admin    GNMI        172.100.100.1:56384 stop   service=shell priv-lvl=15 cmd=exit
2025 May 22 14:32:39 admin    GNMI        172.100.100.1:56384 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 14:32:39 admin    GNMI        172.100.100.1:56384 stop   service=shell priv-lvl=15 cmd=configure session session39809301962348 commit
```

</p>
</details></br>

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip set --update-path 'interfaces/interface[name=Ethernet2]/subinterfaces/subinterface[index=0]/ipv4' --update-file demos/gNMI-demo/intf-ip.json
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "source": "clab-arlab-spine1:6030",
  "timestamp": 1747926246807411633,
  "time": "2025-05-22T15:04:06.807411633Z",
  "results": [
    {
      "operation": "UPDATE",
      "path": "interfaces/interface[name=Ethernet2]/subinterfaces/subinterface[index=0]/ipv4"
    }
  ]
}
```

</p>
</details></br>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
spine1#show running-config interfaces Ethernet 2
interface Ethernet2
   ip address 172.31.255.3/31

spine1#show ip int brief 
                                                                                Address
Interface         IP Address             Status       Protocol           MTU    Owner  
----------------- ---------------------- ------------ -------------- ---------- -------
Management1       172.100.100.2/24       up           up                1500           

--- aaa accounting logs ---

2025 May 22 15:04:07 admin    GNMI        172.100.100.1:62878 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 15:04:07 admin    GNMI        172.100.100.1:62878 stop   service=shell priv-lvl=15 cmd=configure session session41697857817877
2025 May 22 15:04:07 admin    GNMI        172.100.100.1:62878 stop   service=shell priv-lvl=15 cmd=interface Ethernet2
2025 May 22 15:04:07 admin    GNMI        172.100.100.1:62878 stop   service=shell priv-lvl=15 cmd=no switchport
2025 May 22 15:04:07 admin    GNMI        172.100.100.1:62878 stop   service=shell priv-lvl=15 cmd=ip address 172.31.255.2/31
2025 May 22 15:04:07 admin    GNMI        172.100.100.1:62878 stop   service=shell priv-lvl=15 cmd=exit
2025 May 22 15:04:07 admin    GNMI        172.100.100.1:62878 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 15:04:07 admin    GNMI        172.100.100.1:62878 stop   service=shell priv-lvl=15 cmd=configure session session41697857817877 commit
```

</p>
</details>

## Subscribe

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip subscribe --mode STREAM --stream-mode ON_CHANGE --path '/interfaces/interface[name=Management1]/state/counters'
```

<details>
<summary>Reveal Output</summary>
<p>

```json
{
  "source": "clab-arlab-spine1:6030",
  "subscription-name": "default-1747924007",
  "timestamp": 1747924007615237721,
  "time": "2025-05-22T14:26:47.615237721Z",
  "prefix": "interfaces/interface[name=Management1]/state/counters",
  "updates": [
    {
      "Path": "in-octets",
      "values": {
        "in-octets": 98093
      }
    },
    {
      "Path": "in-pkts",
      "values": {
        "in-pkts": 658
      }
    },
    {
      "Path": "in-unicast-pkts",
      "values": {
        "in-unicast-pkts": 658
      }
    }
  ]
}
{
  "source": "clab-arlab-spine1:6030",
  "subscription-name": "default-1747924007",
  "timestamp": 1747923993577125465,
  "time": "2025-05-22T14:26:33.577125465Z",
  "prefix": "interfaces/interface[name=Management1]/state/counters",
  "updates": [
    {
      "Path": "out-octets",
      "values": {
        "out-octets": 42001
      }
    },
    {
      "Path": "out-pkts",
      "values": {
        "out-pkts": 284
      }
    },
    {
      "Path": "out-unicast-pkts",
      "values": {
        "out-unicast-pkts": 284
      }
    }
  ]
}
{
  "source": "clab-arlab-spine1:6030",
  "subscription-name": "default-1747924007",
  "timestamp": 1747922632401323501,
  "time": "2025-05-22T14:03:52.401323501Z",
  "updates": [
    {
      "Path": "interfaces/interface[name=Management1]/state/counters/carrier-transitions",
      "values": {
        "interfaces/interface/state/counters/carrier-transitions": 3
      }
    }
  ]
}
{
  "source": "clab-arlab-spine1:6030",
  "subscription-name": "default-1747924007",
  "timestamp": 1747922632819332043,
  "time": "2025-05-22T14:03:52.819332043Z",
  "prefix": "interfaces/interface[name=Management1]/state/counters",
  "updates": [
    {
      "Path": "in-broadcast-pkts",
      "values": {
        "in-broadcast-pkts": 0
      }
    },
    {
      "Path": "in-discards",
      "values": {
        "in-discards": 0
      }
    },
    {
      "Path": "in-errors",
      "values": {
        "in-errors": 0
      }
    },
    {
      "Path": "in-fcs-errors",
      "values": {
        "in-fcs-errors": 0
      }
    },
    {
      "Path": "in-multicast-pkts",
      "values": {
        "in-multicast-pkts": 0
      }
    },
    {
      "Path": "out-broadcast-pkts",
      "values": {
        "out-broadcast-pkts": 0
      }
    },
    {
      "Path": "out-discards",
      "values": {
        "out-discards": 0
      }
    },
    {
      "Path": "out-errors",
      "values": {
        "out-errors": 0
      }
    },
    {
      "Path": "out-multicast-pkts",
      "values": {
        "out-multicast-pkts": 0
      }
    }
  ]
}
```

</p>
</details>

## Octa

To subscribe to EOS native paths (Sysdb, Smash etc) you need to enable Octa.

```shell
management api gnmi
   transport grpc oob
   provider eos-native   <--- add this config line under gnmi config mode
```

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip get --path "eos_native:/Smash/arp/status/arpEntry" | jq
```

<details>
<summary>Reveal Output</summary>
<p>

```json
[
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747981696447354400,
    "time": "2025-05-23T06:28:16.447354345Z",
    "prefix": "eos_native:Smash/arp/status/arpEntry",
    "updates": [
      {
        "Path": "172.100.100.1_Management1_0/key/intfId",
        "values": {
          "172.100.100.1_Management1_0/key/intfId": "Management1"
        }
      },
      {
        "Path": "172.100.100.1_Management1_0/key/vrfId",
        "values": {
          "172.100.100.1_Management1_0/key/vrfId": {
            "value": 0
          }
        }
      },
      {
        "Path": "172.100.100.1_Management1_0/key/addr",
        "values": {
          "172.100.100.1_Management1_0/key/addr": "172.100.100.1"
        }
      },
      {
        "Path": "172.100.100.1_Management1_0/ethAddr",
        "values": {
          "172.100.100.1_Management1_0/ethAddr": "02:42:e3:84:97:b9"
        }
      },
      {
        "Path": "172.100.100.1_Management1_0/isStatic",
        "values": {
          "172.100.100.1_Management1_0/isStatic": false
        }
      },
      {
        "Path": "172.100.100.1_Management1_0/source",
        "values": {
          "172.100.100.1_Management1_0/source": {
            "value": 1
          }
        }
      },
      {
        "Path": "172.100.100.2_Management1_0/source",
        "values": {
          "172.100.100.2_Management1_0/source": {
            "value": 1
          }
        }
      },
      {
        "Path": "172.100.100.2_Management1_0/key/intfId",
        "values": {
          "172.100.100.2_Management1_0/key/intfId": "Management1"
        }
      },
      {
        "Path": "172.100.100.2_Management1_0/key/vrfId",
        "values": {
          "172.100.100.2_Management1_0/key/vrfId": {
            "value": 0
          }
        }
      },
      {
        "Path": "172.100.100.2_Management1_0/key/addr",
        "values": {
          "172.100.100.2_Management1_0/key/addr": "172.100.100.2"
        }
      },
      {
        "Path": "172.100.100.2_Management1_0/ethAddr",
        "values": {
          "172.100.100.2_Management1_0/ethAddr": "02:42:ac:64:64:02"
        }
      },
      {
        "Path": "172.100.100.2_Management1_0/isStatic",
        "values": {
          "172.100.100.2_Management1_0/isStatic": false
        }
      }
    ]
  }
]
```

</p>
</details>

## Cli Origin

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip  get --path "cli:/show version"
```

<details>
<summary>Reveal Output</summary>
<p>

```json
[
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747987293521267754,
    "time": "2025-05-23T08:01:33.521267754Z",
    "updates": [
      {
        "Path": "cli:show version",
        "values": {
          "show version": {
            "architecture": "aarch64",
            "bootupTimestamp": 1747981663.575444,
            "configMacAddress": "00:00:00:00:00:00",
            "hardwareRevision": "",
            "hwMacAddress": "00:00:00:00:00:00",
            "imageFormatVersion": "1.0",
            "imageOptimization": "None",
            "internalBuildId": "ec3ed791-8ca6-4ae1-a16a-08f747fc981a",
            "internalVersion": "4.34.1F-41757195",
            "isIntlVersion": false,
            "kernelVersion": "6.10.14-linuxkit",
            "memFree": 2166644,
            "memTotal": 10175280,
            "mfgName": "Arista",
            "modelName": "cEOSLab",
            "serialNumber": "B41626AAD233E43A723BA3778A850982",
            "systemMacAddress": "00:1c:73:72:44:f0",
            "uptime": 5629.958059310913,
            "version": "4.34.1F-41757195 (engineering build)"
          }
        }
      }
    ]
  }
]
```

</p>
</details></br>

```shell
gnmic -a clab-arlab-spine1:6030 -u admin -p admin --insecure --gzip --encoding ASCII get --path "cli:/show running-config"
```

<details>
<summary>Reveal Output</summary>
<p>

```json
[
  {
    "source": "clab-arlab-spine1:6030",
    "timestamp": 1747987940404905554,
    "time": "2025-05-23T08:12:20.404905554Z",
    "updates": [
      {
        "Path": "cli:show running-config",
        "values": {
          "show running-config": "! Command: show running-config\n! device: spine1 (cEOSLab, EOS-4.34.1F-41757195.orinocorel (engineering build))\n!\nno aaa root\n!\nusername admin privilege 15 role network-admin secret sha512 $6$ZpibF/SwnFp8AP66$Mnrvz5xLfAYWVvuCtVOLs6tdChTn.P.WeDP5T5WIQH5zJ0puhgBFv8nPTAROmSsfAbtNo7ebLz91lNxnYPGwl0\n!\nmanagement api http-commands\n   protocol https ssl profile self-signed\n   no shutdown\n!\nno service interface inactive port-id allocation disabled\n!\ntransceiver qsfp default-mode 4x10G\n!\nservice routing protocols model multi-agent\n!\nhostname spine1\n!\nspanning-tree mode mstp\n!\nsystem l1\n   unsupported speed action error\n   unsupported error-correction action error\n!\nmanagement api gnmi\n   transport grpc oob\n   provider eos-native\n!\nmanagement api netconf\n   transport ssh oob\n!\nmanagement api restconf\n   transport https oob\n      ssl profile self-signed\n      port 5900\n!\nmanagement security\n   ssl profile self-signed\n      cipher-list HIGH:!eNULL:!aNULL:!MD5:!ADH:!ANULL\n      certificate selfSigned.crt key selfSigned.key\n!\ninterface Ethernet1\n!\ninterface Ethernet2\n   description P2P_LINK_TO_LEAF2\n   no switchport\n   ip address 172.31.255.2/31\n!\ninterface Management1\n   description oob_management\n   ip address 172.100.100.2/24\n   ipv6 address 2001:172:100:100::3/80\n!\nip routing\n!\nip route 0.0.0.0/0 172.100.100.1\n!\nipv6 route ::/0 2001:172:100:100::1\n!\nrouter multicast\n   ipv4\n      software-forwarding kernel\n   !\n   ipv6\n      software-forwarding kernel\n!\nend\n"
        }
      }
    ]
  }
]
```

</p>
</details>

## Local gNMI Get Requests

```shell
CEOS-RTR2# show gnmi get /system/state
```

<details>
<summary>Reveal Output</summary>
<p>

```json
/system/state:
{
  "openconfig-system:boot-time": "1748239233930232048",
  "openconfig-system:current-datetime": "2025-05-26T06:10:34Z",
  "openconfig-system:hostname": "CEOS-RTR2",
  "openconfig-system:last-configuration-timestamp": "1748239321906310796",
  "openconfig-system:software-version": "4.34.1F-41757195.orinocorel (engineering build)"
}
```

</p>
</details>

