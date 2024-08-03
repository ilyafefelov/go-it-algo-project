def greedy_algorithm(items, budget):
    # Sort items by their calorie-to-cost ratio in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    chosen_items = []

    for item, details in sorted_items:
        if budget >= details['cost']:
            chosen_items.append(item)
            total_calories += details['calories']
            budget -= details['cost']

    return chosen_items, total_calories

# Example usage
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
greedy_result = greedy_algorithm(items, budget)
print("Greedy algorithm result:", greedy_result)




def dynamic_programming(items, budget):
    # Number of items
    n = len(items)
    # Convert items dictionary to a list for easier indexing
    item_list = list(items.items())
    
    # Create a 2D DP table with (n+1) rows and (budget+1) columns initialized to 0
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        item, details = item_list[i - 1]
        cost, calories = details['cost'], details['calories']
        for w in range(budget + 1):
            if cost <= w:
                # If the item can be included, choose the max of including or not including the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                # If the item cannot be included, carry forward the value without including the item
                dp[i][w] = dp[i - 1][w]

    # The maximum calories that can be achieved with the given budget
    max_calories = dp[n][budget]
    
    # To find the items included in the optimal solution, backtrack through the DP table
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, _ = item_list[i - 1]
            chosen_items.append(item)
            w -= items[item]['cost']

    # The items are collected in reverse order, reverse them to get the correct order
    chosen_items.reverse()
    
    return chosen_items, max_calories

# Example usage
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
dp_result = dynamic_programming(items, budget)
print("Dynamic programming result:", dp_result)
