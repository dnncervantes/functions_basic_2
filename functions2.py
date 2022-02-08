def count_down(highNum):
    list=[]
    for i in range(highNum,-1,-1):
        list.append(i)
    print(list)
x=count_down(10)
# for i in range(5,0,-1):
#     print(i)
def print_and_return(list):
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

def first_plus_length(x):
    return x[0] + len(x)
print(first_plus_length([1,2,3,4,5]))

def value_greater_than_second(j):
    if len(j) < 2:
        return False
    output = []
    for i in range(0,len(j)):
        if j[i] > j[1]:
            output.append(j[i])
    print(len(output))
    return output
print(value_greater_than_second([5,2,3,2,1,4]))
print(value_greater_than_second([3]))

def length_value(num1, num2):
    output = []
    for i in range(0, num1):
        output.append(num2)
    return output
print(length_value(4,7))
print(length_value(6,2))