# gNMI Dial-out via gRPC Tunnel

- [gNMI Dial-out via gRPC Tunnel](#gnmi-dial-out-via-grpc-tunnel)
  - [Requirements](#requirements)
  - [Configuration](#configuration)
    - [Tunnel Server](#tunnel-server)
    - [Switch](#switch)
    - [Subscriptions on Tunnel Server](#subscriptions-on-tunnel-server)

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

### Subscriptions on Tunnel Server

Use the following commands to check the subscription states on the tunnel server

```shell
docker logs clab-arlab-gnmic -f
```

<details>
<summary>Reveal Output</summary>
<p>

```shell
$ docker logs clab-arlab-gnmic -f
2025/05/29 12:29:18.669172 [gnmic] version=0.41.0, commit=932a2403, date=2025-04-15T15:17:24Z, gitURL=https://github.com/openconfig/gnmic, docs=https://gnmic.openconfig.net
2025/05/29 12:29:18.669198 [gnmic] using config file "/app/gnmic.yaml"
2025/05/29 12:29:18.671529 [gnmic] starting output type file
2025/05/29 12:29:18.671844 [file_output:default-stdout] initialized file output: {"Name":"default-stdout","FileName":"","FileType":"stdout","Format":"json","Multiline":true,"Indent":"  ","Separator":"\n","SplitEvents":false,"OverrideTimestamps":false,"AddTarget":"","TargetTemplate":"","EventProcessors":null,"MsgTemplate":"","ConcurrencyLimit":1,"EnableMetrics":false,"Debug":false,"CalculateLatency":false,"Rotation":null}



2025/05/29 13:01:56.928005 [gnmic] tunnel server discovered target {ID:clab-arlab-spine1 Type:GNMI_GNOI}
2025/05/29 13:01:56.928148 [gnmic] adding target {"name":"clab-arlab-spine1","address":"clab-arlab-spine1","username":"admin","password":"****","timeout":10000000000,"insecure":true,"skip-verify":false,"buffer-size":100,"retry-timer":10000000000,"log-tls-secret":false,"gzip":false,"token":"","tunnel-target-type":"GNMI_GNOI"}
2025/05/29 13:01:56.928669 [gnmic] queuing target "clab-arlab-spine1"
2025/05/29 13:01:56.928689 [gnmic] starting target "clab-arlab-spine1" listener
2025/05/29 13:01:56.928736 [gnmic] subscribing to target: "clab-arlab-spine1"
2025/05/29 13:01:56.929441 [gnmic] target "clab-arlab-spine1" gNMI client created
2025/05/29 13:01:56.929550 [gnmic] dialing tunnel connection for tunnel target "clab-arlab-spine1"
2025/05/29 13:01:56.929456 [gnmic] sending gNMI SubscribeRequest: subscribe='subscribe:{subscription:{path:{elem:{name:"interfaces"}  elem:{name:"interface"  key:{key:"name"  value:"Management1"}}  elem:{name:"state"}  elem:{name:"counters"}  elem:{name:"in-octets"}}}  subscription:{path:{elem:{name:"interfaces"}  elem:{name:"interface"  key:{key:"name"  value:"Management1"}}  elem:{name:"state"}  elem:{name:"counters"}  elem:{name:"out-octets"}}}}', mode='STREAM', encoding='JSON', to clab-arlab-spine1
2025/05/29 13:01:56.930154 [gnmic] sending gNMI SubscribeRequest: subscribe='subscribe:{subscription:{path:{elem:{name:"system"}  elem:{name:"state"}  elem:{name:"software-version"}}}  subscription:{path:{elem:{name:"system"}  elem:{name:"state"}  elem:{name:"hostname"}}}  mode:ONCE}', mode='ONCE', encoding='JSON', to clab-arlab-spine1
2025/05/29 13:01:56.930200 [gnmic] sending gNMI SubscribeRequest: subscribe='subscribe:{subscription:{path:{origin:"eos_native"  elem:{name:"Kernel"}  elem:{name:"proc"}  elem:{name:"cpu"}  elem:{name:"utilization"}  elem:{name:"total"}}}}', mode='STREAM', encoding='JSON', to clab-arlab-spine1
2025/05/29 13:01:56.930226 [gnmic] sending gNMI SubscribeRequest: subscribe='subscribe:{subscription:{path:{origin:"eos_native"  elem:{name:"Kernel"}  elem:{name:"proc"}  elem:{name:"meminfo"}}}}', mode='STREAM', encoding='JSON', to clab-arlab-spine1
{
  "source": "clab-arlab-spine1",
  "subscription-name": "system-info",
  "timestamp": 1748521797597557966,
  "time": "2025-05-29T12:29:57.597557966Z",
  "updates": [
    {
      "Path": "system/state/software-version",
      "values": {
        "system/state/software-version": "4.34.0F-41641815.4340F (engineering build)"
      }
    }
  ]
}
{
  "source": "clab-arlab-spine1",
  "subscription-name": "system-info",
  "timestamp": 1748522109407437559,
  "time": "2025-05-29T12:35:09.407437559Z",
  "updates": [
    {
      "Path": "system/state/hostname",
      "values": {
        "system/state/hostname": "DC1_SPINE1"
      }
    }
  ]
}
{
  "sync-response": true
}
{
  "sync-response": true
}
{
  "sync-response": true
}
{
  "source": "clab-arlab-spine1",
  "subscription-name": "port-stats",
  "timestamp": 1748523716597093569,
  "time": "2025-05-29T13:01:56.597093569Z",
  "prefix": "interfaces/interface[name=Management1]/state/counters",
  "updates": [
    {
      "Path": "in-octets",
      "values": {
        "in-octets": 286932
      }
    },
    {
      "Path": "out-octets",
      "values": {
        "out-octets": 317739
      }
    }
  ]
}
```

</p>
</details></br>
