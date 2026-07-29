class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map={}

        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1

        # Sort the keys based on their values (frequencies) in descending order
        sorted_elements = sorted(hash_map.keys(), key=lambda x: hash_map[x], reverse=True)
        
        # Return the first k elements from the sorted list
        return sorted_elements[:k]