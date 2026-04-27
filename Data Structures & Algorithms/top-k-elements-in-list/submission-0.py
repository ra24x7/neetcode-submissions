class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        freq = []
        for n in nums:
          hash[n] = hash.get(n,0)+1
        for _ in range(len(nums)+1):
          freq.append([])
        for n,c in hash.items():
          freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
          for n in freq[i]:
            res.append(n)
            if len(res) == k:
              return res
        



        

        
