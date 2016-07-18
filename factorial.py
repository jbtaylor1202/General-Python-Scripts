def factorial(n):
    if n < 1:
        print ("Please enter a positive whole number.")
    else:
        tempData = n
        while n > 1:
            tempData = tempData * (n - 1)
            n = n - 1
        return tempData


print ("What number: ")
number = int(input())
print (factorial(number))
