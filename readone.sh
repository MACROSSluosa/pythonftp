#!/bin/bash
## find the docs which is biger than 1MB
find . -type f -size +1000k > newdocs
## find the docs which is biger than 1M and created when  before [24h,0.5]
#find . -mtime 0  -mmin +30 -type f -size +1000k > > newdocs
filename='./newdocs'
i=0 #设置循环次数检查;当前发送文件个数
 > predocs
if [ -f ${filename} ];then
   while read line
   do
     arr=($line) #每一行的所有内容以空格为分割标记分成数组
	
	# grep ${arr[0]} ./okftp
 	string=${arr[0]}
#echo "${arr[0]} is string " 
#directoryname=${string:1:8}# 第2行到第9行 0-100
#	filename001=${string:9}#第十行到最后
#	echo $directoryname
#	echo $filename001
 if [ ${arr[0]} ];then ##除去空字符串的第一行
		if [ `grep  ${arr[0]}  ./histdocs` ]; then
			echo "${arr[0]} 文件已经传送"
		else
			echo "${arr[0]}文件未传送，即将写入待传送列表"
           echo ${arr[0]} >> predocs
		fi

	
	fi
	        #echo ${#arr[@]} #显示数组长度，每一行被分成了多少个数组
	i=$((i+1))

   done < ${filename}
fi
echo “本次文件传送回合总计检查文件个数为” $i 
