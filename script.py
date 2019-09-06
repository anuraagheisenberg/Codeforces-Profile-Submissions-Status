#test
import requests
import re
from bs4 import BeautifulSoup
from requests.auth import HTTPProxyAuth
import MySQLdb
import sys,json
import sys
def tsp():
	url="http://codeforces.com/api/user.status?handle=";
	url2="&from=1&count=1000000";
	#cursor=db.cursor()
	k=raw_input();
	url=url+k+url2;
	session = requests.Session()
	session.trust_env = False
	source_code = session.get(url)
	print "Status Code(Id Exists or not)="+str(source_code.status_code);
	k=source_code.text
	p=k.encode('utf-8').split(',')
	ac=0
	re=0
	wa=0
	ce=0
	tle=0
	flag=0
	s1=""
	s2=""
	answer=[];
	for i in p:
		k=i
		if(flag==1):
			answer.append(s1);
			s1=""
			flag=0;
		if(k[1:8]=="problem"):
			s1+=k[-3:]
		if(k[1:6]=="index"):
			s1+=k[-2]
		'''if(k[1:5]=="name"):
			s1+="  "+k[8:-1]'''
		if(k[1:8]=='verdict'):
			s3=k[11:-1]
			if(s3=='OK'):
				ac+=1;
				flag=1
			elif(s3=="WRONG_ANSWER"):
				wa+=1
				s1=''
			elif(s3=='COMPILATION ERROR'):
				ce+=1
				s1=''
			elif(s3=='TIME_LIMIT_EXCEEDED'):
				tle+=1
				s1=''
			else:
				re+=1
				s1=''	
	ts=int(re)+int(tle)+int(ac)+int(wa);
	wap=wa/(ts*1.0)*100;
	wap=float("{0:.2f}".format(wap))
	tlep=tle/(ts*1.0)*100;
	tlep=float("{0:.2f}".format(tlep))
	rep=re/(ts*1.0)*100;
	rep=float("{0:.2f}".format(rep))
	acp=ac/(ts*1.0)*100;
	acp=float("{0:.2f}".format(acp))
	print "Total Submittions ="+str(ts);
	print "Wrong Answers ="+str(wa)+" ("+str(wap)+"%)";
	print "Accepted Answers ="+str(ac)+" ("+str(acp)+"%)";
	print "Time Limit Exceed ="+str(tle)+" ("+str(tlep)+"%)";
	print "Runtime Error ="+str(re)+" ("+str(rep)+"%)";
				
	'''for i in answer:
		flag=0
		#print i;
		query='Select qid from questions where id=\''+i+'\';'
		qid=0;
		#print query
		try:
			cursor.execute(query);
			result=cursor.fetchall();
			#print result
			for row in result:
				qid=row[0];
		except:
			qid=-1;
		if(qid>0):
			queryc='Select uid from solved where qid='+str(qid)+';';
			try:
				
				cursor.execute(queryc);
				result = cursor.fetchall();
				uid2=0
				for row in result:
					uid2=row[0]
				#print uid2
				if(uid2==uid):
					flag=1
			except:
				flag=1;
			if(flag==0):
				query='Insert into solved(qid,uid) Values('
				query+=str(qid)+","+str(uid)+");";
				#print query
				try:
					cursor.execute(query);
					#print "inserted"
					db.commit();
				except:
					#print "not inserted"	
					db.rollback();
			else:
				p=1
				#print "already present"
	#for accuracy
	query2='Update users set accuracy='+str(acp)+',wronganswers='+str(wap)+',runtimeerror='+str(rep)+',timeexceed='+str(tlep)+"where uid="+str(uid);
	try:
		cursor.execute(query2);
		db.commit();
	except:
		db.rollback();'''
tsp();
