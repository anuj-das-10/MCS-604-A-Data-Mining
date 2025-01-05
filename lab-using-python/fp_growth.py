from collections import defaultdict

class TreeNode:
    def __init__(self, name, count, parent):
        self.name = name
        self.count = count
        self.parent = parent
        self.children = {}
        self.link = None

    def increment(self, count):
        self.count += count


def build_fptree(transactions, min_support):
    # Count item frequencies and filter by min_support
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1

    item_counts = {k: v for k, v in item_counts.items() if v >= min_support}
    if not item_counts:
        return None, None

    # Sort transactions by frequency
    sorted_transactions = []
    for transaction in transactions:
        filtered = [item for item in transaction if item in item_counts]
        sorted_transactions.append(sorted(filtered, key=lambda x: -item_counts[x]))

    # Build FP-tree
    root = TreeNode("root", 1, None)
    header_table = {item: None for item in item_counts}

    for transaction in sorted_transactions:
        current_node = root
        for item in transaction:
            if item not in current_node.children:
                new_node = TreeNode(item, 0, current_node)
                current_node.children[item] = new_node

                if header_table[item] is None:
                    header_table[item] = new_node
                else:
                    current = header_table[item]
                    while current.link is not None:
                        current = current.link
                    current.link = new_node

            current_node = current_node.children[item]
            current_node.increment(1)

    return root, header_table


def find_patterns(header_table, min_support):
    frequent_itemsets = []

    def mine_tree(node, suffix):
        itemset = suffix + [node.name]
        frequent_itemsets.append((itemset, node.count))

        for child in node.children.values():
            mine_tree(child, itemset)

    for item, node in header_table.items():
        while node is not None:
            mine_tree(node, [])
            node = node.link

    return frequent_itemsets


def fp_growth(transactions, min_support):
    tree, header_table = build_fptree(transactions, min_support)
    if not tree:
        return []

    return find_patterns(header_table, min_support)


# Read transactions from file
def read_transactions(file_name):
    with open(file_name, "r") as file:
        return [line.strip().split(",") for line in file.readlines()]


min_support = 3
input_file = "transactions.txt"

transactions = read_transactions(input_file)
frequent_itemsets = fp_growth(transactions, min_support)

print("Frequent Itemsets:")
for itemset, support in frequent_itemsets:
    print(f"Itemset: {str(itemset):<22} -> Support: {support}")
