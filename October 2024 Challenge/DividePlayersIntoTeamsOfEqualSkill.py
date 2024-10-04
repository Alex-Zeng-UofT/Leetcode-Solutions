class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        n, ret = len(skill), 0

        skill.sort()
        first_skill_pair = skill[0] + skill[-1]
        
        for i in range(n // 2):

            if skill[i] + skill[-1 - i] != first_skill_pair:
                return -1
                
            ret += skill[i] * skill[-1 - i]

        return ret