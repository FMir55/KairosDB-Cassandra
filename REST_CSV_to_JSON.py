#coding=utf-8
'''
Created on 2015/7/19

@author: fmir55
'''
import requests
import json
import sys
import csv
import time
import datetime

def delete_matric(Name):
    url = 'http://localhost:8080/api/v1/metric/'+Name
    r = requests.delete(url)
    if r.status_code != 204:
        print sys.exc_info()
    else:
        print "Successfully deleted metric:",Name
    
def make_query(Name):
    myQuery={"start_absolute":1,"metrics":[{"name":Name}]}
    return json.dumps(myQuery)
    
def post_metric(JSON,Name):
    headers = {'content-type': 'application/json'}
    url = 'http://localhost:8080/api/v1/datapoints'
    r = requests.post(url, data=JSON, headers=headers)
    if r.status_code != 204:
        print sys.exc_info()
    else:
        print "Successfully added new metric:",Name
        
def get_metric(Query):
    headers = {'content-type': 'application/json'}
    url = 'http://localhost:8080/api/v1/datapoints/query'
    r = requests.post(url, data=Query, headers=headers)
    sample_size = r.json()['queries'][0]['sample_size']
    results = r.json()['queries'][0]['results'][0]
    print "Sample size: {0}\nResults:".format(sample_size)
    for key in results.keys():
        print key, ":", results[key]                

def truncate_metric(Query,Name):
    headers = {'content-type': 'application/json'}
    url = 'http://localhost:8080/api/v1/datapoints/delete'
    r = requests.post(url, data=Query, headers=headers)
    if r.status_code != 204:
        print sys.exc_info()
    else:
        print "Successfully truncated metric:",Name

def csv_to_json_TS(Path,Name,TS,Value):
    myfo = open(Path, 'r')
    myDatapoints=[]
    for wkRow in csv.DictReader(myfo):
        myDatapoints.append([int(wkRow[TS]),int(wkRow[Value])])
    myData=[{'name':Name,'datapoints':myDatapoints,'tags':{'host':'FMir55'}}]
    myfo.close()  
    return json.dumps(myData)

def csv_to_json_Year(Path,Name,TS,Value):
    myfo = open(Path, 'r')
    myDatapoints=[] 
    for wkRow in csv.DictReader(myfo):
        wkTS=time.strptime(wkRow[TS],'%Y')
        myDatapoints.append([int(time.mktime(wkTS))*1000,int(wkRow[Value])])
    myData=[{'name':Name,'datapoints':myDatapoints,'tags':{'host':'FMir55'}}]
    myfo.close()  
    return json.dumps(myData)

def csv_to_json_Month(Path,Name,TS,TS2,Value,Tag):
    myfo = open(Path, 'r')
    myDatapoints=[] 
    i=1
    for wkRow in csv.DictReader(myfo):
        if wkRow[Value]!='' :
            wkTS=time.strptime(wkRow[TS]+'/'+wkRow[TS2],'%Y/%m')
            if int(time.mktime(wkTS))<0:
                break
            myDatapoints.append([int(time.mktime(wkTS))*1000,int(wkRow[Value])])
        print i
        i=i+1
        if i==919:
            break
    myData=[{'name':Name,'datapoints':myDatapoints,'tags':{'Type':Tag}}]
    myfo.close()  
    return json.dumps(myData)

def csv_to_json_Day(Path,Name,TS,Value,Tag):
    myfo = open(Path, 'r')
    myDatapoints=[] 
    i=1
    for wkRow in csv.DictReader(myfo):
        if wkRow[Value]!='' :
            wkTS=time.strptime(wkRow[TS],'%m/%d/%Y')
            if int(time.mktime(wkTS))<0:
                break
            myDatapoints.append([int(time.mktime(wkTS))*1000,float(wkRow[Value])])
        print i
        i=i+1
        #if i==919:
            #break
    myData=[{'name':Name,'datapoints':myDatapoints,'tags':{'Type':Tag}}]
    myfo.close()  
    return json.dumps(myData)

def csv_to_json_Minute(Path,Name,TS,TS2,Value,Tag):
    myfo = open(Path, 'r')
    myDatapoints=[] 
    i=1
    Name=Name+'2'
    for wkRow in csv.DictReader(myfo):
        if wkRow[Value]!='':
            wkTS=time.strptime(wkRow[TS]+' '+wkRow[TS2],'%m/%d/%Y %H:%M')
            myDatapoints.append([int(time.mktime(wkTS))*1000,float(wkRow[Value])])
        print i
        i=i+1
        if i==129232:
            break
    myData=[{'name':Name,'datapoints':myDatapoints,'tags':{'Hurts':Tag}}]
    myfo.close()  
    return json.dumps(myData)

def csv_to_json_Second(Path,Name,TS,Value,Tag):
    myfo = open(Path, 'r')
    myDatapoints=[] 
    i=1
    for wkRow in csv.DictReader(myfo):
        if wkRow[Value]!='':
            wkTS=time.strptime(wkRow[TS],'%Y-%m-%d %H:%M:%S')
            if int(time.mktime(wkTS))<0:
                break
            myDatapoints.append([int(time.mktime(wkTS))*1000,float(wkRow[Value])])
        print i
        i=i+1
        if i==15655:
            break
    myData=[{'name':Name,'datapoints':myDatapoints,'tags':{'Type':Tag}}]
    myfo.close()  
    return json.dumps(myData)



#Elements

cvPath='/mnt/hgfs/下載/trip_fare_1.csv'
cvName=cvPath.split('/')[4].split('.')[0]
cvTS=' pickup_datetime'
cvValue=' total_amount'

#post Second

cvTS2=''
cvJSON = csv_to_json_Second(cvPath,cvName,cvTS,cvValue,cvValue)
post_metric(cvJSON,cvName)


#post Minute
'''
cvTS2='TIME'
cvJSON = csv_to_json_Minute(cvPath,cvName,cvTS,cvTS2,cvValue,cvValue)
post_metric(cvJSON,cvName)
'''

#post DAY
'''
cvJSON = csv_to_json_Day(cvPath,cvName,cvTS,cvValue,cvValue)
post_metric(cvJSON,cvName)
'''

#post Month
'''
cvTS2='Month'
cvJSON = csv_to_json_Month(cvPath,cvName,cvTS,cvTS2,cvValue,cvValue)
post_metric(cvJSON,cvName)
'''

#post Year
'''
cvJSON = csv_to_json_Year(cvPath,cvName,cvTS,cvValue)
post_metric(cvJSON,cvName)
'''

#post Timestamp
'''
cvJSON = csv_to_json_TS(cvPath,cvName,cvTS,cvValue)
post_metric(cvJSON,cvName)
'''

#view 

cvQuery=make_query(cvName)
get_metric(cvQuery)


#truncate
'''
cvQuery=make_query(cvName)
truncate_metric(cvQuery,cvName)
'''

#delete
'''
delete_matric(cvName)
'''

