from netmiko import ConnectHandler
from datetime import datetime
# import paramiko
import argparse
import os
import threading
import time



def mlnxClient(host, user, password):
    mlnx_os = {
            "device_type": "mellanox_mlnxos",
            "host": host,
            "username": user,
            "password": password,
            }
    net_connect = ConnectHandler(**mlnx_os)
    net_connect.enable()
    return net_connect


def mlnxExecute(mlnxClient, commands):
    output = ""
    prompt = mlnxClient.find_prompt() + " "
    for c in commands:
        output += prompt + c + "\n"
        output += mlnxClient.send_command(c)

    return output


def linuxClient(host, user, password):
    linux_os = {
            "device_type": "linux",
            "host": host,
            "username": user,
            "password": password,
            }
    net_connect = ConnectHandler(**linux_os)
    return net_connect


def linuxExecute(linuxClient, commands):
    output = ""
    prompt = linuxClient.find_prompt() + " "
    for c in commands:
        output += prompt + c + "\n"
        output += linuxClient.send_command(c)
        output += "\n"
    return output


def cumulusLinuxClient(host, user, password):
    cumulus_os = {
            "device_type": "linux",
            "host": host,
            "username": user,
            "password": password,
            }
    net_connect = ConnectHandler(**cumulus_os)
    return net_connect


def cumulusLinuxExecute(cumulusLinuxClient, commands):
    output = ""
    prompt = cumulusLinuxClient.find_prompt() + " "
    for c in commands:
        output += prompt + c + "\n"
        output += cumulusLinuxClient.send_command(c)
        output += "\n"
    return output



def unique_generator(things):
    visited = set()
    for thing in things:
        if thing in visited:
            continue
        visited.add(things)
        yield thing


def do_commands(host, user, password, commands):
    Type = ""
    output = ""
    try:
        if user == "cumulus":
            Type += "cumulus"
            client = cumulusLinuxClient(host, user, password)
        elif user == "admin":
            Type += "mlnx"
            client = mlnxClient(host, user, password)
        else:
            Type += "linux"
            client = linuxClient(host, user, password)
    except:
        print("\033[31mError: Unable to connect to host: " + host +
              "\033[0m\nPlease check whether the ip address, user name or password is correct.\n")
    else:
        # print("\033[32mSuccessfully connected to the host: " + host + "\033[0m")
        if Type == "cumulus":
            output += cumulusLinuxExecute(client, commands)
        elif Type == "mlnx":
            output += mlnxExecute(client, commands)
        elif Type == "linux":
            output += linuxExecute(client, commands)
    print(output)
    return output

def sftp_trans(hostname, user, password, sysdump_file):
    transport = paramiko.Transport(hostname, 22)
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get('/var/opt/tms/sysdumps/' + sysdump_file, sysdump_file)
    transport.close()


def generate_sysdump(host, user, password):
    commands = ["debug generate dump"]
    sysdump_file = ""
    try:
        client = mlnxClient(host, user, password)
    except:
        print("\033[31;1mError: Unable to connect to host: " + host + "\n\033[0mPlease check whether the ip address, user name or password is correct.")
    else:
        print("\033[32;1mSuccessfully connected to the host: " + host + "\n\033[0mGenerating a new sysdump file may take up to 4 minutes.")

        result = mlnxExecute(client, commands)
        with open(".sysdump.log", 'w') as f:
            f.write(result)
        if result:
            for line in unique_generator(open(".sysdump.log")):
                if line.find("Generated dump") != -1:
                    sysdump_file = line.rstrip("\n").split()[-1]
            print(result)
            #print(sysdump_file)
            print("Downloading sysdump file ... ... ")
            sftp_trans(host, user, password, sysdump_file)
            print("Done!")
        else:
            print(result)

if __name__ == "__main__":
    start = datetime.now()
    parser = argparse.ArgumentParser(description='Author: wuchanghui@infohpc.com')
    parser.add_argument('hostname', help="Hostname or ip address", nargs="+", type=str)
    parser.add_argument('-u', help="Switch's login user", nargs="?", const="cumulus", default="admin", type=str)
    parser.add_argument('-p', help="Switch's login password", nargs="?", const="CumulusLinux!", default="admin", type=str)
    parser.add_argument('-c', help="The commands to run. ex: 'show version; show inventory'", default="\n", type=str)
    parser.add_argument('-e', help="Generate sysdump, and download to remote server.", nargs="?", const="yes", default="no", type=str)
    args = parser.parse_args()

    if args.e != "no":
        ip = []
        if os.path.isfile(args.hostname[0]):
            with open(args.hostname[0], 'r') as f:
                lines = f.readlines()
            ip.extend(lines)
        else:
            ip = (args.hostname)
        threads = []
        for i in range(len(ip)):
            threads.append(threading.Thread(target=generate_sysdump, args=(ip[i], args.u, args.p)))
            time.sleep(0.1)
        for j in range(len(ip)):
            time.sleep(1)
            threads[j].start()
        for k in range(len(ip)):
            threads[k].join()
    else:
        commands = []
        ip = []
        if os.path.isfile(args.hostname[0]):
            with open(args.hostname[0], 'r') as f:
                lines = f.readlines()
            ip.extend(lines)
        else:
            ip = (args.hostname)
        # print(ip)
        if os.path.isfile(args.c):
            with open(args.c, 'r') as f:
                lines = f.readlines()
            commands.extend(lines)
        else:
            commands.extend(args.c.split(";"))

        for i in ip:
            print("\033[1mHost: " + i + "\033[0m")
            do_commands(i, args.u, args.p, commands)

    # commands = ["show version", "show interface ib status", "show ib sm", "show clock"]
    # mlnx_con = mlnxClient("192.168.1.119", "admin", "admin")
    # result = mlnxExecute(mlnx_con, commands)
    # print(result)

    # commands = ["net show system", "net show interface all", "net show system sensors", "cl-license"]
    # cumulusLinux_con = cumulusLinuxClient("192.168.1.101", "cumulus", "CumulusLinux!")
    # result = cumulusLinuxExecute(cumulusLinux_con, commands)
    # print(result)

    # commands = ["ifconfig", "date", "hostname"]
    # linux_con = linuxClient("192.168.1.83", "root", "123456")
    # result = linuxExecute(linux_con, commands)
    # print(result)
    # linux_con.disconnect()
    # generate_sysdump("192.168.1.119", "admin", "admin")


    end = datetime.now()
    print(end - start)
    print(datetime.now())

