#example for type hints.

#Integers
Age : int = 20

#String
Name : str = "Arjun"

#Float
Height : float = 196.25

#List
Marks : list[int] = [99,97,89]

#dictionary
Student : dict[str,int] = {
    "Name":"Arjun",
    "Age":20
}

#type hint using functions:
def customer(name :str, age:int) -> str:
    print("I am ",name," and ",age," years old")
    
def main():
    customer("Arjun",20)
    
if __name__ == "__main__":
    main()