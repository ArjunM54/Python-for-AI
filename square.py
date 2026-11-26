"""create a function that calculate the square of the number."""

def square(num):
    return num*num

def main():
    
    number = int(input("Enter a number to check its square: "))
    result = square(number)
    print(result)
    
main()