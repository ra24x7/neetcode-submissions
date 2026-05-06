class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sp =[[p,s] for p, s in zip(position,speed)]
        sp.sort(reverse=True)
        
        fleet = 0
        prevtime = 0
        for p,s in sp:
            time = (target-p)/s
            if time > prevtime:
                fleet += 1
                prevtime = time
        return fleet