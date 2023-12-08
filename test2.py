#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City

def test_all_method():
    # Create an instance of FileStorage
    fs = FileStorage()

    # Create two State objects
    state1 = State()
    state1.name = "California"
    fs.new(state1)

    state2 = State()
    state2.name = "Nevada"
    fs.new(state2)

    # Create one City object
    city = City()
    city.name = "Las Vegas"
    city.state_id = state2.id  # Assigning the city to Nevada
    fs.new(city)

    # Save the objects to file
    fs.save()

    # Retrieve all objects using the all method
    all_objects = fs.all()

    # Print the results
    print("All Objects:")
    for obj_key, obj_value in all_objects.items():
        print(obj_value)

if __name__ == "__main__":
    test_all_method()
