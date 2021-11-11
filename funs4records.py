"""
This module is required for 'main' in 'Record_Collection' project.
"""

# **** INNER FUNCTIONS **** #


def my_add(name: str, amount: int, record: dict) -> str:
    res = my_search(name, record, sub=False)
    if res == name:
        record[name] += amount
        return '>> record\'s amount update completed: '+name+','+str(record[name])
    # if record was not found
    record[name] = amount
    return '>> record adding completed: '+name+','+str(record[name])


def my_del(name: str, amount: int, record: dict) -> str:
    res = my_search(name, record, sub=False)
    if res == name:
        subs = record[name]-amount
        if subs > 0:
            record[name] = subs
            return '>> record\'s amount update completed: '+name+','+str(record[name])
        elif subs == 0:
            del record[name]
            return '>> record deleting completed'
        return '>> updated amount invalid! record deleting failed'
    # if record was not found
    return res+', record deleting failed'


def my_search(name: str, record: dict, sub=True):
    keys_list = sorted(list(record.keys()))
    options_list = []
    for key in keys_list:
        if key.startswith(name):
            options_list.append(key)
    if sub:
        if not options_list:
            return '>> record was not found'
        for key in options_list:
            print(key, record[key], sep=':')
        return "*"
    # if sub=False
    if name not in options_list:
        return '>> record was not found'
    return name


def my_up_name(old: str, new: str, record: dict) -> str:
    res = my_search(old, record, sub=False)
    if res == old:
        record[new] = record.pop(old)
        return '>> record\'s name update completed: '+new+','+str(record[new])
    # if record was not found
    print(res)
    return '>> record\'s name update failed'


def my_up_amount(name: str, amount: int, record: dict) -> str:
    res = my_search(name, record, sub=False)
    if res != name:
        print(res)
        return res+', record\'s amount update failed'
    # if record was found
    record[name] = amount
    return '>> record\'s amount update completed: '+name+','+str(record[name])


def my_total(record: dict) -> str:
    total_names = len(record)
    total_amount = sum(record.values())
    if 0 in [total_names, total_amount]:
        return '>> There are no records in the Record Collection'
    return '>> There are '+str(total_amount)+' records in the Record Collection\n' + \
'>> There are '+str(total_names)+' different albums'


def my_order(record: dict):
    if len(record) == 0:
        return '>> There are no records in the Record Collection'
    for name in sorted(record, key=lambda x: x.lower()):
        print(name, ":", record[name])
    return '*'


# **** INPUT & VALIDATIONS **** #


def choice_input() -> int:
    """ input + validation for CHOICE from the menu """
    choice = input('Please choose one action from 1 to 8 : ')
    if choice in list('12345678'):
        return int(choice)
    print('** WrongInput: enter only integer between 1 and 8 **')
    return choice_input()


def name_input() -> str:
    """ input + validation for RECORD_NAME """
    flag = True
    while flag:
        name = input('Enter record\'s name: ')
        if name.isalpha():
            return name
        print('** WrongInput: enter only alphabet letters **')


def amount_input() -> int:
    """ input + validation for AMOUNT """
    flag = True
    while flag:
        amount = input('Enter amount: ')
        if amount.isdigit() and amount != '0':
            return int(amount)
    print('** WrongInput: enter only integer larger than 0 **')
    print('** WrongInput: enter only integer larger than 0 **')


# **** OUTER FUNCTIONS **** #


def outer_add(record: dict):
    return my_add(name_input(), amount_input(), record)


def outer_del(record: dict):
    return my_del(name_input(), amount_input(), record)


def outer_search(record: dict):
    return my_search(name_input(), record)


def outer_up_name(record: dict):
    print('Previous name >>', end=" ")
    old = name_input()
    print('New name >>', end=" ")
    new = name_input()
    return my_up_name(old, new, record)


def outer_up_amount(record: dict):
    return my_up_amount(name_input(), amount_input(), record)


# **** PROGRAM **** #


def menu():
    print("+--------------------------------------------+",
          "| Welcome to Records Collection !            |",
          "| Please select one of the options bellow :  |",
          "| 1. Add a record                            |",
          "| 2. Delete a record                         |",
          "| 3. Search by record name                   |",
          "| 4. Update record's name                    |",
          "| 5. Update record's amount                  |",
          "| 6. Get total amount                        |",
          "| 7. Get the collection in alphabetic order  |",
          "| 8. Exit                                    |",
          "+--------------------------------------------+",
          sep='\n')
    return


def get_fun(choice: int, record: dict) -> bool:
    choice_dict = {1: outer_add,         # dictionary of references to the functions
                   2: outer_del,
                   3: outer_search,
                   4: outer_up_name,
                   5: outer_up_amount,
                   6: my_total,
                   7: my_order
                   }
    print()
    if choice == 8:
        print('Goodbye :(')
        return False
    foo = choice_dict[choice]  # defining function
    print(foo(record))         # calling function
    print()
    return True
