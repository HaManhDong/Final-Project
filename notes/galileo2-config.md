
### Set static ip for galileo 

```sh

# ifconfig eth0 inet 192.168.0.10 netmask 255.255.255.0 up

# vi  /etc/network/interfaces

iface eth0 inet static
address 192.168.0.10
netmask 255.255.255.0
gateway 192.168.0.250

# connmanctl services
*AR Wired                ethernet_984fee0314f4_cable

( # connmanctl config ethernet_984fee0314f4_cable --ipv4 manual 192.168.60.231 255.255.255.0 192.168.60.1)

# connmanctl config ethernet_984fee0314f4_cable --nameservers 8.8.8.8 8.8.4.4

# cat /var/lib/connman/ethernet_984fee0314f4_cable/settings

[ethernet_984fee0314f4_cable]
Name=Wired
AutoConnect=true
Modified=2018-02-08T12:04:52.642485Z
IPv4.method=dhcp
IPv6.method=auto                                                                                                                                                          
IPv6.privacy=disabled                                                                                                                                                     
Nameservers=8.8.8.8;8.8.4.4;

```

Source: https://communities.intel.com/thread/80494
