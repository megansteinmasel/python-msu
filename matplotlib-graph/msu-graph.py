# -------------------------------------------------
# CSCI 127                                        
# April 8, 2021                                   
# Megan Steinmasel                                
# -------------------------------------------------
#Creates an enrollment bar graph of the subcolleges


import numpy as np
import matplotlib.pyplot as plt
import csv

#--------------------------------------------------
#Creates arrays of college name and enrollment numbers & returns them

def read_file(file_name):
    file = open(file_name,"r")
    
    lineone = file.readline()
    
    namelist = []
    enrollmentlist = []
    
    for line in file:
        line = line.strip('\n')
        s = line.split(",")
        
        enrollmentlist.append(float(s[0]))
        namelist.append(s[1])
        
    college_names = np.array((namelist))
    college_enrollments = np.array((enrollmentlist))
    
    return(college_names,college_enrollments)
            
        
# -------------------------------------------------
#Creates the bar graph

def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    
    plt.figure(num='MSU Enrollments')
    plt.bar(college_names, college_enrollments, color= ['Yellow', 'Blue', 'Yellow', 'Blue', 'Yellow', 'Blue'])


    plt.yticks(np.arange(0,5001, 1000))

    plt.xlabel("College")
    plt.ylabel("Enrollment")
    plt.title("Fall 2020")
    
    plt.show()
# -------------------------------------------------

main("fall-2020.csv")
