class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map={}
        result=[]

        for i in strs:
            
            key="".join(sorted(i))
            if key not in hash_map:
                hash_map[key]=[]

            hash_map[key].append(i)
        
        for ele,idx in hash_map.items():

            result.append(idx)
        return result

        