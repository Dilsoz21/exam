#task_3
x=int(input("enter the percentage:"))
massiv=[10, 20, 30, 40, 50]

def foiz(x, massiv):
    for i in massiv:
        p=(x*i)//100
        return p



print(foiz(x, massiv))


#task_2
num=int(input("enter the number of people:"))


def task2(num):
    c=num//5
    if num>5:
        print(f"we need {c} car")
    else:
        print(f"we haven't got enough people")
        return


print(task2(num))


#task_1
massiv=[1,3,4,7,9,2,6,8]


def task1(massiv):
    for x in range(1, 11):
        if not x in massiv:
            return x


print(task1(massiv))





