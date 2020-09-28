### Configuration of IP address in Routers and ping messages.

* A network toplogy was created using Router-PT as a connecting device and two PCs(end devices) connected to it.
* A Default gateway and a unique IP address was set up for both the devices.
* Router IP address Configuration for interfaces fa 0/0 and fa 1/0.<br>The following commands were executed in the CLI:

```
enable
config terminal 
interface <interface_name>
ip address <ip_address>  <subnet_mask>
no shutdown
exit
```
* A ping request was sent to PC1 from PC0 using the command prompt using the commands `ipconfig` and `ping <ip_address_PC1>` and a ping reply was recieved from PC1.
* A simple PDU was simulated by sending an ICMP packet from PC0(source) to PC1(destination).

### Learning Outcomes
1. A router is a networking device that forwards data packets between computer networks and works on the network layer.
2. Creating a network topology using a router.
3. Configuration of IP address in interfaces.
4. Using ICMP PING responses to manually test for connectivity between network devices i.e checking if the destination is live.
5. Simulation of a simple PDU.
6. The device sets TTL in the packet header.

