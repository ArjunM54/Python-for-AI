"""creat a dictionary containing your name, college, department and age. 
print each value seperatly."""

def main():
    
    student = {
        "Name" : "Arjun M",
        "Age" : 20,
        "College" : "Hindusthan college",
        "Department" : "BE CSE"
    }
    
    print(student)
    print("-----------------------------------------------------------------------------------")
    student["Age"] = 21 # it's update the age.
    del student["College"] # it delete te college in the list.
    print(student["Age"])  #it print the seperate key'values.
    print(student)
    
main()
