from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if the total amount of gas is not sufficient
        if sum(gas) < sum(cost):
            # we cannot travel around the circuit
            return -1
        
        gas_available = 0
        # starting station from where we can start
        start = 0

        for i in range(len(gas)):
            # update the available gas to go to next station
            gas_available += gas[i] - cost[i]
            # if the available gas goes below zero
            if gas_available < 0:
                # we again rest the gas available
                gas_available = 0
                # we set the next station as the starting station
                start = i + 1
                
        # we return the starting index            
        return start