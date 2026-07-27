#Loops- do this thing, once for every time
#To print each skills we need to write print(skills[0]), print(skills[1]) 
# to solve this we have loops
skills = ["Marketing", "AI", "Python","LLM", "n8n"]

for anything in skills:
    print(anything)

# Decode: for - keyword to start loop. it means repeat of each
#Skill/ anything - is basically a temporary box we are inventing. for each pass through loop python puts current item in the box
# in skills- in the skills list you're going through
#:- block the code intendentation - what to do on each pass

for skill in skills:
    print(f"I am learning {skill} ")

#Looping in numbers through range()
for number in  range(5):
    print(number)

for day in range(1,8):
    print(f"Day {day} of learning")

#Looping through your dictionaries
books = [
    {"title" : "Love it", "author" : "Anudeep"},
    {"title" : "She Killed him", "author" : "Sahithi"},
    {"title" : "Love yourself", "author": "Hema"}
]
for book in books:
    print(f"{book['title']} by {book['author']}")

#Playlist Program:

playlist = [
    {"title": "F.R.I.E.N.D.S", "artist" : "Billie", "Duration" : 2.45},
    {"title": "Baby", "artist" : "Justin Bieber", "Duration" : 4.02},
    {"title": "Young and Beautiful", "artist" : "Lana Del Rey", "Duration" : 3.42},
    {"title": "Believer", "artist" : "Enimen", "Duration" : 4.00}
]
for song in playlist:
    print(f"{song['title']} by {song['artist']} - {song['Duration']} min")

print(len(playlist))

#single dictionary pairs
song = {"title": "Believer", "artist": "Eminem", "duration": 4.0}

for key, value in song.items():
    print(f"{key}: {value}")

#Student Report Program
students = [
        {"name" : "Hema", "marks" : 88, "subjects" : ["Maths", "Social", "Hindi", "RAG"]},
        {"name" : "Sahithi", "marks" : 93, "subjects" : ["Maths", "Science", "English"]},
        {"name" : "Anudeep", "marks" : 77, "subjects" : ["Maths", "Social", "Physics"]},
        {"name" : "Jyotsna", "marks" : 95, "subjects" : ["Science", "Social", "Python"]},
    ]

for student in students:
            print(f"{student['name']} scored {student['marks']}-")
            if student['marks'] >= 90:
                print("Grade A")
            elif student['marks'] >= 70:
                print("Grade B")
            elif student['marks'] >= 50:
                print ("Grade C")
            else:
                print("Fail!")
            print(f"{student['name']} is taking {len(student['subjects'])} subjects")

#While Loops- keep doing this until a condition becomes false

count = 1

while count <=5:
     print(f"count is {count}")
     count = count + 1
# Decode :
# count =1 starting value before loop. this is for something to keep checking.
# while count <=5 - this is the condition. python checks if the count is <= 5 if not it stops.
#count = count + 1 this is important. It changes the count each pass  (1--> 2-->3...). without it count stays 1 forver. 
# 1 <=5. the loop never stops. it is called infinite loop. program hangs forver

count = 5

while count >= 1:
    print(count)
    count = count - 1
print("Blast off")

#Gym Membership Checker

members = [
     {"name" : "Hema", "age" : 25, "visits" : 25, "active" : True},
     {"name" : "Sahithi", "age" : 23, "visits" : 28, "active" : True},
     {"name" : "Anudeep", "age" : 33, "visits" : 10, "active" : False},
     {"name" : "Surya", "age" : 27, "visits" : 15, "active" : True},
     {"name" : "Jyotsna", "age" : 28, "visits" : 5, "active" : False},
     {"name" : "Rohan", "age" : 55, "visits" : 3, "active" : True}
]

for mem in members:
     if mem['active'] and mem['visits'] >=15:
          print(f"{mem['name']} -- Gold Status!")
     elif mem['active'] and mem['visits'] >=5:
          print(f"{mem['name']} -- Regular member")
     elif mem['active'] and mem['visits'] < 5:
          print(f"{mem['name']} -- We miss you! Only {mem['visits']} visits this month")
     else:
          print(f"{mem['name']} -- membership inactive, please renew")
active_count = 0
for mem in members:
    if mem['active']:
        active_count +=1  
print(f"Active members: {active_count}")