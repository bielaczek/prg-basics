import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    data = queue.LifoQueue()
    for char in expression:
        if char == '[' or char == '(' or char == '{':
            data.put(char)
        elif char == ']':
            if data.get() != '[':
                return False
        elif char == ')':
            if data.get() != '(':
                return False
        elif char == '}':
            if data.get() != '{':
                return False
            
    if data.empty():
        return True
    else:
        return False

if brackets_ok(expression1):
   print('Brackets OK')
else:
   print('Brackets NOT OK')

if brackets_ok(expression2):
    print('Brackets OK')
else:
    print('Brackets NOT OK')

if brackets_ok(expression3):
    print('Brackets OK')
else:
    print('Brackets NOT OK')