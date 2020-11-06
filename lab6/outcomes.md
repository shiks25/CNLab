## Configuring RIP Routing Protocol in Routers
* A toplogy was created using three Routers connected via serial DCE connections and two PCs as [shown here](topology.PNG).
* Default Gateway and IP address was added to the PCs and Router interfaces were configured.
* `Encapsulation ppp` was specified to all the routers along with `clock rates 64000` where required while configuring them.
* Routing Information Protocol (RIP) is a dynamic routing protocol which uses hop count as a routing metric to find the best path between the source and the destination network and adds it to the router table.
* RIP routing protocol was configured using the commands:<br>
`router rip`<br>`network destination addresses`.
* Pinging PC1 from PC0 gives the required [response](ping_pc1.PNG).
