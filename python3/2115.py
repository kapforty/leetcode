class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies, edgeMap = set(supplies), {}
        for i in range(len(recipes)):
            edgeMap[recipes[i]] = ingredients[i]
        
        def dfs(curr, path):
            if curr in supplies:
                return True
            if curr in path or curr not in edgeMap:
                return False
            for ingredient in edgeMap[curr]:
                path.add(curr)
                if not dfs(ingredient, path):
                    return False
                path.remove(curr)
            supplies.add(curr)
            return True

        res = []
        for k, v in edgeMap.items():
            if dfs(k, set()):
                res.append(k)
        return res
