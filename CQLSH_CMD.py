'''
Created on 2015/7/12

@author: fmir55
'''
import cql
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')

con = cql.connect(host="127.0.0.1",port= 9160,  keyspace="nyc")

cursor = con.cursor()

select = "SELECT * FROM person;"
drop = "DROP TABLE person;"
create = "CREATE TABLE person(a text PRIMARY KEY,b text,c int,d text,e varint,f varint,g text,h text,i int,j text,k text,l int,m int,n int,o int,p varint,q int,r int,s int,t text,u text,v varint,w int,x int,y int);"
alter="ALTER TABLE person ADD z int;"

truncate="TRUNCATE person"

'''
create =  "create table eclipse(a text PRIMARY KEY,b int);"
insert = "INSERT INTO eclipse (a, b ) values('ddd',6);"
drop = "DROP TABLE eclipse;"
'''

cursor.execute(alter)







