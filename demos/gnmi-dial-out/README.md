# gNMI Dial-out via gRPC Tunnel

gNMI server instantiates (dials-out) a gRPC tunnel connection using a tunnel client, to the collector which runs a instance of a gRPC tunnel server listening for incoming tunnel requests.

The collector and gNMI server exchange gNMI request and response via the gRPC tunnel.

## Requirements

We will be using gnmic [Tunnel Server](https://gnmic.openconfig.net/user_guide/tunnel_server/). Confirm `gnmic` is installed, else install it using steps mentioned [here](https://gnmic.openconfig.net/install/).

Start the [arista-ceos](../../labs/arista-ceos/) lab using containerlab.

## Configuration

### Tunnel Server

Tunnel server configruation can be found in the [gnmic.yaml](../../labs/arista-ceos/gnmic.yaml) file.

<details>
<summary>Reveal File</summary>
<p>

```yaml
---
insecure: true
log: true
username: admin
password: admin

subscriptions:
  system-info:
    mode: once
    paths:
      - '/system/state/software-version'
      - '/system/state/hostname'
  port-stats:
    paths:
      - 'interfaces/interface[name=Management1]/state/counters/in-octets'
      - 'interfaces/interface[name=Management1]/state/counters/out-octets'
    stream_mode: on-change
  mem-stats:
    paths:
      - 'eos_native:/Kernel/proc/meminfo'
  cpu-stats:
    paths:
      - 'eos_native:/Kernel/proc/cpu/utilization/total'

targets:
  clab-arlab-spine1:
    address: 172.100.100.2:6030
    gzip: true
    subscriptions:
      - system-info
      - port-stats
  clab-arlab-leaf1:
    address: 172.100.100.3:6030
    gzip: true
    subscriptions:
      - system-info
      - mem-stats
  clab-arlab-leaf2:
    address: 172.100.100.4:6030
    gzip: true
    subscriptions:
      - system-info
      - cpu-stats

tunnel-server:
  address: ":57401"
  targets:
    - id: clab-arlab-spine1
    - id: clab-arlab-leaf1
    - id: clab-arlab-leaf2
```

</p>
</details></br>

A `gnmic` container will be started by default when running the [arista-ceos](../../labs/arista-ceos/topology.clab.yml) lab.

```yaml
gnmic:
  kind: linux
  mgmt-ipv4: 172.100.100.7
  image: ghcr.io/openconfig/gnmic:latest
  binds:
    - ./gnmic.yaml:/app/gnmic.yaml:ro
  ports:
    - 57401:57401
  cmd: "--config /app/gnmic.yaml --use-tunnel-server subscribe"
```

### Switch

Following configuration is required under the `management api gnmi` configuration mode.

```shell
management api gnmi
   transport grpc oob
   !
   transport grpc-tunnel tunnel1
      destination 172.100.100.7 port 57401
      local interface Management1
      target clab-arlab-spine1
   provider eos-native
```

