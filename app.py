loop = "n"
while loop != "y":
    pid = input("Please Enter Product ID: ")
    name = input("Please Enter Name: ")
    desc = input("Please Enter Description: ")
    price = input("Please Enter Price: ")
    loop = input("Stop? Y/n: ").lower()   
    with open("file_object.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write("Product ID: " + pid)
    with open("file_object.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write("Name: " + name)
    with open("file_object.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write("Description: " + desc)
    with open("file_object.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write("Price: " + price)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write("----------------------------------------------------------------------------")
