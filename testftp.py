#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from ftplib import FTP
import sys,getpass,os.path,os,time
#host = '202.43.149.133'
host = '172.16.139.33'
username = 'ftptest'
password = '1234qwer'
#username = 'sda' 
#password = '8U3YBoxU'
port = 21
timeout = 30 

localfile0 = '/Users/mac/pythoncode/'

#localfile2 = localfile0 + localfile1 ## meger the CMD
localfile2 = ''
remotepath0 = '/shandong/test/'

def ftpsend0(directory,filename):
    ##
      localfile2 = localfile0 + directory + '/' + filename
      remotepath2 = remotepath0 + directory
      f = FTP()
      f.connect(host,port,timeout)
      f.login(username,password)
      f.set_pasv(True)
      try:
            f.cwd(remotepath2)
      except: 
            f.cwd('/shandong/test')
            f.mkd(directory)
            f.cwd(remotepath2)
              
         #f.cwd(remotepath2)
      file1 = open(localfile2,'rb')

      f.storbinary('STOR %s' % os.path.basename(localfile2),file1)
      #f.storbinary('STOR ' + localfile2, file1)
      #f.storbinary('STOR %s'%(localfile2),open(localfile2,'rb'))

      file1.close()
      f.quit()
      return 3


if __name__ == "__main__":
   #print(remotepath2)
  while True:
        
      status0 = os.system('/Users/mac/pythoncode/readone.sh')
      statuspre = os.system('/Users/mac/pythoncode/histprepare.sh')
      #status1 = ftpsend0()
      #print (status0)
      file0 = open('/Users/mac/pythoncode/predocs')
      while True:
            line = file0.readline()
            #print(len(line))
            if not line: break
            #process(line) ##what is this ?
            directory = line[2:8]
            filename = line[9:43]
            #localfile2 = localfile0 + directory + '/' + filename
            remotepath2 = remotepath0 + directory
            print(remotepath2)
            #print(filename)
            #print(directory)
            status1 = ftpsend0(directory,filename)

            if (status1 == 3):
                  file3 = open('/Users/mac/pythoncode/okdocs','w')
                  file3.write(line)
                  file3.close()
                  statushist = os.system('/Users/mac/pythoncode/cpoktohist.sh')

      file0.close()
      time.sleep(60)
    


   

