# Demo-1

This demo lab has the following basic topology, an Arista cEOS-Lab node connected via a point-to-point ethernet link to a Nokia SR Linux node.

```shell
ceos[eth1] <--> [e1-1]srl
```

The lab nodes are pre-configured with layer-3 interface and BGP configuration to bring up an iBGP session between the two nodes.

## Deploying the lab

Use the following command to deploy the lab

```shell
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
curl -s 'http://admin:NokiaSrl1!@172.100.100.2/jsonrpc' -d @labfiles/srl-json-req.json | python3 -m json.tool
```

Arista cEOS-Lab

```shell
curl -k -X POST https://admin:admin@172.100.100.3/command-api -H "Content-Type: text/json" -d @labfiles/ceos-json-req.json | python3 -m json.tool
```

### OpenConfig Examples

Nokia SR Linux

```shell
```

Arista cEOS-Lab

```shell
gnmic -a 172.100.100.3:6030 -u admin -p admin --insecure get --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'
```
