import numpy as np              #we Import the Numpy library.
note = " "
first_row= np.array(["name", "total", "percent", "note"])               #will be the first line to display column names and make the table easier to read
while True:
    try:
        #Ask the user to enter the number of students and the number of subjects.
        nbr_student = int(input("entry  the number of students "))
        nbr_subjects = int(input("entry  the number of subjects "))
        array = []          #array is a list to contain student data
        array.append(first_row)
        
        for student in range (1, nbr_student +1):           #loop to browse over all students to retrieve their data
            
            student_mark = []                       # student_mark will take the name as well as the notes and the list_mark will take only the notes in order to be able to perform operations on them.
            list_marks = []
            name = input(f"enter student name {student} : ")
            student_mark.append(name)                   #we start adding the student's name to the list student_mark
           
            for subject in range(1, nbr_subjects +1):       #loop to browse over all subjects to retrieve their notes
                mark = int(input(f"enter the {name} 's rating for subject {subject} : "))
                
                if mark > 0 :        #an if/else loop to check that the notes entered are positive
                    list_marks.append(mark)
                else:
                    print("a negative score is considered zero !")
                    break
                
            total_mark =np.sum(list_marks)                  #total_mark is assigned the sum of each student's marks
            percent = (total_mark / (nbr_subjects * 100)) * 100     #Calculate the percentage for each student using the total marks
           
            if (percent < 50):                              #loop if/else to Calculate the grade for each student using the percentage
                note = "F"
            elif (50 <= percent < 60):
                note = "C"
            elif (60 <= percent < 70):
                note = "B"
            elif (70 <= percent < 80):
                note = "B+"
            elif (80 <= percent < 90):
                note = "A"
            else:
                note = "A+"
                
                
            student_mark.append(total_mark)                         #we add the total scores and percentages to the student_mark list
            student_mark.append("{0:.2f}".format(percent))          #this format allows only two digits after the decimal point
            student_mark.append(note)
            
            array.append(student_mark)                              #we add each student's information to the array list before transforming it into an array
            new_array = np.array(array)
        print("here is the table of notes for students : ")         #display the table of notes for students
        print(new_array)
            
    except ValueError :                                             #the except block  manages the error
        print('Error, your entry must be a whole number !')
        continue
    break


   