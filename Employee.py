#create an employee model usind pydantic for validaton:

from pydantic import BaseModel,Field,ValidationError

class Employeee(BaseModel):
    
    name : str
    Age : int
    employee_id : str |None = None
    salary : float = Field(gt = 0, lt=100000000)
    phone_number : int | None = None
    
#def main():
try:    
    data = Employeee(
            name = "Arjun",
            Age = 20,
            employee_id = "12_sid",
            salary = "300000.756"
            )
    print(data)
    
except ValidationError as e:
    print("Error: ",e)
    
#if __name__ == "__main__":
#    main()