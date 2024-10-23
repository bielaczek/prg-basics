dog_age = int(input("Enter the dog's age in human years: "))
if dog_age <= 2:
    print(f"The dog's age in dog's years is {dog_age * 10.5} years.")
elif dog_age > 2:
    print(f"The dog's age in dog's years is {21 + 4 * (dog_age - 2)} years.")