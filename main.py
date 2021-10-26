"""
Welcome to Record Collection Project!

With this project, you will be able to manage
any record collection of type DICTIONARY,
that includes record's name as key
and record's amount as value - {'name':amount}.

Run the program and .enjoy().
"""

import funs4records as f4r


def main(record: dict):
    flag = True
    while flag:
        f4r.menu()
        flag = f4r.get_fun(f4r.choice_input(), record)


if __name__ == '__main__':
    record_D = {'OOPsIinitAgain': 5,
                'tryToExcept': 1,
                'HelpINeedSomebody': 3,
                'foobar': 1,
                'getfunc': 2,
                'FloatingInTheDeep': 3,
                'MyPayathondaDont': 4,
                'DontStackMeNow': 7,
                'HeapMeBabyOneMoreTime': 7
                }
    main(record_D)
