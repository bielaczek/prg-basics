###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
    if test_results[answer]:
        correct_answers += 1

# calculates the number of incorrect answers
wrong_anwsers = 0
for answer in test_results:
    if not test_results[answer]:
        wrong_anwsers += 1

# calculates the percentage of correct answers
percentage = correct_answers/question_number * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrerct answers:', wrong_anwsers)
print(f'percentage: {percentage}%', )