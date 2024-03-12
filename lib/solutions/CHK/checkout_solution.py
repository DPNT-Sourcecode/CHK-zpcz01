# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Check for illegal input
    if not isinstance(skus, str):
        return -1

    # Set prices of items with offers
    group_offer = (['S', 'T', 'X', 'Y', 'Z'], 45)
    prices = {
        'A': {'price': 50, 'special_offer': [(5, 200), (3, 130)]},
        'B': {'price': 30, 'special_offer': [(2, 45)]},
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {'price': 40, 'item_free': [(2, {'B': 1})]},
        'F': {'price': 10, 'item_free': [(2, {'F': 1})], 'require': 3},
        'G': {'price': 20},
        'H': {'price': 10, 'special_offer': [(10, 80), (5, 45)]},
        'I': {'price': 35},
        'J': {'price': 60},
        'K': {'price': 70, 'special_offer': [(2, 120)]},
        'L': {'price': 90},
        'M': {'price': 15},
        'N': {'price': 40, 'item_free': [(3, {'M': 1})]},
        'O': {'price': 10},
        'P': {'price': 50, 'special_offer': [(5, 200)]},
        'Q': {'price': 30, 'special_offer': [(3, 80)]},
        'R': {'price': 50, 'item_free': [(3, {'Q': 1})]},
        'S': {'price': 20, 'group': group_offer},
        'T': {'price': 20, 'group': group_offer},
        'U': {'price': 40, 'item_free': [(3, {'U': 1})], 'require': 4},
        'V': {'price': 50, 'special_offer': [(3, 130), (2, 90)]},
        'W': {'price': 20},
        'X': {'price': 17, 'group': group_offer},
        'Y': {'price': 20, 'group': group_offer},
        'Z': {'price': 21, 'group': group_offer},
    }

    item_counts = {}
    is_counted = count_items(skus, prices, item_counts)
    if is_counted == -1:
        return -1

    calculate_item_free(prices, item_counts)
    checkout_price = calculate_checkout_value(prices, item_counts)
    return checkout_price


def count_items(skus, prices, item_counts):
    for item in skus:
        if item not in prices:
            return -1

        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    return 0


def calculate_special_offer(prices, item, count):
    value = 0
    for special_quantity, special_price in prices[item]['special_offer']:
        special_count = count // special_quantity
        remaining_count = count % special_quantity
        value += special_count * special_price
        count = remaining_count

    value += count * prices[item]['price']

    return value


def calculate_item_free(prices, item_counts):
    item_keys = list(item_counts.keys())
    for item in item_keys:
        if 'item_free' in prices[item]:
            for free_quantity, free_item in prices[item]['item_free']:
                free_count = item_counts[item] // free_quantity
                required = prices[item].get('require', 0)
                if item_counts[item] < required:
                    continue
                for key, value in free_item.items():
                    if key in item_counts:
                        if required != 0:
                            free_count = item_counts[item] // (free_quantity + 1)
                        item_counts[key] -= free_count
                    else:
                        item_counts[key] = 0

def calculate_group_offer(group_offer):
    value = 0
    for item in group_offer:



def calculate_checkout_value(prices, item_counts):
    value = 0

    for item, count in item_counts.items():
        if 'special_offer' in prices[item]:
            value += calculate_special_offer(prices, item, count)
        else:
            value += count * prices[item]['price']

    return value




