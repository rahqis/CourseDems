# List classes and demographics of each class for this college
import csv

f = open("test_python.csv")

csv_f = csv.reader(f)

raceCvs = []
courseNameCvs = []
genderCvs = []
courseThing =""
for row in csv_f:
    raceCvs.append(row[3])
    courseThing += row[4] + ' '
    genderCvs.append(row[2])
    courseNameCvs.append(row[4])



def race_counter(course: str, race: str) -> float:
    z: int = 0

    for i in range(0,len(courseNameCvs)):
        if(course in courseNameCvs[i]):
            if(race == raceCvs[i]):
                z += 1
    return z

Black: str = "Black or African American"
Asian: str = "Asian or Pacific-Islander"
White: str = "White/Caucasian"
Hispanic: str = "Hispanic/Latinx"
Middle: str = "Middle-Eastern/North African"
Native: str = "American Indian or Alaska Native"




def specific_race(course: str) -> dict[str, float]:
    x: float = race_counter(course, Black)
    y: float = race_counter(course, Asian)
    z: float = race_counter(course, White)
    n: float = race_counter(course, Hispanic)
    m: float = race_counter(course, Middle)
    u: float = race_counter(course, Native)
    race_list = [Black, Asian, White, Hispanic, Middle, Native]
    race_counter_List = [x, y, z, n, m, u]
    total: float = x + y + z + n + m + u
    o: dict[str, float] = {}
    j: int = 0
    while j < len(race_list):
        sum: float = race_counter_List[j]/total
        o[race_list[j]] = sum
        j += 1
    return o


print(specific_race("MATH 381"))




f.close()




