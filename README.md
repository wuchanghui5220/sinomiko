# sinomiko
# A ssh client for MLNX_OS, cumuluslinux, linux server with python3.8

# download tar package 
链接：https://pan.baidu.com/s/1RrkSs6K0Q8jIrFuHfDjaGg 
提取码：miko 


# install step :
	tar xf sinomiko-python3.8.tar.gz
	cp ./python3.8/sinomiko /usr/bin/sinomiko
	cp ./python3.8/python3.8 /usr/bin/python3.8
	cp ./python3.8/switch-ip.txt ./
	cp ./python3.8/switch-commands.txt ./
	mv ./python3.8 /usr/local/lib/

# example:
	sinomiko 192.168.1.202 -u admin -p admin -c "show health-report"
	
# use switch's ip address file AND commands file
	sinomiko switch-ip.txt -c switch-commands.txt 

# Mellanox switch's commands
	show hosts |include Hostname
	show interfaces mgmt0 configured |include "IP address"
	show version concise
	show voltage
	show power
	show fan
	show interfaces ib status |include LinkUp
	

# Enjoy!
