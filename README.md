# route-graph
Analyzes regions of Foxhole MMO and determines optimized graph of resource nodes.


## Design Documentation
So currently I have these three functions that perform a variety of GETs. The User is going to pick a region (each region in the game is a server) they want to put under analysis, and when that happens we need to verify the server is active in this current war - getActiveRegions() is the request that returns that info.
 
List of active servers may be considered static
 

On first run, "getActiveRegions()" is called and caches the resulting list.

New war check. If new war detected, "getActiveRegions" runs again.

3. User must choose a valid region to analyze.