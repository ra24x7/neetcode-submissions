class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

      #get the count of each numbers
      map = {}
      for n in nums:
        map[n] = map.get(n,0) + 1
      
      #create empty buckets with frequency as index
      freq = [[] for _ in range(len(nums) + 1)]

      #add values to these empty buckets
      for key, v in map.items():
        freq[v].append(key)


      # Find top K elements and response back
      result = []
      for c in range(len(freq) - 1, 0, -1):
        for i in freq[c]:
          result.append(i)
          if len(result) == k:
            return result

       




        

        
