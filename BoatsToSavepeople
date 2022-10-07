class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        numBoats = 0
        i,j = 0,len(people)-1
        while i<=j:
            remain = limit - people[j]
            j-=1
            numBoats+=1
            if remain >= people[i]:
              i+=1
        return numBoats
