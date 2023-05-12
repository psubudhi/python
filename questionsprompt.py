import json

with open("questionbank") as file:
    content = file.read()

data=json.loads(content)
score=0
for question in data:
    print(question["Question text"])
    for index, alternatives in enumerate(question["alternatives"]):
        print (index, "-", alternatives)
    user_choice=int(input("Enter answer number: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["answer"]:
        score = score + 1

for index, question in enumerate(data):
    message= f" {index+1} - Your answer: {question['user_choice']},"  \
             f" Correct answer is: {question['answer']}"
    print(message)

print(score,"/",len(data))