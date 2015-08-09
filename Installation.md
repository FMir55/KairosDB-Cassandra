# Install Cassandra & KairosDB
- package install via apt-get
- Reference 

http://www.erol.si/2015/02/how-to-install-kairosdb-timeseries-database/
http://www.desmondrduggan.com/2014/09/11/How-to_Install-Cassandra.html
https://snapwebsites.org/journal/2014/10/installation-instructions-get-cassandra-ubuntu


##Cassandra
###Preparation
source setting
```
sudo gedit /etc/apt/sources.list &
append>>
        deb http://www.apache.org/dist/cassandra/debian 21x main
        deb-src http://www.apache.org/dist/cassandra/debian 21x main
save & quit
```

add public keys to be able to access debian packages
```
gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
gpg --export --armor F758CE318D77295D | sudo apt-key add -
 
gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00
gpg --export --armor 2B5C1B00 | sudo apt-key add -
 
gpg --keyserver pgp.mit.edu --recv-keys 0353B12C
gpg --export --armor 0353B12C | sudo apt-key add -
```

###Install Cassandra
```
sudo apt-get update
sudo apt-get install cassandra
```

###Install Java
```
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:webupd8team/java
```
```
sudo apt-get update
sudo apt-get install oracle-java7-installer
```
```
sudo apt-get install oracle-java7-set-default
```


###run Cassandra
```
sudo service cassandra start
sudo service cassandra stop
sudo service cassandra restart
```

## KairosDB

###download & unpack
- First of all,link to the website to check the latest version : x.x.x-x
- https://github.com/kairosdb/kairosdb/releases
```
wget https://github.com/kairosdb/kairosdb/releases/download/vx.x.x/kairosdb_x.x.x-x_all.deb
sudo dpkg -i kairosdb_x.x.x-x_all.deb
```

###Enable Cassandra as used DATABASE
```
gedit /opt/kairosdb/conf/kairosdb.properties
comment out as:
                #kairosdb.service.datastore=org.kairosdb.datastore.h2.H2Module
uncomment as:
                kairosdb.service.datastore=org.kairosdb.datastore.cassandra.CassandraModule
```

### Start KairosDB
```
cd /opt/kairosdb/bin

sudo ./kairosdb.sh run 
(first time)
(this will run kairosdb in foreground)
(use Ctrl + C to stop)

sudo ./kairosdb.sh start (this will run kairosdb in background)
sudo ./kairosdb.sh stop  (to stop kairosdb)
```
or
```
sudo service kairosdb start
sudo service kairosdb stop
sudo service kairosdb restart
```

### Using UI
```
firefox/chrome=>       localhost:8080
```
