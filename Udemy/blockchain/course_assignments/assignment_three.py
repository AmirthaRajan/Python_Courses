persons = []

def add_person():
    name = input("Enter user name : ")
    age = int(input("Enter user age : "))
    hobbies = []
    read_hobbies = True
    while read_hobbies:
        hobby = input("Enter a hobby or Enter 'q' for no more hobbies : ")
        if hobby == 'q':
            read_hobbies =False
        hobbies.append(hobby)
    person = {
        'name' : name,
        'age' : age,
        'hobbies' : hobbies
        }
    persons.append(person)

def get_names():
    names = [person['name'] for person in persons]
    print(names)

def get_older_persons():
    check_age = all([person['age'] > 20 for person in persons])
    if check_age:
        print("All persons are above 20 age")
    else:
        print("Some persons are not above 20 age")

def get_persons_copy():
    copy_persons = persons[:]
    print(copy_persons)

def unpack_persons():
    names , ages , hobbies = [ [(name,age,hobbies) for (name,age,hobbies) in person.values()] for person in persons]
    print(names)
    print(ages)
    print(hobbies)

reading_input = True

while reading_input:
    print("1 : Add a person")
    print("2 : Output person names")
    print("3 : Check if all persons are older than 20")
    print("4 : Get copy of persons")
    print("5 : unpack all person details")
    print("q : quit")
    input_value = input("Enter your option : ")
    if input_value == '1':
        add_person()
        continue
    elif input_value == '2':
        get_names()
        continue
    elif input_value == '3':
        get_older_persons()
        continue
    elif input_value == '4':
        get_persons_copy()
        continue
    elif input_value == '5':
        unpack_persons()
        continue
    elif input_value == 'q':
        reading_input = False
        print("User Left...")

print("Done!!")
    