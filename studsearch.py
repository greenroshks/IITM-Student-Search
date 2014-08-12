import urllib2
import csv
import sys

dep=raw_input("Enter the department you want to search\t:")
url = "http://ccw.iitm.ac.in/?q=/IITMHostels/listbydept/"+dep # write the url here
hostel = raw_input("Enter the hostel you want to search\t:")
hostel_l = len(hostel)
usock = urllib2.urlopen(url)
data = usock.read()
usock.close()
html="<!doctype html><html><head><title>Quick Search</title><meta charset=\"utf-8\"/></head><body>"

i=0
cnt=0
while(i>=0):
    i=data.find(hostel,i+10)
    #print i
    #print "\n"
    subs=data[i-300:i+20]
    j=subs.find("\n")
   
    name= subs[j+140:j+183]
    roll=subs[j+78:j+89]
    k1=roll.find("<")
    l1=roll.find(">")
    k=name.find("<")
    l=name.find(">")
    print roll[l1+1:k1]+"\t"+name[l+1:k]+"\t"+data[i+hostel_l+9:i+hostel_l+12]+"\n"

    html=html+"<br>"+roll[l1+1:k1]+"........................"+name[l+1:k]+"<img src=\"http://photos.iitm.ac.in/byroll.php?roll="+roll[l1+1:k1].upper()+"\"width=\"252\" height=\"379\"><br>"
    cnt=cnt+1
print "\n\nThere are "+str(cnt)+" students"
f=open(dep,'w')
f.write(html)
f.close()
    
   

