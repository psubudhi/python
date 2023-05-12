
count=int(input("Enter the count"))
while count>0:
    print(count)
    count=count-1

i = 1
list=[]
while i <= 5:
    print(i)
    list.append(i)
    i += 1
print(list)

text=input("Enter Case string")
match text:
    case 'add':
        print("ad called")
    case 'min':
        print("min called")
    case 'sub':
        print("sub called")

for meal in 'meals':
    print(meal.capitalize())

strs = ["1.abc.def","2.asd.ghj","3.asda.adf","4.AFS.F"]
for str in strs:
    str=str.replace('.','-')
    print(str)

file1 = open("essay.txt",'r')
print(file1.read())

names = ["john smith", "jay santi", "eva kuki"]
print(names)
names=[name.title() for name in names]
print(names)
names=[len(name) for name in names]
print(names)
name= set(names)
print(names)

user_entries = ['10', '19.1', '20']
user_entries =[float(user) for user in user_entries]
print(user_entries)
print(sum(user_entries))



with open("essay.txt", 'r') as file:
    ## print(file.read())
    print(len(file.read()))
with open("essay.txt", 'w') as file:
    file.writelines("My New line")


pwdtext= input("Enter pasword")
if len(pwdtext) < 7:
    print("passwword is weak")
elif len(pwdtext) == 7:
    print("passwword is ok but weak")
else :
    print("passwword is good")
while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print("The sum of the two numbers is:", result)
        break
    except ValueError:
        print("Please enter a valid number.")

def get_todo():
    text = input("Enter the value")
    return text

while True:
    try:
        num1 = int(get_todo())
        num2 = int(get_todo())
        result = num1 + num2
        print("The sum of the two numbers is:", result)
        break
    except ValueError:
        print("Please enter a valid number.")

