# sinomiko
# A ssh client for MLNX_OS, cumuluslinux, linux server with python3.8

# download tar package 
链接：https://pan.baidu.com/s/1WJL19Rj_pl86fzIPYaqXYA 
提取码：xs0r 



# install 
	## install independence

	yum install gcc -y
	yum install zlib zlib-devel -y

	########################################################## 
	####             install openssl                      ####
	##########################################################

	## download openssl file

	 wget --no-check-certificate https://www.openssl.org/source/openssl-1.1.1s.tar.gz
	 tar xf openssl-1.1.1s.tar.gz
	 cd openssl-1.1.1s

	## config and  install

	 ./config --prefix=/usr/local/openssl --openssldir=/usr/local/openssl no-ssl2

	 make 
	 make install


	## verify openssl
	# whereis openssl
	openssl: /usr/bin/openssl /usr/lib64/openssl /usr/local/openssl /usr/share/man/man1/openssl.1ssl.gz



	########################################################## 
	####             install python                       ####
	########################################################## 

	## download python file

	wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tar.xz
	tar xf Python-3.11.0.tar.xz
	cd Python-3.11.0

	## modify file:  Modules/Setup
	sed -i '219,221 s/#//g' Modules/Setup


	vim Modules/Setup
	# OpenSSL bindings
	#_ssl _ssl.c $(OPENSSL_INCLUDES) $(OPENSSL_LDFLAGS) $(OPENSSL_LIBS)
	#_hashlib _hashopenssl.c $(OPENSSL_INCLUDES) $(OPENSSL_LDFLAGS) -lcrypto

	# To statically link OpenSSL:
	 _ssl _ssl.c $(OPENSSL_INCLUDES) $(OPENSSL_LDFLAGS) \
	     -l:libssl.a -Wl,--exclude-libs,libssl.a \
	     -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a
	# _hashlib _hashopenssl.c $(OPENSSL_INCLUDES) $(OPENSSL_LDFLAGS) \
	#     -l:libcrypto.a -Wl,--exclude-libs,libcrypto.a


	## configure and install

	./configure --with-openssl=/usr/local/openssl
	make 
	make install


	## verify python and import ssl for check

	[root@sinomiko sinomiko]# python3.11
	Python 3.11.0 (main, Dec  5 2022, 11:33:08) [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
	Type "help", "copyright", "credits" or "license" for more information.
	>>> import ssl
	>>> exit()




	########################################################## 
	####            pip3 install netmiko                  ####
	########################################################## 

	## install all whl files

	pip3 install *.whl
	
	# OR install netmiko online ,Github link:  https://github.com/ktbyers/netmiko
	pip3 install netmiko
	



# example MLNX_OS :
	sinomiko.py 192.168.1.202 -u admin -p admin -c "show health-report"
	
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
	
# For linux server
	hostname
	uname -r
	
# For linux server with Mellanox adapter
	# check PN and SN
	lspci -vvvxxx -s `lspci |grep Mellanox |awk '{print $1}'` |egrep "SN|PN"
	
	# show pci device line $1 or line $2
	lspci -vvvxxx -s `lspci |grep Mellanox |awk '{print $1}'` 
	
	# show mellanox adapter devices
	lspci |grep Mellanox
	
	# query PSID
	mstflint -d `lspci |grep Mellanox |awk '{print $1}'` q
	
	# Firmware Downloads
	https://network.nvidia.com/support/firmware/firmware-downloads/
	
	ofed_info -s
	sysinfo-snapshot.py
	sminfo
	smpquery nd <lid>
	saquery -s
	mlnx_tune
	mlxlink -d mlx5_0 -m
	
# flint Firmware
# A example
	[root@host13 ~]# mst start
	Starting MST (Mellanox Software Tools) driver set
	Loading MST PCI module - Success
	Loading MST PCI configuration module - Success
	Create devices
	Unloading MST PCI module (unused) - Success

	[root@host13 ~]# mst status
	MST modules:
	------------
	    MST PCI module is not loaded
	    MST PCI configuration module loaded


	MST devices:
	------------
	/dev/mst/mt4123_pciconf0         - PCI configuration cycles access.
					   domain:bus:dev.fn=0000:b1:00.0 addr.reg=88 data.reg=92 cr_bar.gw_offset=-1
					   Chip revision is: 00

	[root@host13 ~]# flint -d /dev/mst/mt4123_pciconf0 -i /root/fw-ConnectX6-rel-20_29_1016-MCX653105A-ECA_Ax-UEFI-14.22.14-FlexBoot-3.6.204.bin b


	    Current FW version on flash:  20.32.1010
	    New FW version:               20.29.1016


	    Note: The new FW version is older than the current FW version on flash.


	Do you want to continue ? (y/n) [n] : y


	FSMST_INITIALIZE -   OK
	Writing Boot image component -   OK
	-I- To load new FW run mlxfwreset or reboot machine.
	[root@host13 ~]# reboot
	
# Enjoy!
