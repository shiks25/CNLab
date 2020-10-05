## Configuring IP address and static routes in multiple router topology
* A toplogy was created using three Router-PT and two PC's using copper cross-over and serial DCE connections as [shown here](./topology.png).
* Dafault gateway and unique IP address was set up in both the PC's.
* IP address was configured for each of the interfaces i.e fastEthernet and Serial using CLI in [Router0](router0_config.png),[Router1](router1_config.png),[Router2](router2_config.png).
* Pinging PC1 from PC0 gave destination host unreachable.
* Ip routes for each router was viewed using the command: `show ip route`
* Static ip route for missing ip routes(the device networks not connected directly) was configured for each router using CLI command: `ip route destination_network subnet_mask next_hop_address`
* Pinging PC1 from PC0 gave the required ping responses.
