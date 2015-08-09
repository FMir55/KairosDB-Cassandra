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
192.168.187.129 fmir55-virtual-machine
192.168.187.134 fmir77-virtual-machine
```


###For Seed(Main node)


###For Droplets(Rest of nodes)
