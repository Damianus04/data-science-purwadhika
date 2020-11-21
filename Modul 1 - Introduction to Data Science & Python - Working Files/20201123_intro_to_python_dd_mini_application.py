# data = [
#     {
#         "userId": 1,
#         "id": 1,
#         "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#         "body": "quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto"
#     },
#     {
#         "userId": 1,
#         "id": 2,
#         "title": "qui est esse",
#         "body": "est rerum tempore vitae sequi sint nihil reprehenderit dolor beatae ea dolores neque fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis qui aperiam non debitis possimus qui neque nisi nulla"
#     },
#     {
#         "userId": 1,
#         "id": 3,
#         "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
#         "body": "et iusto sed quo iure voluptatem occaecati omnis eligendi aut ad voluptatem doloribus vel accusantium quis pariatur molestiae porro eius odio et labore et velit aut"
#     }]

car_list = ["mustang", "ford", "volkswagen",
            "ferrari", "lamborghini", "porsche", "BMW"]

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
                system = ""
                while system != "exit":
                    print("Password is correct. Login is successful")
                    print("#"*70)
                    print("\t\t\tWELCOME TO APPLICATION")
                    print("#"*70)
                    print('''\t\tSelect the following instructions:\b
                        - "print" to print item\b
                        - "add" to add item\b
                        - "update" to udpate item\b
                        - "delete" to delete item\b
                        - "exit" to exit the application\b
                        ''')
                    instruction = str(
                        input('\t\t--->Enter your selected instruction: '))

                    if instruction == "print":
                        print("-"*70)
                        print('\t\tPRINT MENU')
                        input_item = str(
                            input("\t\t---> Enter item name: "))
                        if input_item in car_list:
                            index = car_list.index(input_item)
                            print(car_list[index])
                        elif input_item not in car_list:
                            print("\t\tthe item is not in the list")
                            print("\t\t'please check your item in this list'")
                            for n, i in enumerate(car_list):
                                print(f"\t\t{n+1}. {i}")
                        else:
                            print("'you do not enter the required inputs'")
                        print("-"*70)
                    elif instruction == "add":
                        print('\t\tADD MENU')
                        input_item = str(
                            input("\t\t---> Enter item name: "))
                        if input_item in car_list:
                            index = car_list.index(input_item)
                            if type(input_item) == type(car_list[index]):
                                command = str(input('''\t\t---> Data has been registered.\b
                                        Do you want to add?(Y/N): '''))
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
                            command = str(input('''\t\t---> Data is not registered.\b
                                                Do you want to add data?(Y/N): '''))
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

                        print("-"*70)
                    elif instruction == "update":
                        print('\t\tUPDATE MENU')
                        input_item = str(
                            input("\t\t---> Enter item name to update: "))
                        if input_item in car_list:
                            index = car_list.index(input_item)
                            if type(input_item) == type(car_list[index]):
                                update_item = str(input('''\t\t---> Data has been registered.\b
                                        Enter the update?: '''))
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

                        print("-"*70)
                    elif instruction == "delete":
                        print('\t\tDELETE MENU')
                        input_item = str(
                            input("\t\t---> Enter item name to update: "))
                        if input_item in car_list:
                            index = car_list.index(input_item)
                            if type(input_item) == type(car_list[index]):
                                # update_item = str(input('''\t\t---> Data has been registered.\b
                                #         Enter the item to delete?: '''))
                                car_list.remove(input_item)
                                print(
                                    f"\t\t'-{input_item}- has been deleted'")
                                for n, i in enumerate(car_list):
                                    print(f"\t\t{n+1}. {i}")
                            else:
                                print("'data format is incorrect'")
                        else:
                            print("\t\t'the item is not in the list'")
                            print("\t\t'please check your item in this list'")
                            for n, i in enumerate(car_list):
                                print(f"\t\t{n+1}. {i}")
                        print("-"*70)
                    elif instruction == "exit":
                        print('\t\tEXIT')
                        print("-"*70)
                        break
                    else:
                        print("you dont enter the correct instruction")
                        print("-"*70)

                    system = str(
                        input("do you want to continue?(yes/exit): "))
except:
    print("\t\terror occurs")


# instruction = str(input('''Select the following instructions:\b
#                             - "print" to print item\b
#                             - "add" to add item\b
#                             - "update" to udpate item\b
#                             - "delete" to delete item\b
#                             - "exit" to exit the application\n

#                             Enter your selected instruction: '''))

# if instruction == "print":
#     print('print')
# elif instruction == "add":
#     print('add')
# elif instruction == "update":
#     print('update')
# elif instruction == "delete":
#     print('delete')
# elif instruction == "exit":
#     print('exit')
# else:
#     print("you dont enter the correct instruction")


# try:
#     input_item = str(input("Enter item name: "))
#     instruction = str(input('''Select the following instructions:\b
#                             - "print" to print item\b
#                             - "add" to add item\b
#                             - "update" to udpate item\b
#                             - "delete" to delete item\b
#                             - "exit" to exit the application\n

#                             Enter your selected instruction: '''))
#     # 1 Read
#     if input_item in car_list:
#         index = car_list.index(input_item)
#         if instruction == "print":
#             print(car_list[index])
#         elif instruction == "add":
#             print("add instruction")
#     elif input_item not in car_list:
#         print("the item is not in the list")
#     else:
#         print("you do not enter the required inputs")
# except:
#     print('error')
