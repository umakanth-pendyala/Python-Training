# nth fibonacci number using iteration 

number = int(input('Enter any Number:\t'))
firstNumber = 0;secondNumber = 1;
finalNumber = 0;
count = 2;
if number == 2 :print (number,"rd fibonacci number :\t 1");
elif number == 1 : print (number,"rd fibonacci number :\t 0");
else :
    while (count < number) :
        count = count + 1;
        finalNumber = firstNumber + secondNumber;
        firstNumber = secondNumber;
        secondNumber = finalNumber;
        
    print (number,"rd fibonacci number :\t",finalNumber);