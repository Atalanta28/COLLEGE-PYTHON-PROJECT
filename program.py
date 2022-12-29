import csv
import subprocess
import numpy as np
import sys
try:
    import matplotlib.pyplot as plt
except:
    subprocess.run(['pip', 'install', 'matplotlib'])
    import matplotlib.pyplot as plt
fields=["Student ID", "Name", "Class Roll Number", "Batch Name"]
c=None

def addStudent():
    with open ("student.csv", "r") as fhand:
        c=fhand.read()
    if c=="":
        with open ("student.csv", "a") as fhand:
            csvWriter=csv.writer(fhand)
            csvWriter.writerow(fields)
    else:
        sid=input("STUDENT ID: ")
        sname=input("STUDENT NAME: ")
        sroll=input("CLASS ROLL NUMBER: ")
        sbatch=input("BATCH NAME: ")
        sdetails=[sid,sname,sroll,sbatch]
        with open ("student.csv","a") as fhand:
            csvWriter=csv.writer(fhand)
            csvWriter.writerow(sdetails)

def viewStudent():
    with open ("student.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        print("--------------------------------------------------------------------------------------------")
        for row in csvReader:
            print(row[0]+" "*(12-len(row[0]))+row[1]+" "*(30-len(row[1]))+str(row[2])+" "*(25-len(str(row[2])))+row[3])
        print("--------------------------------------------------------------------------------------------")
def removeStudent():
    delID=input("Enter the ID of the student to be deleted: ")
    editedData=[]
    with open ("student.csv","r") as fhandin:
        csvReader=csv.reader(fhandin)
        for row in csvReader:
            if(row[0]!=delID):
                editedData.append(row)
    with open ("student.csv","w") as fhandout:
        csvWriter=csv.writer(fhandout)
        csvWriter.writerows(editedData)
def updateStudent():
    updateddata=[]
    updateid=input("Enter the id of the student to be updated: ")
    updateChoice=int(input("1)Update student's name, 2)Update student's roll number, 3)Update student's batch"))
    with open ("student.csv","r") as fhandin:
        csvReader=csv.reader(fhandin)
        for row in csvReader:
            if(row[0]!=updateid):
                updateddata.append(row)
            else:
                match updateChoice:
                    case 1:
                        newName=input("Enter the new name: ")
                        row=[row[0],newName,row[2],row[3]]
                    case 2:
                        newRoll=int(input("Enter the new roll number: "))
                        row=[row[0],row[1],newRoll,row[3]]
                    case 3:
                        newBatch=input("Enter new batch: ")
                        row=[row[0],row[1],row[2],newBatch]
                updateddata.append(row)
    with open ("student.csv","w") as fhandout:
        csvWriter=csv.writer(fhandout)
        csvWriter.writerows(updateddata)
def generateReport():
    sid=input("Enter the student id: ")
    print("Enter the marks of the students if the student does not have a subject write NA there(Full marks is 100)")
    phy=input("Physics: ")
    bio=input("Biology: ")
    chem=input("Chemistry: ")
    math=input("Mathematics: ")
    elec=input("Basic Electrical Engineering: ")
    mech=input("Engineering Mechanics: ")
    comp=input("Computer: ")
    marksList=[phy,bio,chem,math,elec,mech,comp]
    with open ("student.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(sid==row[0]):
                with open(sid + ".txt", "a") as fhand:
                    fhand.write(f"REPORT CARD\nSTUDENT ID: {sid} \nSTUDENT NAME: {row[1]}\nMARKS             GRADES           STATUS\n")
    for item in marksList:
        stat="PASS"
        if(item!="NA"):
            marks = int(item)
            print(marks)
            if marks >= 90:
                grade = "A"
            elif marks >= 80:
                grade = "B"
            elif marks >= 70:
                grade = "C"
            elif marks >= 60:
                grade = "D"
            elif marks >= 50:
                grade = "E"
            elif marks < 40:
                grade = "F"
                stat="FAIL"
            with open(sid+".txt","a") as fhand:
                fhand.write(str(marks)+" "*(18-len(str(marks)))+grade+" "*(17-len(grade))+stat+"\n")
    marksList=[eval(i) for i in marksList]
    overAllPercentage=sum(marksList)/len(marksList)
    with open(sid + ".txt", "a") as fhand:
        fhand.write(f"The overall percentage: {overAllPercentage}%")
def studentDb():
    choice=0
    while(choice!=6):
        choice=int(input("Enter 1)CREATE A STUDENT, 2)UPDATE STUDENT DETAILS, 3)REMOVE A STUDENT FROM THE DATABASE, 4)GENERATE REPORT CARD OF A STUDENT, 5)VIEW DB 6)BACK! "))
        match choice:
            case 1:
                addStudent()
            case 2:
                updateStudent()
            case 3:
                removeStudent()
            case 4:
                generateReport()
            case 5:
                viewStudent()


#Course Database

def addCourse():
    courseField=["id","name","marks"]
    with open ("course.csv", "r") as fhand:
        c=fhand.read()
    if c=="":
        with open ("course.csv", "a") as fhand:
            csvWriter=csv.writer(fhand)
            csvWriter.writerow(courseField)
    else:
        cid=input("Course ID: ")
        cname=input("Course name: ")
        marksLength=int(input("Enter the number of student you want to add marks: "))
        cmarks=dict(input("Enter student id and marks separated by a space: ").split() for i in range (marksLength))
        cdetails=[cid,cname,cmarks]
        with open ("course.csv","a") as fhand:
            csvWriter=csv.writer(fhand)
            csvWriter.writerow(cdetails)
def viewCourse():
    with open ("course.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        print("--------------------------------------------------------------------------------------------")
        for row in csvReader:
            print(row[0]+" "*(12-len(row[0]))+row[1]+" "*(30-len(row[1]))+str(row[2]))
        print("--------------------------------------------------------------------------------------------")
def viewPerformance():
    courseId=input("Enter the course id: ")
    reqDic={}
    with open("course.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[0]==courseId):
                reqDic=eval(row[2])
        with open("student.csv","r") as fhand:
            csvReader=csv.reader(fhand)
            print("--------------------------------------------------------------------------------------------")
            print("NAME                          ROLL        MARKS")
            for key,value in reqDic.items():
                for row in csvReader:
                    # print(row)
                    # print(key)
                    if(key==row[0]):
                        print(row[1]+" "*(30-len(row[1]))+row[2]+" "*(12-len(row[2]))+value)
                        break
            print("--------------------------------------------------------------------------------------------")       
def histogram():
    courseId=input("Enter the course id: ")
    marksList=[]
    marksDict={}
    with open("course.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
          if(row[0]==courseId):
                marksDict=eval(row[2])
                for key,value in marksDict.items():
                    marksList.append(int(value))
                plt.hist(marksList)
                plt.title("COURSE STATISTICS(HISTOGRAM)")
                plt.xlabel("Grades")
                plt.ylabel("Number of students")
                plt.show()
            
    

def courseDb():
    choice=0
    while(choice!=5):
        choice=int(input("Enter 1)CREATE A COURSE, 2)VIEW PERFORMANCE OF ALL STUDENTS IN A COURSE, 3)COURSE STATISTICS(HISTOGRAM), 4)VIEW 5)BACK! "))
        match choice:
            case 1:
                addCourse()
            case 2:
                viewPerformance()
            case 3:
                histogram()
            case 4:
                viewCourse()

#BATCH DATABASE
def addBatch():
    batchField=["Batch ID","Batch Name","Department Name", "List of Courses", "list of students"]
    with open ("batch.csv", "r") as fhand:
        c=fhand.read()
    if c=="":
        with open ("batch.csv", "a") as fhand:
            csvWriter=csv.writer(fhand)
            csvWriter.writerow(batchField)
    bid=input("Batch ID(e.g:- ECE22): ")
    bname=input("Batch name(e.g:- ECE 2022-26): ")
    dname=input("Department name(e.g:- ECE): ")
    courseLength=int(input("Enter the number of courses in this batch: "))
    courseList=[input("Enter course ids in this batch(one by one): ") for i in range(courseLength)]
    studentList=[]
    with open ("student.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[3]==bid):
                studentList.append(row[0])
    # studentLength=int(input("Enter number of students in the batch: "))
    # studentList=[input("Enter student id: ") for i in range(studentLength)]
    bdetails=[bid,bname,dname,courseList,studentList]
    with open ("batch.csv","a") as fhand:
        csvWriter=csv.writer(fhand)
        csvWriter.writerow(bdetails)
def viewBatch():
    with open ("batch.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        for row in csvReader:
            print(row[0]+" "*(20-len(row[0]))+row[1]+" "*(25-len(row[1]))+str(row[2])+" "*(25-len(row[2]))+str(row[3])+" "*(40-len(str(row[3])))+str(row[4]))
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
def viewStudentList():
    batchId=input("Enter batchId: ")
    with open ("batch.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[0]==batchId):
                studentList=eval(row[4])
                print("STUDENT ID             NAME                                ROLL")
                for element in studentList:
                    with open ("student.csv", "r") as fhand:
                        csvReader=csv.reader(fhand)
                        for row in csvReader:
                            if(row[0]==element):
                                print(row[0]+" "*(23-len(row[0]))+row[1]+" "*(36-len(row[1]))+str(row[2]))
def viewCourseList():
    batchId=input("Enter batchId: ")
    with open ("batch.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[0]==batchId):
                courseList=eval(row[3])
                print("COURSE ID      NAME")
                for element in courseList:
                    with open ("course.csv", "r") as fhand:
                        csvReader=csv.reader(fhand)
                        for row in csvReader:
                            if(row[0]==element):
                                print(row[0]+" "*(15-len(row[0]))+row[1])
def viewBatchPerformance():
    batchId=input("Enter the batch ID: ")
    print("ROLL      NAME                              PERCENTAGE OBTAINED")
    with open ("batch.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[0]==batchId):
                studetList=eval(row[4])
                for element in studetList:
                    with open("course.csv", "r") as fhandCourse , open("student.csv", "r") as fhandStudent:
                        csvReaderStudent=csv.reader(fhandStudent)
                        roll=0
                        name=""
                        for i in csvReaderStudent:
                            if(i[0]==element):
                                name=i[1]
                                roll=i[2]
                        csvReader=csv.reader(fhandCourse)
                        count=0
                        tmarks=0
                        marks=0
                        marksDict={}
                        for row in csvReader:
                            if(row[2]!="marks"):
                                marksDict=eval(row[2])
                                if element in marksDict.keys():
                                    tmarks=int(marksDict[element])+tmarks
                                    count=count+1
                        if count!=0:
                            marks=tmarks/count
                            print(roll+" "*(10-len(roll))+name+" "*(34-len(name))+str(marks)+"%" )
                    # with open ("student.csv", "r") as fhand:
                    #     csvReader=csv.reader(fhand)
                    #     for row in csvReader:
                    #         if(row[0]==e):
def pieChart():
    value=[]
    label=[]
    batchId=input("Enter the batch ID: ")
    with open ("batch.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[0]==batchId):
                studetList=eval(row[4])
                for element in studetList:
                    with open("course.csv", "r") as fhandCourse , open("student.csv", "r") as fhandStudent:
                        csvReaderStudent=csv.reader(fhandStudent)
                        roll=0
                        name=""
                        for i in csvReaderStudent:
                            if(i[0]==element):
                                name=i[1]
                                roll=i[2]
                        csvReader=csv.reader(fhandCourse)
                        count=0
                        tmarks=0
                        marks=0
                        marksDict={}
                        for row in csvReader:
                            if(row[2]!="marks"):
                                marksDict=eval(row[2])
                                if element in marksDict.keys():
                                    tmarks=int(marksDict[element])+tmarks
                                    count=count+1
                        if count!=0:
                            marks=tmarks/count
                            value.append(marks)
                            label.append(name)
                            # print(roll, name, marks,"%" )                                
    plt.pie(value, labels=label)
    plt.title("PERFORMANCE OF STUDENTS(PIE CHART)")
    plt.show()
def batchDb():
    choice=0
    while(choice!=7):
        choice=int(input("Enter 1)CREATE A NEW BATCH, 2)VIEW LIST OF ALL STUDENT IN A BATCH, 3)VIEW LIST OF ALL COURSES TAUGHT IN A BATCH, 4)VIEW COMPLETE PERFORMANCE OF ALL STUDENTS IN A BATCH 5)PIE CHART OF PERCENTAGE OF ALL STUDENTS 6)VIEW DB 7)BACK! "))
        match choice:
            case 1:
                addBatch()
            case 2:
                viewStudentList()
            case 3:
                viewCourseList()
            case 4:
                viewBatchPerformance()
            case 5:
                pieChart()
            case 6:
                viewBatch()
def addDepartment():
    batchField=["Department ID", "Department Name", "Batch List"]
    with open ("department.csv", "r") as fhand:
        c=fhand.read()
    if c=="":
        with open ("department.csv", "a") as fhand:
            csvWriter=csv.writer(fhand)
            csvWriter.writerow(batchField)
    did=input("Department ID(e.g:- ECE): ")
    dname=input("Department name(full name): ")
    batchList=[]   
    with open ("batch.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[2]==did):
                batchList.append(row[0])
    ddetails=[did,dname,str(batchList)]
    with open ("department.csv","a") as fhand:
        csvWriter=csv.writer(fhand)
        csvWriter.writerow(ddetails)
def viewBatches():
    did=input("Enter the id of the department: ")
    batchList=[]
    with open("department.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if(row[0]==did):
                batchList=eval(row[2])
        print("Batch ID                     Batch Name")
        for element in batchList:
            with open("batch.csv", "r") as fhand:
                csvReader = csv.reader(fhand)
                for row in csvReader:
                    if(row[0]!="Batch ID"):
                        if(element==row[0]):
                            print(row[0]+" "*(29-len(row[0]))+row[1])
def viewAvgPerformance():
    did=input("Enter the id of the department: ")
    print("BATCH ID               AVERAGE PERFORMANCE")
    with open ("department.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        batchList=[]
        for row in csvReader:
            allBatchMarks=0
            countBatch=0
            if(row[0]==did):
                batchList=eval(row[2])
                for batch in batchList:
                    countStudent=0
                    allStudentMarks=0
                    with open("student.csv","r") as fhand:
                        csvReader=csv.reader(fhand)
                        for row in csvReader:
                            if(batch==row[3]):
                                sid=row[0]
                                marksDict = {}
                                oneStudentMarks = 0
                                count = 0
                                with open("course.csv","r") as fhand:
                                    csvReader=csv.reader(fhand)
                                    for row in csvReader:
                                        if(row[2]=="marks"):
                                            continue
                                        else:
                                            marksDict=eval(row[2])
                                            for key,value in marksDict.items():
                                                if(sid==key):
                                                    oneStudentMarks=oneStudentMarks+int(value)
                                                    count=count+1
                                    if(count!=0):
                                        oneStudentMarks=oneStudentMarks/count
                                allStudentMarks=allStudentMarks+oneStudentMarks
                                countStudent=countStudent+1
                        if(countStudent!=0):
                         allStudentMarks=allStudentMarks/countStudent
                         print(batch+" "*(23-len(batch))+str(allStudentMarks)+"%")
def linePlot():
    plotValue=[]
    plotLabel=[]
    did = input("Enter the id of the department: ")
    with open("department.csv", "r") as fhand:
        csvReader = csv.reader(fhand)
        batchList = []
        for row in csvReader:
            allBatchMarks = 0
            countBatch = 0
            if (row[0] == did):
                batchList = eval(row[2])
                print(batchList)
                for batch in batchList:
                    countStudent = 0
                    allStudentMarks = 0
                    with open("student.csv", "r") as fhand:
                        csvReader = csv.reader(fhand)
                        for row in csvReader:
                            if (batch == row[3]):
                                sid = row[0]
                                print(sid)
                                marksDict = {}
                                oneStudentMarks = 0
                                count = 0
                                with open("course.csv", "r") as fhand:
                                    csvReader = csv.reader(fhand)
                                    for row in csvReader:
                                        if (row[2] == "marks"):
                                            print("marks detected")
                                            continue
                                        else:
                                            marksDict = eval(row[2])
                                            print(marksDict)
                                            for key, value in marksDict.items():
                                                if (sid == key):
                                                    oneStudentMarks = oneStudentMarks + int(value)
                                                    print(oneStudentMarks)
                                                    count = count + 1
                                    if (count != 0):
                                        oneStudentMarks = oneStudentMarks / count
                                        print(oneStudentMarks)
                                allStudentMarks = allStudentMarks + oneStudentMarks
                                countStudent = countStudent + 1
                        if (countStudent != 0):
                            allStudentMarks = allStudentMarks / countStudent
                            print(f"{batch} performance {allStudentMarks}")
                            plotValue.append(allStudentMarks)
                            plotLabel.append(batch)
    print(plotLabel,plotValue)
    plt.title("DEPARTMENT STATISTICS(LINE PLOT)")
    plt.ylabel("Average performance")
    plt.xlabel("Batches")
    plt.plot(np.array(plotLabel),np.array(plotValue))
    plt.show()
def viewDepartment():
    with open ("department.csv","r") as fhand:
        csvReader=csv.reader(fhand)
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")
        for row in csvReader:
            print(row[0]+" "*(20-len(row[0]))+row[1]+" "*(60-len(row[1]))+str(row[2]))
        print("------------------------------------------------------------------------------------------------------------------------------------------------------")

def departmentDb():
    choice=0
    while(choice!=6):
        choice=int(input("Enter 1)CREATE A NEW DEPARTMENT, 2)VIEW ALL BATCHES IN A DEPARTMENT, 3)VIEW AVERAGE PERFORMANCE OF ALL BATCHES IN A DEPARTMENT, 4)VIEW DEPERTMENT STATISTICS(LINE PLOT) 5)VIEW DB 6)BACK! "))
        match choice:
            case 1:
                addDepartment()
            case 2:
                viewBatches()
            case 3:
                viewAvgPerformance()
            case 4:
                linePlot()
            case 5:
                viewDepartment()
            
def addExam():
    cid=input("Enter the course id to know the performances of all students: ")
    with open ("course.csv", "r") as fhand:
        csvReader=csv.reader(fhand)
        for row in csvReader:
            if (row[0]==cid):
                print("EXAMINATION NAME:",row[1])
                print("STUDENT ID               NAME                      MARKS")
                marksDict=eval(row[2])
                for key,value in marksDict.items():
                    with open ("student.csv", "r") as fhand:
                        csvReader=csv.reader(fhand)
                        for row in csvReader:
                            if(key==row[0]):
                                print(row[0]+" "*(25-len(row[0]))+row[1]+" "*(26-len(row[1]))+str(value))
def scatterPlot():
    plotValues = []
    plotLabels = []
    with open("course.csv", "r") as fhand:
        csvReader = csv.reader(fhand)
        for row in csvReader:
            if(row[2]!="marks"):
                marksdict = eval(row[2])
                for key, value in marksdict.items():
                    with open("student.csv", "r") as fhand:
                        csvReader = csv.reader(fhand)
                        for row in csvReader:
                            if (key == row[0]):
                                plotValues.append(value)
                                plotLabels.append(row[3])

        plt.scatter(plotLabels,plotValues)
        plt.title("SCATTER PLOT")
        plt.xlabel("Batches")
        plt.ylabel("Marks")
        plt.show()
def examinationDb():
    choice = 0
    while (choice != 3):
        choice = int(input("Enter 1)VIEW THE PERFORMANCE OF ALL STUDENTS IN A EXAMINATION, 2)SCATTER PLOT, 3)BACK! "))
        match choice:
            case 1:
                addExam()
            case 2:
                scatterPlot()
#Database choice
def choice():
    choice=0
    while(choice!=6):
        choice=int(input("Enter 1)STUDENT DB, 2)COURSE DB, 3)BATCH DB, 4)DEPARTMENT DB 5)EXAMINATION 6)BACK! "))
        match choice:
            case 1:
                studentDb()
            case 2:
                courseDb()
            case 3:
                batchDb()
            case 4:
                departmentDb()
            case 5:
                examinationDb()
choice()