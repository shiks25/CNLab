## Configuring DHCP within a LAN

* A Topology was created using a Switch 2950T-24,Router PT,Server PT and 4PCs as [shown here](topology.PNG).
* The Router interface(fa0/0) was configured using CLI.
* The DHCP Server was configured specifying the default gateway(IP Address of the router), DNS server and TFTP server(IP Address of the server) as [shown here](dhcp_services.png).
* 4 steps in DHCP<br>
D - Discover the server<br>
O - Offer the IP address<br>
R - Request IP<br>
A - Acknowledgement<br>
* The PCs in the network individually request the Server for IP address and it assignes IP addresses dynamically from a pool of IP addresses.An example is [shown here](request_ip.png).

