import pprint

hobbiesList = ["Playing chess", "Drawing"]
data = {"name" : "Vinay", "age" : 23, "hobbies" : hobbiesList, "time" : "10 AM"}
print(data)
print(f'Hello I am {data["name"]} and I have {len(data["hobbies"])} hobbies! On the weekend I get up at {data["time"]}')