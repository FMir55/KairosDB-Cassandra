###Concept
- Linear Reliability
- Cluster means a group of nodes
- A cluster contains Data Centers
- Data Center is consists of racks
- A rack is grouped by a seed node and droplet nodes
- Generally,A rack has only 1 seed and at least 2 droplets.

###Sources
- https://snapwebsites.org/journal/2014/10/setting-cluster-cassandra-nodes
- http://posulliv.github.io/2009/09/07/building-a-small-cassandra-cluster-for-testing-and-development/
- http://docs.datastax.com/en/cassandra/2.0/cassandra/initialize/initializeSingleDS.html
- http://grepcode.com/file/repo1.maven.org/maven2/org.kairosdb/kairosdb/0.9.4/kairosdb.properties
- http://qnalist.com/questions/5646884/can-not-connect-with-cqlsh-to-something-different-than-localhost
- http://stackoverflow.com/questions/29121904/cassandra-cqlsh-connection-refused
- https://engineering.eventbrite.com/changing-the-ip-address-of-a-cassandra-node-with-auto_bootstrapfalse/
- http://linux.vbird.org/linux_server/0130internet_connect.php

###Warm up
Use the following cmd to get each inet address in each node
```
ifconfig
```

Further more,edit the the hosts file in etc directory
```
gedit /etc/hosts &
```

Assumning the fmir55-virtual-machine is seed node,others are droplet nodes

(First line is uneditable,or you will face problems.)
```
127.0.0.1       localhost
192.168.187.139 fmir55-virtual-machine
192.168.187.137 fmir66-virtual-machine
192.168.187.138 fmir77-virtual-machine
```

###For Seed(Main node)
Before edit the property file in /etc/cassandra/cassandra.yaml,stop cassandra & clear data
```
sudo service cassandra stop
sudo rm -rf /var/lib/cassandra/data/system/*

gedit /etc/cassandra/cassandra.yaml &
```

```
cluster_name: 'MyCassandraCluster'
auto_bootstrap: false
num_tokens: 256
seed_provider:
  - class_name: org.apache.cassandra.locator.SimpleSeedProvider
    parameters:
         - seeds: "192.168.187.139"
listen_address: fmir55-virtual-machine
rpc_address: fmir55-virtual-machine
endpoint_snitch: GossipingPropertyFileSnitch
```
Note that
 - cluster name must be identical between nodes
 - Seed nodes do not bootstrap, which is the process of a new node joining an existing cluster. 
  
   For new clusters, the bootstrap process on seed nodes is skipped.

 - By default seed parameter is set to 127.0.0.1 which means only the local node is used 
 
    (it does not try to connect to other nodes on other computers.)

 - rpc_address (or rpc_interface) is used for client connections,empty goes to localhost automatically  
 - listen_address is for inter-node communication,"192.168.187.129" or fmir55-virtual-machine

###For Droplets(Rest of nodes)
Before edit the property file in /etc/cassandra/cassandra.yaml,stop cassandra & clear data
```
sudo service cassandra stop
sudo rm -rf /var/lib/cassandra/data/system/*

gedit /etc/cassandra/cassandra.yaml &
```

```
cluster_name: 'MyCassandraCluster'
num_tokens: 256
seed_provider:
  - class_name: org.apache.cassandra.locator.SimpleSeedProvider
    parameters:
         - seeds: "192.168.187.139"
listen_address: fmir55-virtual-machine
rpc_address: fmirxx-virtual-machine (or 192.168.187.xxx)
endpoint_snitch: GossipingPropertyFileSnitch
```

###Start and Verify
Start
```
sudo service cassandra start
```
Check what interface the service is listening on
```
netstat -ntl | grep 9042
```

Note the Address with port 9042
```
cqlsh fmirxx-virtual-machine 
or
cqlsh 192.168.187.xxx 

exit
```

Nodetool
```
nodetool status
```
Make sure every nodes is on the list,the launched node will show 'UN' (Up Normal)

###KairosDB syn
Verify property 
```
gedit /opt/kairosdb/conf/kairosdb.properties &

Modify:
kairosdb.datastore.cassandra.host_list=fmir55-virtual-machine:9160,fmir66-virtual-machine:9160,fmir77-virtual-machine:9160

```
Start
```
sudo service kairosdb start

CHROME => localhost:8080
```
  
Notes:
  - Kairosdb can be exetuded perfectly only if every cassandra nodes in hosts_list in "UN" status 
  - Inet address may be changed when the terminal shell shut down or restart
  - use ifconfig & gedit /etc/host to update settings
