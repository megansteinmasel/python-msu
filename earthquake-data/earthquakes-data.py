# --------------------------------------
# Megan Steinmasel                     |
# Feb 25, 2021                         |
# Earthquake data                      |
# --------------------------------------

import csv

def average_magnitude(file_name):
    m = 0 
    count = 0
    
    with open("earthquakes.csv","r") as infile:
        csvdict = csv.DictReader(infile)
        
        for row in csvdict:
            m += float(row["magnitude"])
            count = count + 1
            
    total = (m/count)
    return(total)
    
    

def earthquake_locations(file_name):
    l = []
    count = 0
    c = []
    with open(file_name, newline = '') as infile:
        csvdict = csv.DictReader(infile)
        
        for row in csvdict:
            data = (row["name"])

            if data not in l:
                l.append(data)
                count = count + 1
                c.append(count)
            l.sort()
        for i in range(len(l)):
            print(c[i], "-", l[i])
            
        print(" ")
                
        
            
             
        
def count_earthquakes(file_name, lower_bound, upper_bound):
    count = 0
    with open("earthquakes.csv","r") as infile:
        csvdict = csv.DictReader(infile)
        for row in csvdict:
            data = float(row["magnitude"])
            if lower_bound <= data <= upper_bound:
                count = count + 1
        return(count)


# --------------------------------------

def main(file_name):
    magnitude = average_magnitude(file_name)
    print("The average earthquake magnitude is {:.2f}\n".format(magnitude))
    
    earthquake_locations(file_name)
    
    lower_bound = float(input("Enter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(file_name, lower_bound, upper_bound)
    print("Number of recorded earthquakes between {:.2f} and {:.2f} = {:d}".format(lower_bound, upper_bound, how_many))

# --------------------------------------

main("earthquakes.csv")
