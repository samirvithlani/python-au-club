school = [["Biology", "Chemistry", "Physics"], ["Maths", "Statistics", "Calculus"], ["English", "French", "German"]]

school[0][1]= "Computer Science"

for i in school:
    for j in i:
        print(j)