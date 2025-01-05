from collections import defaultdict

class FPTree:
    def __init__(self):
        self.root = Node(None, 0)
        self.header_table = defaultdict(list)

    def build_tree(self, transactions, min_support):
        freq = defaultdict(int)
        for t in transactions:
            for item in t: freq[item] += 1
        freq = {k: v for k, v in freq.items() if v >= min_support}

        for t in transactions:
            t = [i for i in t if i in freq]
            t.sort(key=lambda x: freq[x], reverse=True)
            self._insert(t)

    def _insert(self, transaction):
        node = self.root
        for item in transaction:
            if item not in node.children:
                node.children[item] = Node(item, 1)
                self.header_table[item].append(node.children[item])
                node.children[item].parent = node
            else:
                node.children[item].count += 1
            node = node.children[item]

    def mine_patterns(self, min_support):
        def mine(node, prefix):
            if prefix: patterns[tuple(prefix)] = node.count
            for child in node.children.values():
                mine(child, prefix + [child.item])

        patterns = {}
        for item, nodes in self.header_table.items():
            support = sum(n.count for n in nodes)
            if support >= min_support:
                patterns[(item,)] = support
                cond_tree = FPTree()
                paths = [[n.path(), n.count] for n in nodes]
                for path, count in paths:
                    cond_tree._insert(path)
                if cond_tree.root.children:
                    cond_tree.mine_patterns(min_support)
        return patterns

class Node:
    def init(self, item, count):
        self.item = item
        self.count = count
        self.parent = None
        self.children = {}
    def path(self):
        node, p = self.parent, []
        while node and node.item is not None:
            p.append(node.item)
            node = node.parent
        return p[::-1]

def read_transactions(file):
    with open(file) as f:
        return [line.strip().split() for line in f]

transactions = read_transactions("transactions.txt")
min_support = 2
tree = FPTree()
tree.build_tree(transactions, min_support)
patterns = tree.mine_patterns(min_support)
print("Frequent Patterns:", patterns)
