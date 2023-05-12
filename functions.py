def get_todos():
    with open("essay.txt", 'r') as file_local:
        filecontent = file_local.readlines()
        print(filecontent)
    return filecontent


def write_todos(todo_args, filepath='eassay.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_args)

def count(phrase):
    return phrase.count('.')

if __name__ == "__main__":
   print("Hello")
   print(get_todos())


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
