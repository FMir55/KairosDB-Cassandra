#Set up
####PPA Setting
```
sudo nano /etc/apt/sources.list
deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main
deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main
```
####Install JAVA
```
sudo apt-get install oracle-java8-installer
```
##Install the Cassandra
```
sudo nano /etc/apt/sources.list
deb http://www.apache.org/dist/cassandra/debian 20x main
deb-src http://www.apache.org/dist/cassandra/debian 20x main
```
```
sudo apt-get install cassandra
sudo bin/cassandra -f 
```
##Install the KairosDB
```
wget https://github.com/kairosdb/kairosdb/releases/download/v0.9.5beta2/kairosdb-0.9.5-0.2beta.tar.gz
tar -xzf kairosdb-0.9.5-0.2beta.tar.gz
```
####Enabling and configuring
```
cd kairosdb/conf
gedit kairosdb.properties
#kairosdb.service.datastore=org.kairosdb.datastore.h2.H2Module
kairosdb.service.datastore=org.kairosdb.datastore.cassandra.CassandraModule
```
```
cd kairosdb/bin
sudo ./kairosdb.sh run 
```
######
http://localhost:8080
```
cqlsh
```
