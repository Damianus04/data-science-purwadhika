car_list = ["sawi", "jamur", "TEERONG", "lobak",
            "tomat", "jamur", "JAMur", "TERong"]


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
                - "add" to add item check\b
                - "update" to update item\b
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

                        if input_item[0].isalpha():
                            if len(car_list) > 0:
                                index = 0
                                for i in car_list:
                                    if input_item.lower() == i.lower():
                                        index = car_list.index(i)
                                    else:
                                        pass

                                if input_item.lower() == car_list[index].lower():
                                    command = str(
                                        input("\t\t---> Data has been registered.\n \t\tDo you want to add?(Y/N): ")).upper()
                                    if command == "Y":
                                        car_list.append(input_item)
                                        print("\t\t'item has been added'")
                                    else:
                                        print("\t\t'item is not added'")
                                else:
                                    command = str(
                                        input("\t\t---> Data is not registered.\n \t\tDo you want to add data?(Y/N): ")).upper()
                                    if command == "Y":
                                        car_list.append(input_item)
                                        print(f"\t\t'item has been added'")
                                    else:
                                        print("\t\t'item is not added'")
                            elif len(car_list) <= 0:
                                command = str(
                                    input("\t\t---> Data is not registered.\n \t\tDo you want to add data?(Y/N): ")).upper()
                                if command == "Y":
                                    car_list.append(input_item)
                                    print(f"\t\t'item has been added'")
                                else:
                                    print("\t\t'item is not added'")
                            else:
                                print("error")

                            for n, i in enumerate(car_list):
                                print(f"\t\t{n+1}. {i}")

                            exit_command = str(
                                input(f"1. back to main menu: (1) \n2. repeat menu {instruction}: (2) \n--->"))
                        else:
                            print("\t\t'input should be text only'")
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

                        index_to_update = []
                        for h, i in enumerate(car_list):
                            if i.lower() == input_item.lower():
                                index_to_update.append(h)

                        try:
                            if input_item.lower() in car_list[index_to_update[0]].lower():
                                update_item = str(
                                    input("\t\t---> Data has been registered.\n \t\tEnter the update?: "))

                                if update_item[0].isalpha():
                                    for i in index_to_update:
                                        car_list[i] = update_item
                                    print(f"'{update_item}' has been updated")
                                    for n, i in enumerate(car_list):
                                        print(f"\t\t{n+1}. {i}")
                                else:
                                    print("\t\t'input should be text only'")
                                    for n, i in enumerate(car_list):
                                        print(f"\t\t{n+1}. {i}")

                            else:
                                print("\t\t'the item is not in the list'")
                                print(
                                    "\t\t'please check your item in this list'")
                                for n, i in enumerate(car_list):
                                    print(f"\t\t{n+1}. {i}")
                        except:
                            print("\t\t'the item is not in the list'")
                            print(
                                "\t\t'please check your item in this list'")
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

                        index_to_delete = []
                        for h, i in enumerate(car_list):
                            if i.lower() == input_item.lower():
                                index_to_delete.append(h)

                        try:
                            if input_item.lower() in car_list[index_to_delete[0]].lower():
                                for i in sorted(index_to_delete, reverse=True):
                                    del car_list[i]
                                print(f"'{input_item}' has been deleted")
                            else:
                                print("\t\t'the item is not in the list'")
                                print(
                                    "\t\t'please check your item in this list'")
                                for n, i in enumerate(car_list):
                                    print(f"\t\t{n+1}. {i}")
                        except:
                            print("\t\t'the item is not in the list'")
                            print(
                                "\t\t'please check your item in this list'")
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
