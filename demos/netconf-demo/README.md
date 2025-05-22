# NETCONF Demo

- [NETCONF Demo](#netconf-demo)
  - [Requirements](#requirements)
  - [Getting Capabilities](#getting-capabilities)
  - [Getting States](#getting-states)
  - [Get Configuration](#get-configuration)
  - [Configuring Device](#configuring-device)
    - [Configuring hostname with edit-config \& merge](#configuring-hostname-with-edit-config--merge)
    - [Configuring DNS Servers using edit-config and merge](#configuring-dns-servers-using-edit-config-and-merge)
    - [Replacing DNS Servers configuration using edit-config and replace](#replacing-dns-servers-configuration-using-edit-config-and-replace)
    - [Deleting DNS Server using edit-config and delete](#deleting-dns-server-using-edit-config-and-delete)
    - [Modifying running-config with lock operation](#modifying-running-config-with-lock-operation)
    - [Copy running configuration to startup configuration](#copy-running-configuration-to-startup-configuration)

In this demo, we will take a look at few examples related to `NETCONF` using `ncclient` with Arista cEOS-Lab devices.

## Requirements

Confirm the following packages are installed, else install them using `pip`

```shell
python3 -m pip freeze | egrep "pyang|pyangbind|ncclient"
```

Start the [arista-ceos](../../labs/arista-ceos/) lab using containerlab.

## Getting Capabilities

Using `capabilities-demo.py` file we will get the client and server NETCONF capabilities

```python
from ncclient import manager

eos = manager.connect(host='172.100.200.3', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

print("\n########## CLIENT CAPABILITIES ##########\n")
for item in eos.client_capabilities:
    print(item)

print("\n########## SERVER CAPABILITIES ##########\n")
for item in eos.server_capabilities:
    print(item)

eos.close_session()
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
########## CLIENT CAPABILITIES ##########

urn:ietf:params:netconf:base:1.0
urn:ietf:params:netconf:base:1.1
urn:ietf:params:netconf:capability:writable-running:1.0
urn:ietf:params:netconf:capability:candidate:1.0
urn:ietf:params:netconf:capability:confirmed-commit:1.0
urn:ietf:params:netconf:capability:rollback-on-error:1.0
urn:ietf:params:netconf:capability:startup:1.0
urn:ietf:params:netconf:capability:url:1.0?scheme=http,ftp,file,https,sftp
urn:ietf:params:netconf:capability:validate:1.0
urn:ietf:params:netconf:capability:xpath:1.0
urn:ietf:params:netconf:capability:notification:1.0
urn:ietf:params:netconf:capability:interleave:1.0
urn:ietf:params:netconf:capability:with-defaults:1.0

########## SERVER CAPABILITIES ##########

urn:ietf:params:netconf:base:1.0
urn:ietf:params:netconf:base:1.1
urn:ietf:params:xml:ns:netconf:base:1.0
urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring
urn:ietf:params:netconf:capability:writable-running:1.0
urn:ietf:params:netconf:capability:candidate:1.0
urn:ietf:params:netconf:capability:url:1.0?scheme=file,flash,ftp,http
http://arista.com/yang/experimental/eos/vxlan?module=arista-exp-eos-vxlan&revision=2023-11-01
http://openconfig.net/yang/ospf-types?module=openconfig-ospf-types&revision=2018-11-21
http://openconfig.net/yang/igmp?module=openconfig-igmp&revision=2023-02-03
http://openconfig.net/yang/platform/linecard?module=openconfig-platform-linecard&revision=2024-04-12
http://openconfig.net/yang/acl?module=openconfig-acl&revision=2023-02-06
http://arista.com/yang/openconfig/aft/augments?module=arista-aft-augments&revision=2024-04-26
http://arista.com/yang/experimental/eos/arista-rcf-rcf-open-config?module=arista-rcf-rcf-open-config&revision=2023-09-12
urn:ietf:params:xml:ns:yang:iana-if-type?module=iana-if-type&revision=2014-05-08
http://arista.com/yang/openconfig/telemetry/augments?module=arista-telemetry-augments&revision=2023-01-24
http://arista.com/yang/openconfig/qos/notsupported-deviations?module=arista-qos-notsupported-deviations&revision=2025-04-29
http://arista.com/yang/experimental/eos/arista-l1-open-config-optical-channel-model-augment?module=arista-l1-open-config-optical-channel-model-augment&revision=2022-05-12
http://arista.com/yang/openconfig/isis/augments?module=arista-isis-augments&revision=2024-06-14
http://openconfig.net/yang/local-routing?module=openconfig-local-routing&revision=2025-02-20
urn:ietf:params:xml:ns:yang:ietf-yang-metadata?module=ietf-yang-metadata&revision=2016-08-05
http://arista.com/yang/openconfig/pim/augments?module=arista-pim-augments&revision=2024-10-16
http://openconfig.net/yang/interfaces/aggregate?module=openconfig-if-aggregate&revision=2022-06-28
http://openconfig.net/yang/spanning-tree/types?module=openconfig-spanning-tree-types&revision=2021-06-16
http://openconfig.net/yang/ospfv2?module=openconfig-ospfv2&revision=2024-06-17
http://arista.com/yang/cli?module=arista-cli&revision=2020-02-11
http://openconfig.net/yang/transport-types?module=openconfig-transport-types&revision=2024-11-21
http://openconfig.net/yang/platform/port?module=openconfig-platform-port&revision=2023-03-22
http://openconfig.net/yang/ospf-policy?module=openconfig-ospf-policy&revision=2018-11-21
http://arista.com/yang/openconfig/network-instances/deviations?module=arista-netinst-deviations&revision=2025-03-14
http://openconfig.net/yang/rib/bgp?module=openconfig-rib-bgp&revision=2022-12-20
http://openconfig.net/yang/segment-routing-types?module=openconfig-segment-routing-types&revision=2020-02-04
http://openconfig.net/yang/igmp/types?module=openconfig-igmp-types&revision=2018-11-21
http://openconfig.net/yang/gnsi?module=openconfig-gnsi&revision=2024-02-13
http://arista.com/yang/experimental/multicast?module=arista-exp-eos-multicast&revision=2017-10-20
http://arista.com/yang/openconfig/sampling/notsupported-deviations?module=arista-sampling-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/system-utilization?module=openconfig-system-utilization&revision=2023-02-13
http://openconfig.net/yang/pcep?module=openconfig-pcep&revision=2023-04-25
http://openconfig.net/yang/sr?module=openconfig-segment-routing&revision=2023-08-09
http://openconfig.net/yang/platform/fabric?module=openconfig-platform-fabric&revision=2022-07-28
http://arista.com/yang/experimental/eos/arista-fhrp-lib-varp-status?module=arista-fhrp-lib-varp-status&revision=2023-03-13
http://arista.com/yang/experimental/eos/arista-ale-counters-open-config-specialized-counters?module=arista-ale-counters-open-config-specialized-counters&revision=2021-10-20
http://openconfig.net/yang/ldp?module=openconfig-mpls-ldp&revision=2023-02-06
http://openconfig.net/yang/openflow?module=openconfig-openflow&revision=2018-11-21
http://openconfig.net/yang/network-instance?module=openconfig-network-instance&revision=2025-02-20
http://openconfig.net/yang/aft-summary?module=openconfig-aft-summary&revision=2024-01-12
http://arista.com/yang/vlan-translation?module=vlan-translation&revision=2020-08-10
http://openconfig.net/yang/openconfig-isis?module=openconfig-isis&revision=2024-02-28
http://arista.com/yang/experimental/eos/evpn?module=arista-exp-eos-evpn&revision=2020-12-07
http://openconfig.net/yang/openconfig-icmpv4-types?module=openconfig-icmpv4-types&revision=2023-01-26
http://openconfig.net/yang/system/procmon?module=openconfig-procmon&revision=2019-03-15
http://arista.com/yang/openconfig/lacp/augments?module=arista-lacp-augments&revision=2025-02-24
http://arista.com/yang/openconfig/flex-algo/augments?module=arista-flex-algo-augments&revision=2024-03-01
http://arista.com/yang/experimental/eos/arista-arnet-vrf-name?module=arista-arnet-vrf-name&revision=2022-03-28
http://openconfig.net/yang/qos?module=openconfig-qos&revision=2023-10-13
http://openconfig.net/yang/network-instance-l3?module=openconfig-network-instance-l3&revision=2022-11-08
http://openconfig.net/yang/openconfig-isis-policy?module=openconfig-isis-policy&revision=2023-11-02
http://arista.com/yang/openconfig/lldp/deviations?module=arista-lldp-deviations&revision=2022-01-17
http://arista.com/yang/openconfig/defined-sets/notsupported-deviations?module=arista-defined-sets-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/interfaces/tunnel?module=openconfig-if-tunnel&revision=2018-11-21
http://openconfig.net/yang/isis-types?module=openconfig-isis-types&revision=2022-02-11
http://openconfig.net/yang/license?module=openconfig-license&revision=2020-04-22
http://openconfig.net/yang/platform/controller-card?module=openconfig-platform-controller-card&revision=2024-04-10
http://arista.com/yang/openconfig/network-instance/notsupported-deviations?module=arista-network-instance-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/types/yang?module=openconfig-yang-types&revision=2024-05-30
http://openconfig.net/yang/system/logging?module=openconfig-system-logging&revision=2024-08-20
http://openconfig.net/yang/header-fields?module=openconfig-packet-match&revision=2023-03-01
http://openconfig.net/yang/openflow/types?module=openconfig-openflow-types&revision=2022-05-24
http://openconfig.net/yang/system?module=openconfig-system&revision=2024-09-24
http://arista.com/yang/experimental/eos/arista-fhrp-fhrp-config?module=arista-fhrp-fhrp-config&revision=2023-02-13
http://openconfig.net/yang/sampling?module=openconfig-sampling&revision=2022-06-21
http://arista.com/yang/openconfig/system/augments?module=arista-system-augments&revision=2025-03-14
http://arista.com/yang/openconfig/mpls/deviations?module=arista-mpls-deviations&revision=2024-03-30
http://arista.com/yang/experimental/eos/arista-ale-counters-open-config-interrupt-counters?module=arista-ale-counters-open-config-interrupt-counters&revision=2021-10-20
http://openconfig.net/yang/aft?module=openconfig-aft&revision=2025-03-12
http://openconfig.net/yang/programming-errors?module=openconfig-programming-errors&revision=2022-10-11
http://openconfig.net/yang/bfd?module=openconfig-bfd&revision=2025-02-05
http://openconfig.net/yang/system/terminal?module=openconfig-system-terminal&revision=2018-11-21
http://arista.com/yang/experimental/eos/arista-mirroring-tap-agg-common?module=arista-mirroring-tap-agg-common&revision=2024-08-12
http://arista.com/yang/openconfig/policy/augments?module=arista-rpol-augments&revision=2025-01-30
http://openconfig.net/yang/evpn?module=openconfig-evpn&revision=2024-08-14
http://arista.com/yang/experimental/eos/arista-stp-augments?module=arista-stp-augments&revision=2019-11-28
http://arista.com/yang/experimental/eos/arista-intf-intf?module=arista-intf-intf&revision=2023-08-15
http://arista.com/yang/openconfig/routing-policy/notsupported-deviations?module=arista-routing-policy-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/system-controlplane?module=openconfig-system-controlplane&revision=2023-03-03
http://arista.com/yang/experimental/eos/qos/acl?module=arista-exp-eos-qos-acl-config&revision=2024-04-18
http://arista.com/yang/openconfig/network-instances/augments?module=arista-netinst-augments&revision=2023-02-08
http://arista.com/yang/experimental/eos/arista-l1-open-config-platform-model-augment?module=arista-l1-open-config-platform-model-augment&revision=2022-05-12
http://arista.com/yang/openconfig/mpls/augments?module=arista-mpls-augments&revision=2025-02-07
http://arista.com/yang/openconfig/pim/deviations?module=arista-pim-deviations&revision=2024-10-14
http://openconfig.net/yang/interfaces/ip?module=openconfig-if-ip&revision=2024-05-28
http://arista.com/yang/rpc/netconf?module=arista-rpc-netconf&revision=2023-03-03
http://arista.com/yang/openconfig/macsec/deviations?module=arista-macsec-deviations&revision=2023-01-05
http://arista.com/yang/openconfig/relay-agent/deviations?module=arista-relay-agent-deviations&revision=2023-11-14
http://arista.com/yang/openconfig/bfd/augments?module=arista-bfd-augments&revision=2022-05-26
http://openconfig.net/yang/rsvp?module=openconfig-mpls-rsvp&revision=2023-02-06
http://openconfig.net/yang/policy-types?module=openconfig-policy-types&revision=2024-05-14
http://arista.com/yang/openconfig/qos/augments?module=arista-qos-augments&revision=2020-11-30
http://arista.com/yang/experimental/eos/arista-tunnel-tunnel-basic-types?module=arista-tunnel-tunnel-basic-types&revision=2021-10-20
http://arista.com/yang/openconfig/lacp/notsupported-deviations?module=arista-lacp-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/p4rt?module=openconfig-p4rt&revision=2023-12-13
http://arista.com/yang/openconfig/system/deviations?module=arista-system-deviations&revision=2023-03-14
http://arista.com/yang/experimental/eos/vxlan/config?module=arista-exp-eos-vxlan-config&revision=2023-11-01
http://arista.com/yang/openconfig/ospf/augments?module=arista-ospf-augments&revision=2023-04-20
http://arista.com/yang/experimental/eos?module=arista-exp-eos&revision=2016-11-09
http://arista.com/yang/experimental/eos/arista-arnet-conn-tuple?module=arista-arnet-conn-tuple&revision=2022-03-28
http://openconfig.net/yang/rib/bgp-ext?module=openconfig-rib-bgp-ext&revision=2019-04-25
http://arista.com/yang/experimental/eos/arista-l1-open-config-phy-model?module=arista-l1-open-config-phy-model&revision=2023-12-05
http://arista.com/yang/openconfig/stp/deviations?module=arista-stp-deviations&revision=2024-01-11
urn:aristanetworks:yang:experimental:eos?module=arista-exp-eos-mlag&revision=2021-09-27
http://openconfig.net/yang/platform/transceiver?module=openconfig-platform-transceiver&revision=2024-10-09
http://arista.com/yang/experimental/isis-flex-algo?module=openconfig-isis-flex-algo&revision=2021-09-30
http://arista.com/yang/experimental/eos/arista-macsec-macsec-open-config-state-augment?module=arista-macsec-macsec-open-config-state-augment&revision=2025-02-25
http://openconfig.net/yang/vlan-types?module=openconfig-vlan-types&revision=2022-05-24
http://openconfig.net/yang/isis-lsdb-types?module=openconfig-isis-lsdb-types&revision=2018-11-21
http://openconfig.net/yang/aft/ni?module=openconfig-aft-network-instance&revision=2023-04-25
http://arista.com/yang/experimental/eos/varp/intf?module=arista-exp-eos-varp-intf&revision=2023-05-03
http://arista.com/yang/experimental/eos/arista-ebra-intf-encap?module=arista-ebra-intf-encap&revision=2021-10-20
urn:ietf:params:xml:ns:netconf:base:1.0?module=ietf-netconf&revision=2011-06-01
http://openconfig.net/yang/interfaces?module=openconfig-interfaces&revision=2024-12-05
http://arista.com/yang/openconfig/policy/deviations?module=arista-rpol-deviations&revision=2025-01-29
http://openconfig.net/yang/flexalgo?module=openconfig-flexalgo&revision=2023-05-24
http://arista.com/yang/experimental/eos/qos/config?module=arista-exp-eos-qos-config&revision=2022-10-31
http://openconfig.net/yang/bgp-policy?module=openconfig-bgp-policy&revision=2024-11-13
http://openconfig.net/yang/sampling/sflow?module=openconfig-sampling-sflow&revision=2022-06-21
http://arista.com/yang/openconfig/keychain/notsupported-deviations?module=arista-keychain-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/policy-forwarding/sr-te?module=openconfig-pf-srte&revision=2019-10-15
http://openconfig.net/yang/pim/types?module=openconfig-pim-types&revision=2024-05-31
http://openconfig.net/yang/platform/integrated-circuit?module=openconfig-platform-integrated-circuit&revision=2022-04-20
http://arista.com/yang/openconfig/openflow/deviations?module=arista-openflow-deviations&revision=2020-11-30
http://arista.com/yang/experimental/eos/arista-classification-controller-field-set-open-config?module=arista-classification-controller-field-set-open-config&revision=2024-02-06
http://arista.com/yang/openconfig/lldp/augments?module=arista-lldp-augments&revision=2020-11-30
http://arista.com/yang/experimental/eos/arista-acl-spec?module=arista-acl-spec&revision=2022-03-28
http://openconfig.net/yang/mpls-types?module=openconfig-mpls-types&revision=2023-12-14
http://openconfig.net/yang/platform-pipeline-counters?module=openconfig-platform-pipeline-counters&revision=2023-10-08
http://arista.com/yang/experimental/eos/arista-mirroring-mirroring-open-config?module=arista-mirroring-mirroring-open-config&revision=2024-08-12
http://openconfig.net/yang/packet-match-types?module=openconfig-packet-match-types&revision=2023-01-29
http://arista.com/yang/experimental/eos/arista-mpls-mpls-open-config-static-augment?module=arista-mpls-mpls-open-config-static-augment&revision=2024-03-11
http://openconfig.net/yang/bgp-types?module=openconfig-bgp-types&revision=2024-09-06
http://openconfig.net/yang/evpn-types?module=openconfig-evpn-types&revision=2021-06-21
http://openconfig.net/yang/hercules/qos?module=openconfig-hercules-qos&revision=2018-06-01
https://github.com/openconfig/gnsi/credentialz/yang?module=gnsi-credentialz&revision=2024-01-01
http://openconfig.net/yang/system-grpc?module=openconfig-system-grpc&revision=2024-05-29
http://openconfig.net/yang/platform-types?module=openconfig-platform-types&revision=2024-11-04
http://arista.com/yang/openconfig/policy-forwarding/deviations?module=arista-srte-deviations&revision=2021-04-19
http://openconfig.net/yang/platform/psu?module=openconfig-platform-psu&revision=2018-11-21
http://arista.com/yang/openconfig/lldp/notsupported-deviations?module=arista-lldp-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/types/inet?module=openconfig-inet-types&revision=2024-01-05
http://arista.com/yang/openconfig/interfaces/notsupported-deviations?module=arista-interfaces-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/platform/healthz?module=openconfig-platform-healthz&revision=2023-04-11
http://arista.com/yang/openconfig/policy-forwarding/augments?module=arista-srte-augments&revision=2020-11-30
http://openconfig.net/yang/platform/software-module?module=openconfig-platform-software&revision=2021-06-16
http://arista.com/yang/openconfig/platform/augments?module=arista-platform-augments&revision=2024-12-17
urn:ietf:params:xml:ns:yang:ietf-inet-types?module=ietf-inet-types&revision=2013-07-15
http://arista.com/yang/experimental/eos/bgp?module=arista-exp-eos-bgp&revision=2024-05-10
http://openconfig.net/yang/lacp?module=openconfig-lacp&revision=2024-09-24
http://arista.com/yang/openconfig/acl/notsupported-deviations?module=arista-acl-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/mpls-sr?module=openconfig-mpls-sr&revision=2018-11-21
http://arista.com/yang/openconfig/ntp/augments?module=arista-ntp-augments&revision=2024-09-16
http://openconfig.net/yang/platform?module=openconfig-platform&revision=2025-01-30
http://arista.com/yang/experimental/eos/l2protocolforwarding?module=arista-exp-eos-l2protocolforwarding&revision=2022-08-18
http://arista.com/yang/openconfig/ospf/deviations?module=arista-ospf-deviations&revision=2023-11-16
http://arista.com/yang/experimental/eos/arista-arnet-rate?module=arista-arnet-rate&revision=2023-08-15
http://openconfig.net/yang/network-instance-static?module=openconfig-network-instance-static&revision=2025-02-20
http://arista.com/yang/openconfig/terminal-device/notsupported-deviations?module=arista-terminal-device-notsupported-deviations&revision=2025-04-29
http://arista.com/yang/openconfig/bgp/augments?module=arista-bgp-augments&revision=2024-06-08
https://arista.com/fmp/segmentation.v1?module=arista-segmentation.v1&revision=2020-04-27
http://arista.com/yang/openconfig/spanning-tree/notsupported-deviations?module=arista-spanning-tree-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/openconfig-icmpv6-types?module=openconfig-icmpv6-types&revision=2023-05-02
http://arista.com/yang/experimental/eos/eos-types?module=arista-eos-types&revision=2023-09-05
http://openconfig.net/yang/routing-policy?module=openconfig-routing-policy&revision=2024-11-26
http://arista.com/yang/experimental/eos/arista-pfc-buffer-counters-augment?module=arista-pfc-buffer-counters-augment&revision=2024-12-11
http://arista.com/yang/experimental/eos/arista-sand-hardware-drop-counters?module=arista-sand-hardware-drop-counters&revision=2023-01-01
http://arista.com/yang/experimental/eos/arista-nat-nat-dynamic?module=arista-nat-nat-dynamic&revision=2022-03-28
http://arista.com/yang/experimental/eos/arista-sand-control-plane-traffic-counters?module=arista-sand-control-plane-traffic-counters&revision=2023-02-02
http://openconfig.net/yang/telemetry?module=openconfig-telemetry&revision=2018-11-21
http://arista.com/yang/openconfig/macsec/notsupported-deviations?module=arista-macsec-notsupported-deviations&revision=2025-04-29
http://arista.com/yang/openconfig/isis/deviations?module=arista-isis-deviations&revision=2025-02-18
http://arista.com/yang/openconfig/interfaces/deviations?module=arista-intf-deviations&revision=2024-02-12
http://arista.com/yang/experimental/eos/arista-system-session?module=arista-system-session&revision=2023-12-19
http://arista.com/yang/experimental/eos/arista-arnet-vlan-tpid?module=arista-arnet-vlan-tpid&revision=2021-10-20
http://arista.com/yang/experimental/eos/arista-traffic-policy?module=arista-traffic-policy&revision=2024-03-15
http://arista.com/yang/experimental/eos/arista-pseudowire-pseudowire-status?module=arista-pseudowire-pseudowire-status&revision=2021-10-20
https://github.com/openconfig/gnsi/authz/yang?module=gnsi-authz&revision=2023-09-13
http://arista.com/yang/experimental/eos/arista-arnet-vlan-tag?module=arista-arnet-vlan-tag&revision=2021-10-20
http://openconfig.net/yang/macsec?module=openconfig-macsec&revision=2025-01-02
http://arista.com/yang/openconfig/network-instance/deviations?module=arista-vlan-deviations&revision=2020-11-30
http://openconfig.net/yang/platform/cpu?module=openconfig-platform-cpu&revision=2018-11-21
http://arista.com/yang/cert/gnoi-cert?module=arista-gnoi-cert&revision=2018-01-15
http://openconfig.net/yang/platform/fan?module=openconfig-platform-fan&revision=2018-11-21
urn:ietf:params:xml:ns:yang:ietf-yang-types?module=ietf-yang-types&revision=2013-07-15
http://arista.com/yang/experimental/eos/arista-connectivity-monitor-types-connectivity-monitor-types?module=arista-connectivity-monitor-types-connectivity-monitor-types&revision=2024-05-02
http://openconfig.net/yang/hercules/interfaces?module=openconfig-hercules-interfaces&revision=2018-06-01
http://openconfig.net/yang/aaa/types?module=openconfig-aaa-types&revision=2018-11-21
http://openconfig.net/yang/interfaces/ethernet?module=openconfig-if-ethernet&revision=2024-09-17
http://openconfig.net/yang/poe?module=openconfig-if-poe&revision=2018-11-21
http://arista.com/yang/openconfig/qos/deviations?module=arista-qos-deviations&revision=2024-02-28
https://github.com/openconfig/yang/gnsi/acctz?module=openconfig-gnsi-acctz&revision=2024-12-24
http://openconfig.net/yang/qos-types?module=openconfig-qos-types&revision=2018-11-21
http://arista.com/yang/experimental/eos/arista-interfaces-rates?module=arista-interfaces-rates&revision=2024-04-15
http://openconfig.net/yang/oc-keychain?module=openconfig-keychain&revision=2024-05-30
http://arista.com/yang/openconfig/sflow/deviations?module=arista-sflow-deviations&revision=2023-07-27
http://openconfig.net/yang/aaa?module=openconfig-aaa&revision=2022-07-29
http://openconfig.net/yang/vlan?module=openconfig-vlan&revision=2023-02-07
http://openconfig.net/yang/fib-types?module=openconfig-aft-types&revision=2025-01-28
http://arista.com/yang/openconfig/bfd/deviations?module=arista-bfd-deviations&revision=2020-11-30
http://arista.com/yang/openconfig/interfaces/augments?module=arista-intf-augments&revision=2025-03-11
http://openconfig.net/yang/terminal-device?module=openconfig-terminal-device&revision=2024-06-12
http://openconfig.net/yang/mpls?module=openconfig-mpls&revision=2024-06-19
http://arista.com/yang/openconfig/qos/voq/augments?module=arista-qos-voq-augments&revision=2025-01-13
http://openconfig.net/yang/messages?module=openconfig-messages&revision=2024-07-15
http://openconfig.net/yang/relay-agent?module=openconfig-relay-agent&revision=2023-02-06
http://arista.com/yang/openconfig/flex-algo/deviations?module=arista-flex-algo-deviations&revision=2024-03-01
http://arista.com/yang/openconfig/platform/notsupported-deviations?module=arista-platform-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/bgp?module=openconfig-bgp&revision=2024-09-06
urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring?module=ietf-netconf-monitoring&revision=2010-10-04
http://arista.com/yang/experimental/eos/arista-nat-nat?module=arista-nat-nat&revision=2022-03-28
http://arista.com/yang/experimental/eos/arista-ebra-octap-agg-port-config?module=arista-ebra-octap-agg-port-config&revision=2024-08-12
http://arista.com/yang/openconfig/telemetry/notsupported-deviations?module=arista-telemetry-notsupported-deviations&revision=2025-04-29
http://arista.com/yang/experimental/eos/arista-ale-counters-open-config-hardware-drop-counters?module=arista-ale-counters-open-config-hardware-drop-counters&revision=2023-01-01
http://openconfig.net/yang/defined-sets?module=openconfig-defined-sets&revision=2022-12-14
http://arista.com/yang/experimental/igmpsnooping?module=arista-exp-eos-igmpsnooping&revision=2025-03-23
https://github.com/openconfig/gnsi/certz/yang?module=gnsi-certz&revision=2024-02-13
http://openconfig.net/yang/openconfig-metadata?module=openconfig-metadata&revision=2020-08-06
http://openconfig.net/yang/lldp?module=openconfig-lldp&revision=2018-11-21
http://arista.com/yang/experimental/eos/arista-ale-counters-open-config-fap-fe-serdes-info-augment?module=arista-ale-counters-open-config-fap-fe-serdes-info-augment&revision=2024-08-22
http://arista.com/yang/experimental/eos/arista-l1-open-config-xcvr-oc-types?module=arista-l1-open-config-xcvr-oc-types&revision=2023-12-05
http://openconfig.net/interfaces/sdn-ext?module=openconfig-if-sdn-ext&revision=2024-02-21
http://openconfig.net/yang/rib/bgp-types?module=openconfig-rib-bgp-types&revision=2019-03-14
http://openconfig.net/yang/alarms/types?module=openconfig-alarm-types&revision=2018-11-21
http://openconfig.net/yang/network-instance-types?module=openconfig-network-instance-types&revision=2021-07-14
http://openconfig.net/yang/oc-keychain-types?module=openconfig-keychain-types&revision=2024-08-27
http://openconfig.net/yang/spanning-tree?module=openconfig-spanning-tree&revision=2019-11-28
http://openconfig.net/yang/policy-forwarding?module=openconfig-policy-forwarding&revision=2024-11-14
http://arista.com/yang/experimental/eos/arista-qos-interface-queue-state-augment?module=arista-qos-interface-queue-state-augment&revision=2024-08-22
urn:ietf:params:xml:ns:yang:ietf-interfaces?module=ietf-interfaces&revision=2018-02-20
http://arista.com/yang/openconfig/bfd/notsupported-deviations?module=arista-bfd-notsupported-deviations&revision=2025-04-29
http://arista.com/yang/openconfig/lacp/deviations?module=arista-lacp-deviations&revision=2022-03-16
http://openconfig.net/yang/segment-routing/srte-policy?module=openconfig-srte-policy&revision=2021-07-28
http://arista.com/yang/experimental/eos/arista-arnet-ip?module=arista-arnet-ip&revision=2022-03-28
http://openconfig.net/yang/macsec/types?module=openconfig-macsec-types&revision=2019-07-01
http://arista.com/yang/experimental/eos/qos?module=arista-exp-eos-qos&revision=2017-09-26
http://openconfig.net/yang/openconfig-ext?module=openconfig-extensions&revision=2024-09-19
http://openconfig.net/yang/openconfig-types?module=openconfig-types&revision=2024-01-31
http://openconfig.net/yang/lldp/types?module=openconfig-lldp-types&revision=2018-11-21
http://arista.com/yang/openconfig/acl/deviations?module=arista-acl-deviations&revision=2024-11-22
http://arista.com/yang/openconfig/sflow/augments?module=arista-sflow-augments&revision=2023-04-26
http://openconfig.net/yang/telemetry-types?module=openconfig-telemetry-types&revision=2018-11-21
http://arista.com/yang/experimental/eos/arista-bgp-common-augments?module=arista-bgp-common-augments&revision=2023-12-01
http://openconfig.net/yang/pim?module=openconfig-pim&revision=2024-12-06
http://arista.com/yang/openconfig/bgp/deviations?module=arista-bgp-deviations&revision=2025-03-14
http://arista.com/yang/openconfig/network-instance/vlan/augments?module=arista-vlan-augments&revision=2020-11-30
http://arista.com/yang/openconfig/local-routing/deviations?module=arista-local-routing-deviations&revision=2024-07-16
http://arista.com/yang/experimental/eos/arista-ale-counters-open-config-control-plane-traffic-counters?module=arista-ale-counters-open-config-control-plane-traffic-counters&revision=2023-02-02
http://openconfig.net/yang/hercules/platform?module=openconfig-hercules-platform&revision=2018-06-01
http://arista.com/yang/openconfig/system/notsupported-deviations?module=arista-system-notsupported-deviations&revision=2025-04-29
http://openconfig.net/yang/alarms?module=openconfig-alarms&revision=2019-07-09
http://openconfig.net/yang/bgp?module=openconfig-bgp-common&revision=2024-09-06
http://openconfig.net/yang/rib/bgp?module=openconfig-rib-bgp-table-attributes&revision=2022-12-20
http://openconfig.net/yang/policy-forwarding?module=openconfig-pf-interfaces&revision=2024-11-14
http://openconfig.net/yang/openconfig-isis?module=openconfig-isis-routing&revision=2024-02-28
http://openconfig.net/yang/qos?module=openconfig-qos-elements&revision=2023-10-13
http://openconfig.net/yang/bgp?module=openconfig-bgp-neighbor&revision=2024-09-06
http://openconfig.net/yang/ospfv2?module=openconfig-ospfv2-area&revision=2024-06-17
http://openconfig.net/yang/ospfv2?module=openconfig-ospfv2-lsdb&revision=2024-06-17
http://openconfig.net/yang/aaa?module=openconfig-aaa-radius&revision=2022-07-29
http://openconfig.net/yang/bgp?module=openconfig-bgp-common-structure&revision=2024-09-06
http://openconfig.net/yang/bgp?module=openconfig-bgp-peer-group&revision=2024-09-06
http://openconfig.net/yang/aft?module=openconfig-aft-ethernet&revision=2025-03-12
http://openconfig.net/yang/ospfv2?module=openconfig-ospfv2-global&revision=2024-06-17
http://openconfig.net/yang/ospfv2?module=openconfig-ospfv2-common&revision=2024-06-17
http://openconfig.net/yang/policy-forwarding?module=openconfig-pf-forwarding-policies&revision=2024-11-14
http://openconfig.net/yang/policy-forwarding?module=openconfig-pf-path-groups&revision=2024-11-14
http://openconfig.net/yang/hercules/platform?module=openconfig-hercules-platform-node&revision=2018-06-01
http://openconfig.net/yang/aaa?module=openconfig-aaa-tacacs&revision=2022-07-29
http://openconfig.net/yang/network-instance?module=openconfig-network-instance-l2&revision=2025-02-20
http://openconfig.net/yang/bgp?module=openconfig-bgp-global&revision=2024-09-06
http://openconfig.net/yang/aft?module=openconfig-aft-common&revision=2025-03-12
http://openconfig.net/yang/aft?module=openconfig-aft-ipv6&revision=2025-03-12
http://openconfig.net/yang/ospfv2?module=openconfig-ospfv2-area-interface&revision=2024-06-17
http://openconfig.net/yang/aft?module=openconfig-aft-state-synced&revision=2025-03-12
http://openconfig.net/yang/hercules/platform?module=openconfig-hercules-platform-linecard&revision=2018-06-01
http://openconfig.net/yang/bgp-types?module=openconfig-bgp-errors&revision=2024-09-06
http://openconfig.net/yang/mpls?module=openconfig-mpls-igp&revision=2024-06-19
http://openconfig.net/yang/aft?module=openconfig-aft-pf&revision=2025-03-12
http://openconfig.net/yang/platform?module=openconfig-platform-common&revision=2025-01-30
http://openconfig.net/yang/qos?module=openconfig-qos-mem-mgmt&revision=2023-10-13
http://openconfig.net/yang/aft?module=openconfig-aft-mpls&revision=2025-03-12
http://openconfig.net/yang/hercules/platform?module=openconfig-hercules-platform-chassis&revision=2018-06-01
http://openconfig.net/yang/mpls?module=openconfig-mpls-static&revision=2024-06-19
http://openconfig.net/yang/hercules/platform?module=openconfig-hercules-platform-port&revision=2018-06-01
http://openconfig.net/yang/rib/bgp?module=openconfig-rib-bgp-tables&revision=2022-12-20
http://openconfig.net/yang/rib/bgp?module=openconfig-rib-bgp-attributes&revision=2022-12-20
http://openconfig.net/yang/mpls?module=openconfig-mpls-te&revision=2024-06-19
http://openconfig.net/yang/qos?module=openconfig-qos-interfaces&revision=2023-10-13
http://openconfig.net/yang/bgp?module=openconfig-bgp-common-multiprotocol&revision=2024-09-06
http://openconfig.net/yang/rib/bgp?module=openconfig-rib-bgp-shared-attributes&revision=2022-12-20
http://openconfig.net/yang/aft?module=openconfig-aft-ipv4&revision=2025-03-12
http://openconfig.net/yang/openconfig-isis?module=openconfig-isis-lsp&revision=2024-02-28
```

</p>
</details>

## Getting States

Using the `get-demo.py` script, which uses the `ncclient` `get` operation to get the state data. It also uses a filter to specify the portion of state data to retrieve.

```python
import xml.dom.minidom
from ncclient import manager

eos = manager.connect(host='172.100.100.3', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

# Get system information
systemState = """
<system>
    <state>
    </state>
</system>
"""

<---snipped--->

reply = eos.get(filter=("subtree", systemState))

print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

eos.close_session()
```

<details>
<summary>Reveal Output</summary>
<p>

```xml
########## SYSTEM STATE ##########

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:d0b3ad46-d1c4-408a-af1a-f4eb773cf528">
        <data>
                <system xmlns="http://openconfig.net/yang/system">
                        <state>
                                <boot-time>1747899764612676143</boot-time>
                                <current-datetime>2025-05-22T08:02:00Z</current-datetime>
                                <hostname>spine1</hostname>
                                <last-configuration-timestamp>1747899857260751724</last-configuration-timestamp>
                                <software-version>4.34.1F-41757195.orinocorel (engineering build)</software-version>
                        </state>
                </system>
        </data>
</rpc-reply>


########## INTERFACES STATE ##########

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:3f7d59ae-f6d3-4c18-be89-ca0be710ff3e">
        <data>
                <interfaces xmlns="http://openconfig.net/yang/interfaces">
                        <interface>
                                <name>Ethernet1</name>
                                <state>
                                        <admin-status>UP</admin-status>
                                        <oper-status>UP</oper-status>
                                </state>
                        </interface>
                        <interface>
                                <name>Ethernet2</name>
                                <state>
                                        <admin-status>UP</admin-status>
                                        <oper-status>UP</oper-status>
                                </state>
                        </interface>
                </interfaces>
        </data>
</rpc-reply>


########## LLDP STATE ##########

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:dc148e8b-2720-4749-9a1d-1bd4e5408f86">
        <data>
                <lldp xmlns="http://openconfig.net/yang/lldp">
                        <interfaces>
                                <interface>
                                        <name>Ethernet1</name>
                                        <neighbors>
                                                <neighbor>
                                                        <id>1</id>
                                                        <state>
                                                                <chassis-id>00:1c:73:ed:83:00</chassis-id>
                                                                <chassis-id-type>MAC_ADDRESS</chassis-id-type>
                                                                <id>1</id>
                                                                <last-update-time xmlns="http://arista.com/yang/openconfig/lldp/augments">1747900911</last-update-time>
                                                                <management-address>172.100.100.3</management-address>
                                                                <management-address-type>AFIPv4</management-address-type>
                                                                <port-id>Ethernet1</port-id>
                                                                <port-id-type>INTERFACE_NAME</port-id-type>
                                                                <registration-time xmlns="http://arista.com/yang/openconfig/lldp/augments">1747899796</registration-time>
                                                                <system-description>Arista Networks EOS version 4.34.1F-41757195.orinocorel (engineering build) running on an Arista cEOSLab</system-description>
                                                                <system-name>leaf1</system-name>
                                                        </state>
                                                </neighbor>
                                        </neighbors>
                                </interface>
                        </interfaces>
                </lldp>
        </data>
</rpc-reply>
```

</p>
</details>

## Get Configuration

Using the `get-config-demo.py` script, which uses ncclient `get-config` operation with a filter to retrieve parts of the configuration

```python
import xml.dom.minidom
from ncclient import manager

eos = manager.connect(host='172.100.100.3', port='830', timeout=60, username='admin', password='admin', hostkey_verify=False)

# Get hostname config
hostname = """
<system>
    <config>
        <hostname>
        </hostname>
    </config>
</system>
"""

<--snipped-->

reply = eos.get_config(source="running", filter=("subtree", users))

print(xml.dom.minidom.parseString(str(reply)).toprettyxml())

eos.close_session()
```

<details>
<summary>Reveal Output</summary>
<p>

```xml
########## HOSTNAME CONFIGURATION ##########

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:5d173bfd-f038-4310-b91b-4e9e5f2c0dc0">
        <data xmlns:netconf="http://arista.com/yang/rpc/netconf" netconf:time-modified="2025-05-22T07:43:51.801090379Z">
                <system xmlns="http://openconfig.net/yang/system">
                        <config>
                                <hostname>spine1</hostname>
                        </config>
                </system>
        </data>
</rpc-reply>


########## INTERFACE CONFIGURATION ##########

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:8a7407d0-d1b6-4978-a377-d7d79cb36a5b">
        <data xmlns:netconf="http://arista.com/yang/rpc/netconf" netconf:time-modified="2025-05-22T07:43:21.054362712Z">
                <interfaces xmlns="http://openconfig.net/yang/interfaces">
                        <interface>
                                <name>Management1</name>
                                <config>
                                        <description>oob_management</description>
                                </config>
                        </interface>
                </interfaces>
        </data>
</rpc-reply>


########## USER CONFIGURATION ##########

<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:b122dd1f-4819-480b-b959-06516dacce05">
        <data xmlns:netconf="http://arista.com/yang/rpc/netconf" netconf:time-modified="2025-05-22T07:43:51.801090379Z">
                <system xmlns="http://openconfig.net/yang/system">
                        <aaa>
                                <authentication>
                                        <users>
                                                <user>
                                                        <username>admin</username>
                                                        <config>
                                                                <password-hashed>$6$IxQfCisEIVBp33HL$rq4ZkAag06EGiUC3A32VLGQMT5gEV7vpZKd7/2G/fmxgAOOJgMTYFj.SX1xExH4.NIgYHjMAEgZLINB4bGazC1</password-hashed>
                                                                <password-mode xmlns="http://arista.com/yang/openconfig/system/augments">PASSWORD_REQUIRED</password-mode>
                                                                <role xmlns:oc-aaa-types="http://openconfig.net/yang/aaa/types">oc-aaa-types:SYSTEM_ROLE_ADMIN</role>
                                                                <username>admin</username>
                                                        </config>
                                                </user>
                                        </users>
                                </authentication>
                        </aaa>
                </system>
        </data>
</rpc-reply>
```

</p>
</details>

## Configuring Device

Generate the Python class module from a YANG module using `pyangbind` for more details check the [pyangbind-demo](../pyangbind-demo/)

```shell
pyang --plugindir $PYBINDPLUGIN -f pybind -p demos/public-yang -o demos/netconf-demo/oc_system.py demos/public-yang/openconfig-system.yang
```

### Configuring hostname with edit-config & merge

Using the `config-demo.py` we will configure the hostname using `edit-config` operation with the `merge` operation.

```python
import xml.dom.minidom
from ncclient import manager
from oc_system import openconfig_system
from pyangbind.lib.serialise import pybindIETFXMLEncoder


# Update hostname [ merge ]
def hostname(eos):
    HOSTNAME = 'DC1_LEAF1'
    oc_sys = openconfig_system()
    oc_sys.system.config.hostname = HOSTNAME
    config = '<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">\n' + pybindIETFXMLEncoder.serialise(oc_sys.system) + '</config>'
    #Print generated XML data
    print("\n{}\n".format(config))
    #Apply the configuration on the device
    print(eos.edit_config(target="running", config=config, default_operation="merge"))

<--snipped-->
```

<details>
<summary>Reveal Output</summary>
<p>

```xml
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
<system xmlns="http://openconfig.net/yang/system">
  <config>
    <hostname>DC1_LEAF1</hostname>
  </config>
</system>
</config>

<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:51e745c0-970f-48f3-afea-772edca4a527"><ok></ok></rpc-reply>
```

</p>
</details>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
DC1_LEAF1# show running-config section hostname
hostname DC1_LEAF1

--- aaa accounting logs ---

2025 May 22 08:18:26 admin    NETCONF     127.0.0.1 56528 127.0.0.1 22 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 08:18:26 admin    NETCONF     127.0.0.1 56528 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure session session17357341862476
2025 May 22 08:18:26 admin    NETCONF     127.0.0.1 56528 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=hostname DC1_LEAF1
2025 May 22 08:18:26 admin    NETCONF     127.0.0.1 56528 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 08:18:26 admin    NETCONF     127.0.0.1 56528 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure session session17357341862476 commit
```

</p>
</details>

### Configuring DNS Servers using edit-config and merge

Similarly, let's add DNS nameservers using `edit-config` and `merge` operation

```python
# Add DNS [ merge ]
def nameServers(server, eos):
    oc_sys = openconfig_system()
    oc_sys.system.dns.servers.server.add(server)
    dns_srv = oc_sys.system.dns.servers.server[server]
    dns_srv.config.address = server
    dns_srv.config.port = '53'
    config = '<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">\n' + pybindIETFXMLEncoder.serialise(oc_sys.system) + '</config>'
    #Print generated XML data
    print("\n{}\n".format(config))
    #Apply the configuration on the device
    print(eos.edit_config(target="running", config=config, default_operation="merge"))
```

<details>
<summary>Reveal Output</summary>
<p>

```xml
<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
<system xmlns="http://openconfig.net/yang/system">
  <dns>
    <servers>
      <server>
        <address>1.1.1.1</address>
        <config>
          <address>1.1.1.1</address>
          <port>53</port>
        </config>
      </server>
    </servers>
  </dns>
</system>
</config>

<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:13f93404-4321-412b-9860-bcd2f23a027a"><ok></ok></rpc-reply>

<config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
<system xmlns="http://openconfig.net/yang/system">
  <dns>
    <servers>
      <server>
        <address>1.0.0.1</address>
        <config>
          <address>1.0.0.1</address>
          <port>53</port>
        </config>
      </server>
    </servers>
  </dns>
</system>
</config>

<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:31ad68a0-5380-4159-b04d-42471cbac8b8"><ok></ok></rpc-reply>
```

</p>
</details>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
DC1_LEAF1# show running-config section name-server
ip name-server vrf default 1.0.0.1
ip name-server vrf default 1.1.1.1
```

</p>
</details>

### Replacing DNS Servers configuration using edit-config and replace

Here, we will use the `edit-config` operation with the `replace` operation to replace the DNS configuration,

```python
# Replace DNS configuration
def replaceDNS(eos):
    config = """
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <system xmlns="http://openconfig.net/yang/system">
            <dns>
                <servers nc:operation="replace">
                    <server>
                        <address>9.9.9.9</address>
                        <config>
                            <address>9.9.9.9</address>
                            <port>53</port>
                        </config>
                    </server>
                    <server>
                        <address>8.8.8.8</address>
                        <config>
                            <address>8.8.8.8</address>
                            <port>53</port>
                        </config>
                    </server>
                </servers>
            </dns>
        </system>
    </config>
    """
    print("\n{}\n".format(config))
    #Apply the configuration on the device
    print(eos.edit_config(target="running", config=config, default_operation="none"))
```

<details>
<summary>Reveal Output</summary>
<p>

```xml
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <system xmlns="http://openconfig.net/yang/system">
            <dns>
                <servers nc:operation="replace">
                    <server>
                        <address>9.9.9.9</address>
                        <config>
                            <address>9.9.9.9</address>
                            <port>53</port>
                        </config>
                    </server>
                    <server>
                        <address>8.8.8.8</address>
                        <config>
                            <address>8.8.8.8</address>
                            <port>53</port>
                        </config>
                    </server>
                </servers>
            </dns>
        </system>
    </config>
    

<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:5e1bb2f8-bea0-4a6c-b516-57230b622f70"><ok></ok></rpc-reply>
```

</p>
</details>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
DC1_LEAF1# show running-config section name-server
ip name-server vrf default 8.8.8.8
ip name-server vrf default 9.9.9.9

--- aaa accounting logs ---

2025 May 22 08:24:56 admin    NETCONF     127.0.0.1 46370 127.0.0.1 22 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 08:24:56 admin    NETCONF     127.0.0.1 46370 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure session session17747218502028
2025 May 22 08:24:56 admin    NETCONF     127.0.0.1 46370 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=no ip name-server vrf default 1.0.0.1
2025 May 22 08:24:56 admin    NETCONF     127.0.0.1 46370 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=no ip name-server vrf default 1.1.1.1
2025 May 22 08:24:56 admin    NETCONF     127.0.0.1 46370 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=ip name-server vrf default 9.9.9.9
2025 May 22 08:24:56 admin    NETCONF     127.0.0.1 46370 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=ip name-server vrf default 8.8.8.8
2025 May 22 08:24:56 admin    NETCONF     127.0.0.1 46370 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 08:24:56 admin    NETCONF     127.0.0.1 46370 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure session session17747218502028 commit
```

</p>
</details>

### Deleting DNS Server using edit-config and delete

Here, we will use the `edit-config` operation with `delete` operation to remove one of the DNS servers

```python
# Delete operation
def deleteDNS(eos):
    config = """
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <system xmlns="http://openconfig.net/yang/system">
            <dns>
                <servers>
                    <server>
                        <address nc:operation="delete">9.9.9.9</address>
                    </server>
                </servers>
            </dns>
        </system>
    </config>
    """
    print("\n{}\n".format(config))
    #Apply the configuration on the device
    print(eos.edit_config(target="running", config=config, default_operation="none"))
```

<details>
<summary>Reveal Output</summary>
<p>

```xml
    <config xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
        <system xmlns="http://openconfig.net/yang/system">
            <dns>
                <servers>
                    <server>
                        <address nc:operation="delete">9.9.9.9</address>
                    </server>
                </servers>
            </dns>
        </system>
    </config>
    

<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:a7caaf9b-69f2-443b-8a16-54516543e7f9"><ok></ok></rpc-reply>
```

</p>
</details>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
DC1_LEAF1# show running-config section name-server
ip name-server vrf default 8.8.8.8

--- aaa accounting logs ---

2025 May 22 08:28:11 admin    ssh         127.0.0.1       stop   service=shell priv-lvl=1 cmd=netconf start-client
2025 May 22 08:28:11 admin    NETCONF     127.0.0.1 54182 127.0.0.1 22 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 08:28:12 admin    NETCONF     127.0.0.1 54182 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure session session17942769627242
2025 May 22 08:28:12 admin    NETCONF     127.0.0.1 54182 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=no ip name-server vrf default 9.9.9.9
2025 May 22 08:28:12 admin    NETCONF     127.0.0.1 54182 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 08:28:12 admin    NETCONF     127.0.0.1 54182 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure session session17942769627242 commit
```

</p>
</details>

### Modifying running-config with lock operation

Here, we will use the `edit-config` operation with the running configuration datastore. It uses a `lock` operation.

```python
# Modify running configuration with lock
def runningConfigLock(eos):
    config_intf = """
    <config>
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface>
                <name>
                    Ethernet1
                </name>
                <config>
                    <description>
                        P2P_LINK_TO_DC1_SPINE1_Ethernet1
                    </description>
                </config>
            </interface>
        </interfaces>
    </config>
    """
    print("\n{}\n".format(config_intf))
    #Apply the configuration on the device
    with eos.locked("running"):
        input("\nRunning-config locked! Press any key to continue...")
        print(eos.edit_config(target="running", config=config_intf, default_operation="merge"))
        input("\nRunning-config modified! Press any key to continue...")
    print("\nRunning-config unlocked!\nEND")
```

<details>
<summary>Reveal Output</summary>
<p>

```xml
    <config>
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface>
                <name>
                    Ethernet1
                </name>
                <config>
                    <description>
                        P2P_LINK_TO_DC1_SPINE1_Ethernet1
                    </description>
                </config>
            </interface>
        </interfaces>
    </config>
    


Running-config locked! Press any key to continue...
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:d2647c3d-faf8-44ed-9932-4e00640250a5"><ok></ok></rpc-reply>

Running-config modified! Press any key to continue...

Running-config unlocked!
END
```

</p>
</details>
</br>

When executing the script we can see while the change is being made the `running` datastore gets locked,

<details>
<summary>Reveal Switch State</summary>
<p>

```shell

DC1_LEAF1# show configuration lock 
       TTY        User       Time Acquired        Location       Transaction    Reason
------------- ----------- ------------------- --------------- ----------------- ------
   NETCONF       admin         0:01:13 ago       127.0.0.1                 -         -

DC1_LEAF1#
DC1_LEAF1# configure terminal 
DC1_LEAF1(config)# interface Ethernet 2
% Unable to run this command (configuration is locked by another session)
DC1_LEAF1(config)# end

--- aaa accounting logs ---

2025 May 22 08:31:54 admin    ssh         127.0.0.1       stop   service=shell priv-lvl=1 cmd=netconf start-client
2025 May 22 08:31:55 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=0 cmd=enable
2025 May 22 08:31:55 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure lock

2025 May 22 08:34:03 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=enable
2025 May 22 08:34:03 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure session session18295053591445
2025 May 22 08:34:03 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=interface Ethernet1
2025 May 22 08:34:04 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=description P2P_LINK_TO_DC1_SPINE1_Ethernet1
2025 May 22 08:34:04 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=exit
2025 May 22 08:34:04 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=end
2025 May 22 08:34:04 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure session session18295053591445 commit

2025 May 22 08:34:54 admin    NETCONF     127.0.0.1 42350 127.0.0.1 22 stop   service=shell priv-lvl=15 cmd=configure unlock
```

</p>
</details>

### Copy running configuration to startup configuration

Here, we will use the `copy_config` operation to copy the `running-config` to `startup-config`

```python
# Copy running-config to startup-config
def copyConfig(eos):
    eos.copy_config(target="startup", source="running")
    print("\nCopied running-config to startup-config!\n")
```

Before we execute the script we can see the difference between the running-config and the startup-config

<details>
<summary>Reveal Diff</summary>
<p>

```shell
DC1_LEAF1# show running-config  diffs 
--- flash:/startup-config
+++ system:/running-config
@@ -1,4 +1,4 @@
-! device: leaf1 (cEOSLab, EOS-4.34.1F-41757195.orinocorel (engineering build))
+! device: DC1-LEAF1 (cEOSLab, EOS-4.34.1F-41757195.orinocorel (engineering build))
 !
 no aaa root
 !
@@ -14,7 +14,8 @@
 !
 service routing protocols model multi-agent
 !
-hostname leaf1
+hostname DC1_LEAF1
+ip name-server vrf default 8.8.8.8
 !
 spanning-tree mode mstp
 !
@@ -40,8 +41,10 @@
       certificate selfSigned.crt key selfSigned.key
 !
 interface Ethernet1
+   description P2P_LINK_TO_DC1_SPINE1_Ethernet1
 !
 interface Ethernet2
+   description P2P_LINK_TO_CLIENT1_Ethernet1
 !
 interface Management1
    description oob_management
```

</p>
</details>

<details>
<summary>Reveal Switch State</summary>
<p>

```shell
May 22 08:43:45 DC1-LEAF1 ConfigAgent: %SYS-5-CONFIG_STARTUP: Startup config saved from system:/running-config by admin on NETCONF (127.0.0.1).
```

</p>
</details>