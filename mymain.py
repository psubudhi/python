import functions

print("In My Main")


nr_of_periods = functions.count("Trees are good. Grass is green.dgdh.")

print(nr_of_periods)

while True:
    user_action=input("Type add, show, edit or complete or exit:")
    user_action=user_action.strip()

    if user_action.startswith('add'):
        todo=user_action[4:]
        todos = functions.get_todos()
        functions.write_todos(todo)
    elif user_action.startswith('show'):
        todos=functions.get_todos()
        functions.write_todos()