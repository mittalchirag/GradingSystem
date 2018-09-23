
# coding: utf-8

# In[3]:


#Import the pandas library to read csv files
import pandas as pd


# In[8]:


# Read the csv file which acts as the input
data_csv = pd.read_csv("./final_data.csv")
#Convert the file in a DataFrame
data = pd.DataFrame(data_csv)


# In[12]:


def getGrade(regNumber,cgpa):
   #This method calculates the grade of the object
   #Only the object is passed, all attributes are extracted
   # from the object
       reg = regNumber
       if(cgpa <= 4):
           data.at[reg,'CGPA'] = cgpa
           data.at[reg,'Grade'] = 'F'
       if(4 < cgpa <= 5):
           data.at[reg,'CGPA'] = cgpa
           data.at[reg,'Grade'] = 'C'
       if(5 < cgpa <= 6):
           data.at[reg,'CGPA'] = cgpa
           data.at[reg, 'Grade'] = 'C+'
       if(6 < cgpa <= 7):
           data.at[reg,'CGPA'] = cgpa
           data.at[reg, 'Grade'] = 'B'
       if(7 < cgpa <= 8):
           data.at[reg,'CGPA'] = cgpa
           data.at[reg,'Grade'] = 'B+'
       if(8 < cgpa <= 9):
           data.at[reg,'CGPA'] = cgpa
           data.at[reg, 'Grade'] = 'A'
       if(9 < cgpa <= 10):
           data.at[reg,'CGPA'] = cgpa
           data.at[reg, 'Grade'] = 'A+'
def findMarks(regNumber):
   #Calculate mid-sem, sem-end, project marks  
       reg = regNumber
       cesMarks = (data.at[reg,'CES1'] + data.at[reg,'CES2'] + data.at[reg,'CES3']) 
       SemEndMarks = (data.at[reg,'SEE1'] + data.at[reg,'SEE2'] + data.at[reg,'SEE3'])
   #Calculate total marks, divide by number of subjects
       totalmarks = (cesMarks + SemEndMarks)
       percentage = (totalmarks/150)*100
       cgpa =percentage/9.5
       cgpa=round((percentage/9.5),1)
       totalmarks = round(totalmarks)
       getGrade(regNumber,cgpa)
       return

def genData():
       for i in range(1,101):
           regNumber = i
           findMarks((regNumber-1)) 


# In[13]:


def main():
    genData()


# In[14]:


main()


# In[16]:


# Method to store data
data.to_json("testImp.json", orient='records')

