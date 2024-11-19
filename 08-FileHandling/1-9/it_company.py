###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

counter = 1

with open(file_name, 'r') as file:
   for line in file:
        if job_title in line:
            print(counter, line.split(',')[0], line.split(',')[1]) 
            counter += 1