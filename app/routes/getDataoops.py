
# coding: utf-8

# In[9]:


#Import the pandas library to read csv files
import pandas as pd


# In[10]:


# Read the csv file which acts as the input
data_csv = pd.read_csv("./final_data.csv")
#Convert the file in a DataFrame
data = pd.DataFrame(data_csv) 


# In[15]:


#The type of data and its values
data.head()


# In[28]:


#This is the Grading System Class
class GradingSystem:
    #This is the constructor, where the student is an object
    #Set the registration Number and initialize the objects properties
    def __init__(self,regNumber):
        self.regNumber = regNumber
        self.final_grade = ""
        self.Name = "" 
    #This a class method, used to find marks, only the object is passed
    def findMarks(self):
        extraCurMarks = 0
        redMarks = 0
        reg = self.regNumber
    #Set the name of the object, using the registration number
        self.Name = data.at[reg, 'Name']
    #Calculate mid-sem, sem-end, project marks    
        cesMarks = (data.at[reg,'CES1'] + data.at[reg,'CES2'] + data.at[reg,'CES3']) 
        SemEndMarks = (data.at[reg,'SEE1'] + data.at[reg,'SEE2'] + data.at[reg,'SEE3'])
    #Calculate total marks, divide by number of subjects
        totalmarks = (cesMarks + SemEndMarks)
        percentage = (totalmarks/150)*100
        cgpa =percentage/9.5
        self.percentage= percentage
        self.cgpa=round((percentage/9.5),1)
        self.totalmarks = round(totalmarks)
        return

    def getGrade(self):
    #This method calculates the grade of the object
    #Only the object is passed, all attributes are extracted
    # from the object
        reg = self.regNumber
        marks = self.totalmarks
        percentage= self.percentage
        cgpa=self.cgpa
        if(cgpa <= 4):
            data.at[reg,'CGPA'] = cgpa
            data.at[reg,'Grade'] = 'F'
            return 'F'
        if(4 < cgpa <= 5):
            data.at[reg,'CGPA'] = cgpa
            data.at[reg,'Grade'] = 'C'
            return 'C'
        if(5 < cgpa <= 6):
            data.at[reg,'CGPA'] = cgpa
            data.at[reg, 'Grade'] = 'C+'
            return 'C+'
        if(6 < cgpa <= 7):
            data.at[reg,'CGPA'] = cgpa
            data.at[reg, 'Grade'] = 'B'
            return 'B'
        if(7 < cgpa <= 8):
            data.at[reg,'CGPA'] = cgpa
            data.at[reg,'Grade'] = 'B+'
            return 'B+'
        if(8 < cgpa <= 9):
            data.at[reg,'CGPA'] = cgpa
            data.at[reg, 'Grade'] = 'A'
            return 'A'
        if(9 < cgpa <= 10):
            data.at[reg,'CGPA'] = cgpa
            data.at[reg, 'Grade'] = 'A+'
            return 'A+'
            


# In[29]:


class main:  
    def genData():
    #Generate the grades for all the students using marks at once.
        for i in range(1,101):
            regNumber = i
            Student = GradingSystem((regNumber-1))
            Student.findMarks()
            Student.getGrade()        


# In[30]:


main.genData()


# In[32]:


data.to_json("text.json", orient='records')

