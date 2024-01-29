# Intro-demo

This demo lab has the following multi-vendor topology:

1. Arista cEOS-Lab (ceos)
2. Nokia SR Linux (srl)

```shell
      ┌───────────┐                       ┌───────────┐
      │           │ eth1             e1-1 │           │
      │   ceos    ├───────────────────────┤    srl    │
      │           │                       │           │
      └───────────┘                       └───────────┘
```

The lab nodes are pre-configured with layer-3 interface and BGP configuration to bring up iBGP sessions between the nodes.

## Requirements

* Following docker images to be installed

```shell
$ docker images | egrep "IMAGE|ceos|srlinux"

REPOSITORY               TAG          IMAGE ID       CREATED         SIZE
ceosimage                4.30.1F      72e796e3929e   3 weeks ago     2.44GB
ghcr.io/nokia/srlinux    22.11.2      9381f04f8777   11 months ago   2.66GB
```

### Arista cEOS-Lab image

* Download the image from [www.arista.com](http://www.arista.com/) > Software Downloads > cEOS-Lab > EOS-4.2x.y > cEOS-lab-4.2x.y.tar.xz
* Copy the cEOS-lab-4.2x.y.tar.xz to the host/server/VM.
* Next, use the `docker import` command to import the cEOS-Lab image. For example

```shell
docker import cEOS64-lab-4.30.1F.tar.xz ceosimage:4.30.1F
```

### SR Linux image

```shell
docker pull ghcr.io/nokia/srlinux
```

## Deploying the lab

Use the following command to deploy the lab

```shell
cd openconfig-labs/phase-1/multi_vendor_lab

sudo containerlab deploy -t topology.yml
```

To view the deployed nodes use the following command:

```shell
sudo containerlab inspect -t topology.yml
```

## Logging into the nodes

Nokia SR Linux

```shell
docker exec -it clab-srlceoslab-srl sr_cli 
```

Arista cEOS-Lab

```shell
docker exec -it clab-srlceoslab-ceos Cli
```

### CLI Commands

Nokia SR Linux

```shell
show version
show system lldp neighbor
show network-instance default protocols bgp neighbor
show network-instance default route-table
```

Arista cEOS-Lab

```shell
show version
show lldp neighbors
show ip bgp summary
show ip route
```

### JSON-RPC Examples

Nokia SR Linux

```shell
cd openconfig-labs/phase-1/intro_demo

curl -s 'http://admin:NokiaSrl1!@172.100.100.2/jsonrpc' -d @labfiles/srl-json-req.json | python3 -m json.tool
```

Arista cEOS-Lab

```shell
curl -k -X POST https://admin:admin@172.100.100.3/command-api -H "Content-Type: text/json" -d @labfiles/ceos-json-req.json | python3 -m json.tool
```

### OpenConfig Examples

Arista cEOS-Lab

```shell
gnmic -a 172.100.100.3:6030 -u admin -p admin --insecure get --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'
```
