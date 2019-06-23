# to find gcd og two numbers.

bigNumber = int(input("Enter any number :\t"));
smallNumber = int(input("Enter any number : \t"));

if (bigNumber < smallNumber) :
    bigNumber = smallNumber - bigNumber;
    smallNumber = smallNumber - bigNumber;
    bigNumber = bigNumber + smallNumber;

while (bigNumber % smallNumber != 0) :

    bigNumber = bigNumber % smallNumber;
    bigNumber = smallNumber - bigNumber;
    smallNumber = smallNumber - bigNumber;
    bigNumber = bigNumber + smallNumber;

print(smallNumber, " Is the G.C.D ")