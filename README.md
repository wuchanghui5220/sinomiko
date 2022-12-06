# sinomiko
# A ssh client for MLNX_OS, cumuluslinux, linux server with python3.11

# download tar package 
链接：https://pan.baidu.com/s/1WJL19Rj_pl86fzIPYaqXYA 
提取码：xs0r 



# install doc
[link to install.md](https://github.com/wuchanghui5220/sinomiko/blob/main/Packages/install.md)

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
