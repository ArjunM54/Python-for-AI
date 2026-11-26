#Exception handling, ex: zerodivision error, value error, name error.

def main():
    
    a = 1
    
    try:
        number = int(input("Enter a number: "))
        result = a/number
        print(result)
        
    except ZeroDivisionError:
        print("Can't divide by zero you idiot !!")
        
    except ValueError:
        print("Enter numbers only.")
        
    except Exception:
        print("Somthing wrong!")
        
    finally:
        print("Done!")

main()