import csv
import numpy as np
import matplotlib.pyplot as plt


def get_data(column, filename):
  """ Read 1 column of covid data from a csv file.
      Return data as an array.
      : param column : column to extract
                       0 : date
                       1 : new_cases
                       2 : new_deaths
                       3 : total_cases
                       4 : total_deaths
                       5 : weekly_cases
                       6 : weekly_deaths
                       7 : biweekly_cases
                       8 : biweekly_deaths
      : param file : csv file
  """
  reader = csv.reader(open(filename), delimiter=',')
  data= list(reader) # read the data as a list
  lst = []          
  # Extract the selected column. Skip 1st line (the column description)
  for item in data[1:]:
      lst.append(item[column])
  # Convert the list to a float array    
  return np.array(list(map(lambda x: float(x),lst)))    

def rem_zeros(data):
  """ Convert the array data to a list of list of format
      : param data : array([v0,v1,v2,... vn])
      : return : [[d1,v1],[d2,v2],... [dn,v]] all the null vi<=0 have been removed
  """
  lst = []
  for i in range(len(data)):
    if data[i] > 0:
      lst.append([i,data[i]])
  return(lst)    

# The list of dsescription of each column in the data file.
# This can be used to generate labels in a graphics.
Names = ["date","new_cases","new_deaths","total_cases","total_deaths",\
         "weekly_cases","weekly_deaths","biweekly_cases","biweekly_deaths" ]


if __name__ == "__main__":
  col = 1             # Selected column: new daily infections
  data = get_data(col,"covid_JuneJuly2021.csv")
  # print(data)
  plt.semilogy(data)
  plt.ylim([1e3,1e5]) # This generates nicer y labels
  plt.xlabel("days since June 1 2021", fontsize=20)
  plt.ylabel(Names[col], fontsize=20)
  
  # Make the layout large enough to fit large labels
  plt.tight_layout(rect=[0, 0, 1, 1])
  plt.show()

