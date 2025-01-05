from itertools import combinations
from collections import defaultdict

def read_transactions(file_path):
    """
    Reads transactions from a file.
    Each line in the file represents a transaction, with items separated by commas.
    """
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            transaction = line.strip().split(',')
            transactions.append(set(transaction))
    return transactions

def get_itemsets(transactions, length):
    """
    Generate candidate itemsets of a given length.
    """
    items = set(item for transaction in transactions for item in transaction)
    return set(combinations(items, length))

def calculate_support(transactions, itemsets):
    """
    Calculate the support count for each itemset.
    """
    support_count = defaultdict(int)
    for transaction in transactions:
        for itemset in itemsets:
            if set(itemset).issubset(transaction):
                support_count[itemset] += 1
    return support_count

def apriori(transactions, min_support):
    """
    Implements the Apriori algorithm to find frequent itemsets.
    """
    length = 1
    frequent_itemsets = []
    candidate_itemsets = get_itemsets(transactions, length)
   
    while candidate_itemsets:
        print(f"\n=== Generating itemsets of length {length} ===")
       
        # Calculate support for current candidates
        support_count = calculate_support(transactions, candidate_itemsets)
       
        # Filter itemsets based on minimum support
        current_frequent = {itemset: count for itemset, count in support_count.items() if count >= min_support}
        if not current_frequent:
            break
       
        # Add frequent itemsets to the result
        frequent_itemsets.extend(current_frequent.keys())
       
        print(f"Frequent Itemsets of Length {length}: ")
        for itemset, count in current_frequent.items():
            print(f"{str(itemset):<{(10*length) + 3}} -> Support: {count}")
       
        # Generate candidates for the next length
        candidate_itemsets = set(combinations(
            set(item for itemset in current_frequent.keys() for item in itemset), length + 1))
        length += 1

    return frequent_itemsets

if __name__ == "__main__":
    # Path to the transactions file
    file_path = "transactions.txt"
   
    # Minimum support threshold
    min_support = 3

    # Read transactions from the file
    transactions = read_transactions(file_path)
   
    # Perform Apriori Algorithm
    print("=== Apriori Algorithm ===")
    frequent_itemsets = apriori(transactions, min_support)
   
    # Output results
    print("\n===== Results =====")
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset) 