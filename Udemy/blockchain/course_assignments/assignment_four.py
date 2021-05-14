
def mymethod(method_name , *values):
    [print("{:^20.1f}".format(method_name(value))) for value in values]

def sum_values(value):
    return value

arg = [10,100,1000]

mymethod(arg,method_name=sum_values)

mymethod((lambda multiples , multi: multiples * multi,[1,2,3,4,5],1),method_name=sum_values)