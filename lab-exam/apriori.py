from itertools import combinations
from collections import defaultdict

def read_transactions(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            transaction = line.strip().split(',')
            transactions.append(set(transaction))
    return transactions

def get_itemsets(transactions, length):
    items = set(item for transaction in transactions for item in transaction)
    return set(combinations(items, length))

def calculate_support(transactions, itemsets):
    support_count = defaultdict(int)
    for transaction in transactions:
        for itemset in itemsets:
            if set(itemset).issubset(transaction):
                support_count[itemset] += 1
    return support_count

def apriori(transactions, min_support):
    length = 1
    frequent_itemsets = []
    candidate_itemsets = get_itemsets(transactions, length)
   
    while candidate_itemsets:
        print(f"\n=== Generating itemsets of length {length} ===")
        support_count = calculate_support(transactions, candidate_itemsets)
        current_frequent = {itemset: count for itemset, count in support_count.items() if count >= min_support}
        if not current_frequent:
            break

        frequent_itemsets.extend(current_frequent.keys())
       
        print(f"Frequent Itemsets of Length {length}: ")
        for itemset, count in current_frequent.items():
            print(f"{str(itemset):<{(10*length) + 3}} -> Support: {count}")

        candidate_itemsets = set(combinations(
            set(item for itemset in current_frequent.keys() for item in itemset), length + 1))
        length += 1

    return frequent_itemsets

if __name__ == "__main__":
    file_path = "transactions.txt"
    min_support = 3
    transactions = read_transactions(file_path)

    print("=== Apriori Algorithm ===")
    frequent_itemsets = apriori(transactions, min_support)

    print("\n===== Results =====")
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset) 