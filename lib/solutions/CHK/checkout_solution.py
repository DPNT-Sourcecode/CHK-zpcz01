

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    item_counts = {}
    is_counted = count_items(skus, item_counts)
    if is_counted == -1:
        return -1

def count_items(skus, item_counts):
    for item in skus:
        if item not in item_counts:
            return -1

        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

        return 0
