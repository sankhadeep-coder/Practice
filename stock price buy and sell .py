p = [7, 1, 5, 3, 6, 4]

minimum = p[0]
profit = 0

for i in range(1, len(p)):

    if p[i] < minimum:
        minimum = p[i]

    current_profit = p[i] - minimum

    if current_profit > profit:
        profit = current_profit

print(profit)