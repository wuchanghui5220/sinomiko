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



