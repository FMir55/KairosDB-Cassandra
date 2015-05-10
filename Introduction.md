# JAVA

###install the PPA update source
```
sudo gedit /etc/apt/sources.list.d/webupd8team-java-trusty.list
append>>deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main
        deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main
save & quit
```

###add the key to the apt system
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <key>
```
The signature key can be found on the PPA:
https://launchpad.net/~webupd8team/+archive/ubuntu/java

Click on the "Technical details about this PPA" and the key shows up. It looks like this at this time: 1024R/EEA14886, the key is the part after the slash; EEA14886 in this example. So the final command becomes:
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
```
Another way to find the key is to run the following command:
```
sudo apt-get update
```
and get the warning about the fact that the PPA is not trusted.

W: GPG error: http://ppa.launchpad.net trusty Release: the following signatures couldn't be verified because the public key is not available: NO_PUBKEY C2518248EEA14886

As you can see, the EEA14886 appears in this message. The key is exactly 8 hexadecimal digits.
```
sudo add-apt-repository ppa:webupd8team/java
```
This will automatically setup the key for you, but the deb definition is probably not at the right place. Just like the manual add, you have to run an update after the add:
```
sudo apt-get update
```

###install the packages
```
sudo apt-get install oracle-java8-installer
```

# Cassandra

###install the sources as defined
```
sudo vim /etc/apt/sources.list.d/cassandra.list
append>>deb http://www.apache.org/dist/cassandra/debian 20x main
        deb-src http://www.apache.org/dist/cassandra/debian 20x main
save & quit
```

###add the key
```
sudo apt-get update
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <key>
```

###install Cassandra
```
sudo apt-get install cassandra
```

###run Cassandra
```
sudo bin/cassandra -f 
(to run on foreground)
(use Ctrl + C to stop)
```

# KairosDB

###download & unpack
```
wget https://github.com/kairosdb/kairosdb/releases/download/v0.9.5beta2/kairosdb-0.9.5-0.2beta.tar.gz
ls
tar -xzf kairosdb-0.9.5-0.2beta.tar.gz
```

###Enable Cassandra
```
cd kairosdb/conf
gedit kairosdb.properties
comment out as:
                #kairosdb.service.datastore=org.kairosdb.datastore.h2.H2Module
uncomment as:
                kairosdb.service.datastore=org.kairosdb.datastore.cassandra.CassandraModule
```

### Start KairosDB
```
cd ..
cd bin
ls
sudo ./kairosdb.sh run 
(first time)
(this will run kairosdb in foreground)
(use Ctrl + C to stop)

OR
sudo ./kairosdb.sh start (this will run kairosdb in background)
sudo ./kairosdb.sh stop  (to stop kairosdb)
```

### Using UI
```
firefox=>       localhost:8080
```
