class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prefix = defaultdict(list)

        for product in products:
            pre = ""
            for char in product:
                pre += char
                prefix[pre].append(product)

        res = []
        for i in range(1, len(searchWord) + 1):
            res.append(sorted(prefix[searchWord[:i]])[:3])

        return res
