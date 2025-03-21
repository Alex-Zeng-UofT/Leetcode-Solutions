class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        def can_cook(recipe, supps, mapping, seen):

            if recipe not in supps and recipe not in mapping or recipe in seen:
                return False

            seen.add(recipe)
            
            for req in mapping[recipe]:
                if req not in supps and not can_cook(req, supps, mapping, seen):
                    return False

            seen.remove(recipe)
            supps.add(recipe)
            return True

        map = {}
        sups = set(supplies)
        seen = set()
        ret = []

        for i in range(len(recipes)):
            map[recipes[i]] = []
            for ing in ingredients[i]:
                map[recipes[i]].append(ing)
        
        for key in map:
            if can_cook(key, sups, map, seen):
                ret.append(key)

        return ret