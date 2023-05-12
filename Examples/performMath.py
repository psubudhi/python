import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    #If there has been a previous calculation, use that result as the startping point
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye, human!")
        run = False
    else:
        #equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        equation = re.sub('[^0-9/*\-\+]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    p2erformMath()