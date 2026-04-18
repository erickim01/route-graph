# route-graph
Analyzes regions of Foxhole MMO and determines optimized graph of resource nodes based on roads.


## Design Documentation

MVP - User selects a region, and a desired resource (components). Regional data is fetched and finds midpoint of resources
      based on distance to drive on roads. Returns image graph displaying best route between nodes and centralized location.


List of active servers may be considered static.
 
### User Query

- User must choose a valid region to analyze.

- User must choose a valid resource (currently only one at a time).

### Static Data Handling

- On first run, "getActiveRegions()" is called.

- Cache of region list for Shard.

- For each region, Call and cache:
    - resource node location
    - Refinery
    - Depot / Seaports
    - Road & Type / Mountain / Landscape

- New war check. If new war detected, "getActiveRegions()" runs again.

### Graph Logic

- Meaningfully use resource node and road location data to determine valid route on a field
    (??? Put entire map into array ???)

### Output

- Fetch resulting data from previous section

- Get image of region

- Draw corresponding path of determined route onto image

- Option to return this image and data from previous section

