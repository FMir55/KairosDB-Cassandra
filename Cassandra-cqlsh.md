#cqlsh
- (Cassandra query language shell)
- define a schema
- insert data
- execute a query

```
http://www.tutorialspoint.com/cassandra/cassandra_cqlsh.htm
```

###Creating a keyspace
```
CREATE KEYSPACE <identifier> WITH <properties>
```
```
CREATE KEYSPACE “KeySpace Name”
...WITH replication = {'class': ‘Strategy name’, 'replication_factor' : ‘No.Of  replicas’}
...(AND durable_writes = ‘Boolean value’); =====>default value is true
```
Ex:
```
cqlsh> CREATE KEYSPACE tutorialspoint
...WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3}
...AND DURABLE_WRITES = false;
```
###verify members of keyspaces
```
cqlsh> DESCRIBE keyspaces;
```
###verification with details
```
cqlsh> SELECT * FROM system.schema_keyspaces;
```
###Using a keyspace
```
USE <identifier>
```
Ex:
```
cqlsh> USE tutorialspoint;
```
###Alter keyspace
```
ALTER KEYSPACE <identifier> WITH <properties>
```
Ex:
```
ALTER KEYSPACE “KeySpace Name”
...WITH replication = {'class': ‘Strategy name’, 'replication_factor' : ‘No.Of  replicas’}
...(AND durable_writes = ‘Boolean value’);
```
###Drop/Delete keyspace
```
Drop KEYSPACE <identifier>
```
Ex:
```
Drop KEYSPACE tutorialspoint;
```
