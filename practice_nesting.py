library = {"name" : "coforge",
           "Year" : 1998,
           "book" : [
               {"title" : "Love it" , "author" : "Anudeep",  "genres" : ["Romance", "Fiction", "Love"]},
               {"title": "He met her on Dating app" , "author" : "Hema", "genres" : ["Drama", "Fiction", "Love"]},
               {"title": "She killed him" , "author" : "Sahithi", "genres" : ["Murder-Mystery", "Fiction", "Love"]},    
           ],   
           "location" : {"city" : "Hyderabad",
                         "Number_of_floors" : 5}
}

print(library)
print(library["name"])
print(library["location"]["city"])
print(library["book"][0]["title"])
print(library["book"][2]["author"])
print(library["book"][0]["genres"])
print(library["book"][1]["genres"][0])
print(len(library["book"]))
library["book"].append({"title" : "Love yourself" , "author" : "Nithu", "genres" : ["Self-love", "Fiction", "Love"]})
print(library)
library["location"] ["city"] = "Bangalore"
print(library["location"]["city"])
library["location"] ["open"] = True
print(library["location"])
print(library["book"][3])
