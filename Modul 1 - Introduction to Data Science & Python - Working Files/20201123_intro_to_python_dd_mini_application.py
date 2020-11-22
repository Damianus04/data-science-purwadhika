# car_list = ["mustang", "ford", "volkswagen",
#             "ferrari", "lamborghini", "porsche", "BMW"]
car_list = []

try:
    password = "pw9876"
    login = ""
    trial = 1
    trial_limit = 4
    chances = 4

    while login != password and trial <= trial_limit:
        if trial <= trial_limit:
            login = input("--->Enter your password: ")
            if login == "exit":
                print("EXIT APPLICATION")
                break
            elif login != password and trial < trial_limit:
                trial += 1
                chances -= 1
                print(
                    f"Wrong password, please try again. \nYou still have {chances} chances")
            elif login != password and trial == trial_limit:
                trial += 1
                print(f"Wrong password. You cannot enter any more password")
            else:
                print("Password is correct. Login is successful")
                exit_command = ""
                while exit_command != "exit" or exit_command == "1":
                    print("#"*70)
                    print("\t\t\tWELCOME TO APPLICATION")
                    print("#"*70, '\n')
                    print("\t\t===DATA===")
                    for n, i in enumerate(car_list):
                        print(f"\t\t{n+1}. {i}")
                    print('\n', "+-"*35, '\n')
                    print("\t\t===INSTRUCTIONS===")
                    print('''\t\tSelect the following instructions:\b
                    - "print" to print item\b
                    - "add" to add item\b
                    - "update" to udpate item\b
                    - "delete" to delete item\b
                    - "exit" to exit the application\b''')
                    instruction = str(
                        input('\t\t--->Enter your selected instruction: '))

                    if instruction == "print":

                        exit_command = ""
                        while exit_command != "1":
                            print("-"*70)
                            print('\t\tPRINT MENU')
                            if len(car_list) == 0:
                                print("\t\tlist is empty")
                            elif len(car_list) > 0:
                                for n, i in enumerate(car_list):
                                    print(f"\t\t{n+1}. {i}")
                            exit_command = str(
                                input(f"1. back to main menu: (1) \n2. repeat menu {instruction}: (2) \n--->"))
                        print("-"*70)
                    elif instruction == "add":
                        exit_command = ""
                        while exit_command != "1":
                            print('\t\tADD MENU')
                            input_item = str(
                                input("\t\t---> Enter item name: "))
                            if input_item in car_list:
                                index = car_list.index(input_item)
                                if type(input_item) == type(car_list[index]):
                                    command = str(
                                        input("\t\t---> Data has been registered.\n \t\tDo you want to add?(Y/N): "))
                                    if command == "Y":
                                        car_list.append(input_item)
                                        print("\t\t'item has been added'")
                                    else:
                                        print("\t\t'item is not added'")
                                    for n, i in enumerate(car_list):
                                        print(f"\t\t{n+1}. {i}")
                                else:
                                    print("data format is incorrect")
                            elif input_item not in car_list:
                                command = str(
                                    input("\t\t---> Data is not registered.\n \t\tDo you want to add data?(Y/N): "))
                                if command == "Y":
                                    car_list.append(input_item)
                                    print(f"\t\t'item has been added'")
                                else:
                                    print("\t\t'item is not added'")
                                for n, i in enumerate(car_list):
                                    print(f"\t\t{n+1}. {i}")
                            else:
                                print("\t\t'the item is not in the list'")
                                print("\t\t'please check your item in this list'")
                                for n, i in enumerate(car_list):
                                    print(f"\t\t{n+1}. {i}")

                            exit_command = str(
                                input(f"1. back to main menu: (1) \n2. repeat menu {instruction}: (2) \n--->"))

                        print("-"*70)
                    elif instruction == "update":
                        exit_command = ""
                        while exit_command != "1":
                            print('\t\tUPDATE MENU')
                            input_item = str(
                                input("\t\t---> Enter item name to update: "))
                            if input_item in car_list:
                                index = car_list.index(input_item)
                                if type(input_item) == type(car_list[index]):
                                    update_item = str(
                                        input("\t\t---> Data has been registered.\n \t\tEnter the update?: "))
                                    car_list[index] = update_item
                                    print("\t\t'data has been updated'")
                                    for n, i in enumerate(car_list):
                                        print(f"\t\t{n+1}. {i}")
                                else:
                                    print("'data format is incorrect'")
                            else:
                                print("\t\t'the item is not in the lis't")
                                print("\t\t'please check your item in this list'")
                                for n, i in enumerate(car_list):
                                    print(f"\t\t{n+1}. {i}")

                            exit_command = str(
                                input(f"1. back to main menu: (1) \n2. repeat menu {instruction}: (2) \n--->"))

                        print("-"*70)
                    elif instruction == "delete":
                        exit_command = ""
                        while exit_command != "1":
                            print('\t\tDELETE MENU')
                            input_item = str(
                                input("\t\t---> Enter item name to delete: "))
                            for i in car_list:
                                if i == input_item:
                                    car_list.remove(input_item)
                                # index = car_list.index(input_item)
                                # if type(input_item) == type(car_list[index]):
                                #     car_list.remove(input_item)
                                #     print(
                                #         f"\t\t'-{input_item}- has been deleted'")
                                #     for n, i in enumerate(car_list):
                                #         print(f"\t\t{n+1}. {i}")
                                # else:
                                #     print("'data format is incorrect'")
                            else:
                                print("\t\t'the item is not in the list'")
                                print("\t\t'please check your item in this list'")
                                for n, i in enumerate(car_list):
                                    print(f"\t\t{n+1}. {i}")

                            exit_command = str(
                                input(f"1. back to main menu: (1) \n2. repeat menu {instruction}: (2) \n--->"))

                        print("-"*70)
                    elif instruction == "exit":
                        print('\t\tEXIT')
                        print("-"*70)
                        break
                    else:
                        print("\t\t'you do not enter the correct instruction'")
                        print("-"*70)

                    # system = str(
                    #     input("\t1. type any keyword to return to main menu\n\t2. type 'exit' to quit application\n\t--->"))
except:
    print("\t\terror occurs")

    # input_item = str(
    #     input("\t\t---> Enter item name: "))
    # if input_item in car_list:
    #     index = car_list.index(input_item)
    #     print(car_list[index])
    # elif input_item not in car_list:
    #     print("\t\tthe item is not in the list")
    #     print("\t\t'please check your item in this list'")
    #     for n, i in enumerate(car_list):
    #         print(f"\t\t{n+1}. {i}")
    # else:
    #     print("'you do not enter the required inputs'")
