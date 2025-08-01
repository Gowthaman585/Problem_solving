#no of test case
test_case = int(input())
#list for storing the user input numbers
stick_list =  []
#loop until no of test case 
for i in range(0,test_case):
    get_number = input()
    stick_list.append(get_number)
#Declaring the fixed dictinary because the no of sticks for each number in seven segment display is fixed
stick_dict= {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
#method that deals when the total numbers of sticks is even
def even_sticks(no_of_sticks):
    half = no_of_sticks//2
    print('1'*int(half))
#This one is for odd
def odd_sticks(no_of_sticks):
    copy = no_of_sticks-3
    copy = copy//2
    print('7'+'1'*int(copy))
#Method when total numbers of sticks id greater then 9 to separate it single individual digits
def sum_two_sticks(element):
    last = element[1]
    first = element[0]
    sticks_of_last = stick_dict[last]
    sticks_of_first = stick_dict[first]
    tot_sticks = sticks_of_last + sticks_of_first
    if(tot_sticks%2==0):
        even_sticks(tot_sticks)
    else:
        odd_sticks(tot_sticks)
#final code to call the method to do the task
for i in stick_list:
    i = str(i)
    if len(i) == 1:
        no_sticks = stick_dict[i]
        if(no_sticks%2==0):
            even_sticks(no_sticks)
        else:
            odd_sticks(no_sticks)
    elif len(i)==2:
        sum_two_sticks(i)
    #For 100 always same output so for that
    elif i=='100':
        print(1111111)
    # this else conditon is for hidden test case that handle large number of input not fit with in int data -- avoid this else statement
    else:
        tot_sticks = 0
        for dig in i :
            tot_sticks = tot_sticks+stick_dict[dig]
        if tot_sticks%2==0:
            even_sticks(tot_sticks)
        else:
             odd_sticks(tot_sticks)

