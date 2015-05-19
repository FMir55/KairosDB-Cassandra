#cqlsh
- (Cassandra query language shell)
- define a schema
- insert data
- execute a query

```
http://www.tutorialspoint.com/cassandra/cassandra_cqlsh.htm
```
```
    index(?)    =>    table/column family   =>        keyspace
                 with a primary key & column
```

##Keyspace
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
```
ALTER KEYSPACE “KeySpace Name”
...WITH replication = {'class': ‘Strategy name’, 'replication_factor' : ‘No.Of  replicas’}
...(AND durable_writes = ‘Boolean value’);
```
Ex:
```
cqlsh> ALTER KEYSPACE tutorialspoint
...WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3}
...AND DURABLE_WRITES = false;
```
###Drop/Delete keyspace
```
Drop KEYSPACE <identifier>
```
Ex:
```
Drop KEYSPACE tutorialspoint;
```

##table/columnfamilies
###creating a table
```
CREATE TABLE tablename(
   column1 name datatype PRIMARYKEY,
   column2 name data type,
   column3 name data type
   );
```
Ex:
```
cqlsh> USE tutorialspoint;
cqlsh:tutorialspoint> CREATE TABLE emp(
   emp_id int PRIMARY KEY,
   emp_name text,
   emp_city text,
   emp_sal varint,
   emp_phone varint
   );
```
###verification
```
cqlsh:tutorialspoint> select * from emp;
```
###altering a table(ADD & DROP the columns)
```
ALTER TABLE table name
ADD  new column datatype;
DROP column name;
```
Ex:
```
cqlsh> USE tutorialspoint;
cqlsh:tutorialspoint> ALTER TABLE emp
   ... ADD emp_email text,
   ... DROP emp_sal;
```
###verification
```
cqlsh:tutorialspoint> select * from emp;
```
###drop a table
```
DROP TABLE <tablename>
```
Ex:
```
cqlsh> USE tutorialspoint;
cqlsh:tutorialspoint> DROP TABLE emp;
```
###verification
```
cqlsh:tutorialspoint> select * from emp;
```

###truncate a table
清空table內所有column(n rows => 0 row)
```
TRUNCATE TABLE <tablename>
```
Ex:
```
cqlsh> USE tutorialspoint;
cqlsh:tutorialspoint> TRUNCATE emp;
```
###verification
```
cqlsh:tutorialspoint> select * from emp;
```

##index
###creating/dropping a index
```
CREATE INDEX <identifier> ON <tablename>
DROP INDEX <identifier>
```
Ex:
```
cqlsh:tutorialspoint> CREATE INDEX name ON emp (emp_name);
cqlsh:tutorialspoint> DROP INDEX name;
```

##BATCH
植入、刪減TABLE內資料
###creating/dropping a index
```
BEGIN BATCH
<insert-stmt>/ <update-stmt>/ <delete-stmt>
APPLY BATCH;
```
Ex:
```
cqlsh:tutorialspoint> BEGIN BATCH
... INSERT INTO emp (emp_id, emp_city, emp_name, emp_phone, emp_sal)
    values(  4,'Pune','rajeev',9848022331, 30000);
... UPDATE emp SET emp_sal = 50000 WHERE emp_id =3;
... DELETE emp_city FROM emp WHERE emp_id = 2;
... APPLY BATCH;
```
###verification
```
cqlsh:tutorialspoint> select * from emp;
```
