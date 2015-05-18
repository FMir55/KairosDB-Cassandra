##NoSQLDatabase
  - highly scalable(高擴展性)
  - high-performance distributed
  - NoSQL (Not Only SQL) database
      simplicity of design
      horizontal scaling
      finer control over availability.
      Ex:Hbase,MongoDB
      
                      'Relational Database'	                                  'NoSql Database'
                 Supports powerful query language.	                 Supports very simple query language.
                     It has a fixed schema.	                                  No fixed schema.
                        Follows ACID .                              	It is only “eventually consistent”.
                     Supports transactions.                         	Does not support transactions.
                     
                     *ACID:(Atomicity, Consistency, Isolation, and Durability)
##Apache Cassandra
 - open source 
 - distributed and decentralized
 - no single point of failure
    
### Notable points

 - It is scalable, fault-tolerant, and consistent.
 
 - It is a column-oriented database.
 
 - Its distribution design is based on Amazon’s Dynamo and its data model on Google’s Bigtable.
 
 - Created at Facebook, it differs sharply from relational database management systems.
 
 - Cassandra implements a Dynamo-style replication model with no single point of failure, but adds a more powerful “column family” data model.
 
 - Cassandra is being used by some of the biggest companies such as Facebook, Twitter, Cisco, Rackspace, ebay, Twitter, Netflix, and more.
    
### Feature
 - Elastic scalability - 
    Cassandra is highly scalable; it allows to add more hardware to accommodate more customers and more data as per requirement.

 - Always on architecture - 
    Cassandra has no single point of failure and it is continuously available for business-critical applications that cannot afford a failure.

 - Fast linear-scale performance - 
    Cassandra is linearly scalable, i.e., it increases your throughput as you increase the number of nodes in the cluster. Therefore it maintains a quick response time.

 - Flexible data storage - 
    Cassandra accommodates all possible data formats including: structured, semi-structured, and unstructured. It can dynamically accommodate changes to your data structures according to your need.

 - Easy data distribution - 
    Cassandra provides the flexibility to distribute data where you need by replicating data across multiple data centers.

 - Transaction support - 
    Cassandra supports properties like Atomicity, Consistency, Isolation, and Durability (ACID).

 - Fast writes - 
    Cassandra was designed to run on cheap commodity hardware. It performs blazingly fast writes and can store hundreds of terabytes of data, without sacrificing the read efficiency.

```
data => node => data center => cluster
```
