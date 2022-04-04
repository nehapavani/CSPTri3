
# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from Week_0 import tree
from Week_0.Animation import animation
from Week_1 import fibonacci, infodb
from Week_1.infodb2 import tester, tester2, fibtester
from Week_2 import class_factorial, check_prime, check_prime_OOP, palindrome
##
# Menu banner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"
# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. "filename.py" will be run by exec(open("filename.py").read())
# 2. file.function references will be executed as file.function()
main_menu = [
    ["Tree", tree.driver],
    ["List + Loops", infodb.driver],
    ["Palindrome", palindrome.driver],
    ["Animation", animation.Animation],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Fibonacci", fibonacci.driver],
    ["Factorial", class_factorial.driver],
    ["Prime Number Checker", check_prime.driver],
    ["Prime Number Checker OOP", check_prime_OOP.driver],
]

lists_sub_menu = [
    ["InfoDB v2", tester],
    ["Factorial", tester2],
    ["Fibonacci", fibtester],
]

def menu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(banner, options)  # recursion, start menu over again


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    menu(title, sub_menu)

def lists_submenu():
    title = "Lists Submenu" + banner
    menu(title, lists_sub_menu)


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def driver():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Lists", lists_submenu])
    menu(title, menu_list)


if __name__ == "__main__":
    driver()
