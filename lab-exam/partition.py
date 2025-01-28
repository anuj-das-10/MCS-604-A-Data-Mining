from itertools import combinations
from collections import defaultdict

def read_transactions(file_path):
    with open(file_path, 'r') as file:
        transactions = [line.strip().split(",") for line in file]
    return transactions

def get_frequent_itemsets(transactions, min_support):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[frozenset([item])] += 1

    frequent_itemsets = {itemset for itemset, count in item_counts.items() if count >= min_support}
    frequent_items_support = {itemset: count for itemset, count in item_counts.items() if count >= min_support}

    k = 2
    while frequent_itemsets:
        candidates = set()
        for itemset1 in frequent_itemsets:
            for itemset2 in frequent_itemsets:
                union_set = itemset1 | itemset2
                if len(union_set) == k:
                    candidates.add(union_set)

        candidate_counts = defaultdict(int)
        for transaction in transactions:
            transaction_set = frozenset(transaction)
            for candidate in candidates:
                if candidate.issubset(transaction_set):
                    candidate_counts[candidate] += 1

        frequent_itemsets = {itemset for itemset, count in candidate_counts.items() if count >= min_support}
        frequent_items_support.update({itemset: count for itemset, count in candidate_counts.items() if count >= min_support})
        k += 1

    return frequent_items_support

def partition_algorithm(file_path, min_support, num_partitions=2):
    transactions = read_transactions(file_path)
    partition_size = len(transactions) // num_partitions
    partitions = [transactions[i * partition_size: (i + 1) * partition_size] for i in range(num_partitions)]

    local_frequent_itemsets = []
    for partition in partitions:
        local_frequent_itemsets.append(get_frequent_itemsets(partition, min_support // num_partitions))

    global_candidates = set()
    for itemsets in local_frequent_itemsets:
        global_candidates.update(itemsets.keys())

    global_counts = defaultdict(int)
    for transaction in transactions:
        transaction_set = frozenset(transaction)
        for candidate in global_candidates:
            if candidate.issubset(transaction_set):
                global_counts[candidate] += 1

    globally_frequent_itemsets = {itemset: count for itemset, count in global_counts.items() if count >= min_support}

    return globally_frequent_itemsets

file_path = "transactions.txt"
min_support = 3     # Minimum support count
num_partitions = 3  # Number of partitions
frequent_itemsets = partition_algorithm(file_path, min_support, num_partitions)

print(f"{"Frequent Itemsets":<18} | Support")
print("-" * 28)
for itemset, support in frequent_itemsets.items():
    print(f"{str(set(itemset)):<18} : {support}")
