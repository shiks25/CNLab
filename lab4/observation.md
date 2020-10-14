## Configuration of default route to the Router in a multiple routers and switches topology

* A toplogy was created using three Router-PT, two Switch-PT and two PC's each connected to switch as [shown here](topology.png).
* Default gateways and unique ip addresses were configured for each PC .
* IP address was configured for each interface using CLI.
* Pinging PC2 from PC0 gave "destination host unreachable" as the device networks were not connected directly.
* Ip routes for each router was viewed using the command: `show ip route`.
* **Static ip route** was configured for router 1 using CLI command: `ip route destination_network subnet_mask next_hop_address` ([Router1](router1.PNG)).
* **Default ip route** was configured for router 0 and router 2 using CLI command:<br> `ip route 0.0.0.0 0.0.0.0 next_hop_address` ([Router0](router0.PNG),[Router2](router2.PNG)).<br>
(**NOTE:** Configuring default ip route to a router ensures that the packet passes through the default route when no other route is available for an IP destination address)
* Pinging PC2 from PC0 gave the required reply message as [shown here](ping_msg.PNG).
* An ICMP packet was simulated from PC0 to PC2 using simple PDU as ([shown here](simulation.PNG)).
