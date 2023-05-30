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
	
# flint Firmware example
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

# Mellanox SN3700 交换机巡检报告

## 巡检基本信息

- 巡检人员：
- 巡检时间：
- 巡检周期：
- 巡检目的：

## 巡检设备信息

- 交换机型号：Mellanox SN3700
- 交换机序列号：
- 交换机位置：
- 交换机IP地址：
- 交换机端口数：32
- 交换机端口速率：200GbE
- 交换机总吞吐量：12.8Tb/s
- 交换机总处理能力：8.33Bpps

## 巡检内容和结果

### 硬件状态

|项目|内容|结果|备注|
|:--:|:--:|:--:|:--:|
|电源|检查电源是否正常工作|正常/异常||
|风扇|检查风扇是否正常工作|正常/异常||
|温度|检查温度是否在正常范围内|正常/异常||
|指示灯|检查指示灯是否显示正常状态|正常/异常||

### 系统运行状态

|项目|内容|结果|备注|
|:--:|:--:|:--:|:--:|
|系统版本|检查系统版本是否为最新版本|是/否||
|系统日志|检查系统日志是否有异常或错误信息|正常/异常||
|系统配置|检查系统配置是否符合预期或标准|正常/异常||
|系统性能|检查系统性能是否达到预期或标准|正常/异常||

### 端口状态

|端口号|连接设备类型|连接设备IP地址|端口速率|端口状态|
|:--:|:--:|:--:|:--:|:--:|
||||||

### 故障记录

记录本次巡检期间发现或处理的故障情况。

- 故障时间：
- 故障描述：
- 故障原因：
- 故障处理方法：
- 故障处理结果：

## 巡检总结和建议

总结本次巡检的主要发现和结论，提出改进或优化的建议。

