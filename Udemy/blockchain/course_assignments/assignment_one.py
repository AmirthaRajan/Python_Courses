name = input("Enter your name : ")
age = input("Enter your age : ")

def get_decades_lived(age=age):
    return int(age) // 10

def print_details(name,age):
    print(name+ " " +age)
    print(get_decades_lived())

print_details(name,age)