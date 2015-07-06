# 1st data pouring
###create keyspace
```
cqlsh> CREATE KEYSPACE nyc WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 3} AND DURABLE_WRITES = true;
```

###Data types
```
date_id: varint
id:      varint
name:    text
measure: text
type_name:text
geo_id:  varint
entity_name:varint
year:    varint
value:   float
```

###create table
```
cqlsh> USE nyc;
cqlsh:nyc> CREATE TABLE emp(date_id varint PRIMARY KEY,id varint, name text,measure text,type_name text,geo_id varint,entity_name varint,year varint,value float);
cqlsh:nyc> select * from emp;
```

###copy from file
```
cqlsh:nyc> COPY emp (date_id,id,name,measure,type_name,geo_id,entity_name,year,value) FROM 'Air.xls';
cqlsh:nyc> select * from emp;
```
