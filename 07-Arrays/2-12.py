categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

i = 1

most_expensive = expenses[0]
most_index = 0
while i < len(categories):
    if expenses[i] > most_expensive:
        most_expensive = expenses[i]
        most_index = i
    i += 1

print(f'Most expensive: {categories[most_index]}')