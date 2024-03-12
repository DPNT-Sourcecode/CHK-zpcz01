# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Check for illegal input
    if not isinstance(skus, str):
        return -1

    # Set prices of items with offers
    prices = {
        'A': {'price': 50, 'special_offer': [(3, 130), (5, 200)]},
        'B': {'price': 30, 'special_offer': [(2, 45)]},
        'C': {'price': 20},
        'D': {'price': 15},
        'E': {'price': 40, 'item_free': [(2, {'B': 1})]},
    }

    item_counts = {}
    is_counted = count_items(skus, prices, item_counts)
    if is_counted == -1:
        return -1

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


def calculate_special_offer(prices, count):
    special_quantity, special_price = prices[item]['special_offer']
    special_count = count // special_quantity
    remainder = count % special_quantity
    return special_count * special_price + remainder * price


def calculate_checkout_value(prices, item_counts):
    value = 0

    for item, count in item_counts.items():
        price = prices[item]['price']
        if 'special_offer' in prices[item]:
            special_quantity, special_price = prices[item]['special_offer']
            special_count = count // special_quantity
            remainder = count % special_quantity
            value += special_count * special_price + remainder * price
        else:
            value += count * price

    return value


