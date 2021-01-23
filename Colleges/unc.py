# List classes and demographics of each class for this college

import csv

f = open("test_python.csv")

csv_f = csv.reader(f)


## Variables to hold the values from the csv file
collegeName = []
gender = []
courseName = []
race = []

## Appending the info from the file
for row in csv_f:
    collegeName.append(row[1])
    gender.append(row[2])
    race.append(row[3])
    courseName.append(row[4])

## Gets rid of the question that was on the google form
collegeName = collegeName[1::]
gender = gender[1::]
race = race[1::]
courseName= courseName[1::]
originalCourseName =[]
modifiedCourseName = []

## Makes a list of courses that each students has taken by seperating them by ","
for i in courseName:
    originalCourseName.append(i.split(", "))


## Combines all the subjects of each students into one list to be used later
def printOutCourse(originalCoure):
    for i in range(0,len(originalCoure)):
        for j in range(0,len(originalCoure[i])):
            toPrint = originalCourseName[i][j]
            modifiedCourseName.append(toPrint.upper())
    print(modifiedCourseName)

##Checks for duplicate course and skips that 
courseWithoutDuplicate = []
def getRidOfDuplicate(allCourseList):
    for i in allCourseList:
        if i not in courseWithoutDuplicate:
            courseWithoutDuplicate.append(i)

    return courseWithoutDuplicate
    print(courseWithoutDuplicate)


printOutCourse(originalCourseName)
getRidOfDuplicate(modifiedCourseName)




## Finds the indexes at which the course overalp with other students (it's not doing that tho)
def lookForIndex(courseWithoutDuplicate, originalList):
    index = []
    indexY = []
    shortIndex = []
    shortInedxY = []
    for i in range(0,len(courseWithoutDuplicate)):
        for j in range(0,len(originalList)):
            for k in range(0,len(originalList[j])):
                if(courseWithoutDuplicate[i] == originalList[j][k]):
                    index.append(j)
                    indexY.append(k)
                else:
                    continue

                for a in index:
                    if a not in shortIndex:
                        shortIndex.append(a)
                for b in indexY:
                    if b not in shortInedxY:
                        shortInedxY.append(b)
    print(index)
    print(indexY)
    print(shortIndex)
    print(shortInedxY)

lookForIndex(courseWithoutDuplicate,originalCourseName)






f.close()




