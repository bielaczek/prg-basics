file_name = 'it_company.csv'

counter = 1

with open(file_name, 'r') as file:
    # content = file.read()

        # content = file.read()
    for x in range(5):
        line = file.readline().strip('\n')
        print(line)
