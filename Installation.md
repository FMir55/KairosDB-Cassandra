# Install Cassandra & KairosDB
- package install via apt-get
- Reference 
http://www.erol.si/2015/02/how-to-install-kairosdb-timeseries-database/



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

#Java
```
sudo apt-get install oracle-java8-installer
or
sudo apt-get install oracle-java7-installer
```


###run Cassandra
```
sudo bin/cassandra -f 
(to run on foreground)
(use Ctrl + C to stop)
```
or
```
sudo service cassandra start
sudo service cassandra stop
sudo service cassandra restart
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
