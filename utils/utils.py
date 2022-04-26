def get_user_operation():
    print('''\nEnter 1 for inserting/updating/deleting a Province
Enter 2 for inserting/updating/deleting a District
Enter 3 for inserting/updating/deleting a Municipality
Enter 4 for listing all Districts of a Province
Enter 5 for listing all Municipalities of a Province\n''')
    user_operation = input("Input: ")
    return user_operation


def validate_user_operation(user_operation):
    is_valid = True
    if user_operation != "1" and user_operation != "2" and user_operation != "3" and user_operation != "4"\
            and user_operation != "5":
        is_valid = False
    return is_valid


def get_crud_operation(type):
    print("\nEnter a for inserting a " + type + "\nEnter b updating a " +
          type + "\nEnter c for deleting a " + type + "\n")
    crud_operation = input("Input: ")
    return crud_operation


def validate_crud_operation(crud_operation):
    is_valid = True
    if crud_operation != "a" and crud_operation != "b" and crud_operation != "c":
        is_valid = False

    return is_valid


def print_success_message():
    print("\nCongratulations!The Operation was Succesfull.")


def print_failure_message():
    print("\nOops!Looks like You did some Mistake. Try Again!!")
