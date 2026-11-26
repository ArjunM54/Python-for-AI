#json.dump and json load

import json

def dumpp(response):
    result = json.dumps(response) #the dumps works based on convert the python dictionary to json object.
    print(result)
    print(type(result))
    
def loaad(response):
    result = json.loads(response) #the lods works based on convert the json obsect to python dictionary.
    print(result)
    print(type(result))

def main():
    student = [
        {
            "Name":"Arjun",
            "Age":20,
            "College":"Hindusthan"
        },
        {
            "Name":"Abishek",
            "Age":18,
            "College":"Bishob"
        },
        {
            "Name":"Dharanee",
            "Age":18,
            "College":"None"
        }
    ]
    dumpp(student)
    
    print("\n===================================\n")
    
    person = '{"Name":"Arjun","Age":20,"College":"Hindusthan"}'
    loaad(person)
    
if __name__ == "__main__":
    main()