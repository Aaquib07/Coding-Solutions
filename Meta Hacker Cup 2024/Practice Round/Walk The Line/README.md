# Problem
There’s an old, narrow bridge that a group of `N` travelers wish to cross in the night. The bridge can only support the weight of at most 2 people. Crossers must stay together and use the group’s only flashlight while on the bridge. Traveler i can cross the bridge in $S_{i}$ seconds alone.

Thankfully, the group had the foresight to bring a (very lightweight!) wheelbarrow. Either:
- traveler `i` can cross the bridge alone in $S_{i}$ seconds, optionally bringing the wheelbarrow, or
- two travelers `i` and `j` can both cross in $S_{i}$ seconds if traveler `j` rides in the wheelbarrow

Any group crossing the bridge must bring the flashlight. It can be returned to the initial side by the same rules above. Is there a strategy for all travelers to cross the bridge in `K` seconds?

### Constraints
- 1 <= T <= 95
- 1 <= N <= 1000
- 1 <= $S_{i}$, K <= $10^{9}$