# Problem
There are n gas stations along a circular route, where the amount of gas at the i^th^ station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the i^th^ station to its next (i + 1)^th^ station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

### Constraints
- n == gas.length == cost.length
- 1 <= n <= 10^5^
- 0 <= gas[i], cost[i] <= 10^4^

# Solution
## Approach (TC: O(N), SC: O(1))
Initially, we need to find whether the total amount of gas is sufficient or not. If not, then we can never travel around a circuit. Otherwise, we initialize a variable named `gas_available` with 0 to account for the available gas at the current station to go to the next station. We initialize another variable named `start` to take care of the starting station from where we can start travelling to complete a circuit. Then we iteratively calculate the available gas and check whether the available gas is sufficient or not. If not, then we reset the available gas to 0 and mark the next station as the starting station. Lastly, we return the starting station.