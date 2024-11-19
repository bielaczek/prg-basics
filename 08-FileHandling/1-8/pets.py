###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

# reads the entire file
file_content = read_from_file('pets.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()

# prints the array
counter = 0

for line in file_lines:
   print(line)
   tab = line.split(" ")
   counter += len(tab)
print(counter)