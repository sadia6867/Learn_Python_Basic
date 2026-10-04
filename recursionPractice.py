# practice 1
# def num(n):
#     if n==1:
#         return 1
#     return num(n-1) + n

# print(num(5))


# practice 2
def show_list(list,ind):
    if ind==len(list):
        return
    print(list[ind])
    show_list(list,ind+1)

fruits = ["apple","banana","cherry"]
show_list(fruits,0)