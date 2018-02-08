
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

# connmanctl config ethernet_984fee0314f4_cable --nameservers 8.8.8.8 8.8.4.4

```
