# nth fibonacci numebr using recursion meathods

number = int(input("Enter any numebr\t"))
def findFibonacci (num) :
    if (num == 1) : return 0;
    elif (num == 2) : return 1;
    else : return findFibonacci(num-1) + findFibonacci(num-2);


print (number ,'rd fibonacci number it :\t', findFibonacci(number));