class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        spe = defaultdict(int)
        for i, pos in enumerate(position): # assign speeds to original positions
            spe[pos] = speed[i]
        position.sort(reverse=True) # get closest cars to destination first
        l_fleet, fleets = 0, 0

        for pos in position:
            time = (target - pos) / spe[pos] #calculate how long until reaching destination
            if time > l_fleet: # if they get there before the fleet in front, means they will clump at some point
                fleets += 1 # so add them to the amount of fleets if they get there only after the last clump
                l_fleet = time
        
        return fleets
