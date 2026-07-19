price = 9.99
Is_Learning = True
print(type(price))
print(type(Is_Learning))
print(type("Hema"))
print(type(28))

#Lists
Skills= ["Marketing", "Google ads", "Meta Ads", "Python", "f-strings"]
print(Skills)
print(Skills[0]) #[0] is the index- items position
print(Skills[3])
print(Skills[4])
Skills.append("RAG")
print(Skills)
print(len(Skills))

#Dictionaries
person_1 = { "name" : "Hema",
            "job": "Marketing",
            "city": "Hyderabad",
            "age": 28
            }
print(person_1)
print(person_1["age"])
print(person_1["job"])
print(person_1["name"])
person_1["goal"] = "AI Engineer"
print(person_1)

#Nesting
ai_engineer = { "name" : "Hema",
               "skills" : ["Python", "RAG", "Git", "LLM"],
               "progress" : { 
                   "days_completed" : 4,
                   "current_topic" : "dictionaries"
               }
            }
print(ai_engineer)
print(ai_engineer["name"])
print(ai_engineer["skills"][0])
print(ai_engineer["progress"]["days_completed"])
print(ai_engineer["progress"]["current_topic"])
print(ai_engineer["skills"][3])

ai_engineer["progress"] ["git"] = "started"
print(ai_engineer["progress"])

