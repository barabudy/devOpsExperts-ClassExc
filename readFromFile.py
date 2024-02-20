def request_username():
    new_names = []
    my_file = open("names.txt", "a")
    my_file.writelines("\n")

    for i in (range(3)):
        new_names.append(input("Please enter the %d name\t" % (i+1)))
        my_file.writelines(new_names[i] + "\n")
    print("The new added names are " + new_names[0] + ", " + new_names[1] + ", " + new_names[2])
    my_file.close()


def print_file_names():
    my_file = open("names.txt")
    for name in my_file.readlines():
        print(f"Hello {name}", end='')
    my_file.close()


request_username()
print_file_names()
