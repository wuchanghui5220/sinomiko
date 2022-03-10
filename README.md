# sinomiko
# A ssh client for MLNX_OS, cumuluslinux, linux server with python3.8

# download tar package 
# 链接：https://pan.baidu.com/s/16aW_2LMNTdS8ZzCKcq-tFw 
# 提取码：9ky1 

# install step :
	tar xf sinomiko-python3.8.tar.gz
	cp ./python3.8/sinomiko /usr/bin/sinomiko
	cp ./python3.8/python3 /usr/bin/python3
	mv ./python3.8 /usr/local/lib/

# example:
	sinomiko 192.168.1.202 -u admin -p admin -c "show health-report"

# Enjoy!
