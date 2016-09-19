#HW2

For this assignment I worked individually on all sections and used the sample ipython notebooks in Lab 2 and the Data Wrangling folder as reference.

#Assignment Overview:

In assignment 1 I wrote a python script that when executed on the command line along with a valid MTA API key and bus line, will request a json type file containing all info relating to that particular bus line. The script then parses the json file stored as a python dictionary for the total number of buses on the line and the longitude and latitude related to each individual bus on the line. These values are output on the screen using the "print()" command. As the call information is not relevant to assignment 1, the detail level requested of the API is set to "normal" rather than "calls".

In assignment 2 I wrote a similar python script to assignment 1 that is executable on the command line. In addition to requiring a valid MTA API key and bus line, the name of a .csv where outputs are to be saved must also be specified. The script requests a similar json file as before, the only difference being the detail level requested is set to "calls" to allow the scraping of "Onward Calls" information relating to future stops. The json file is again parsed for longitude and latitude, and additionally parsed for the stop name and stop status of the next stop for each individual bus. These values are output separated by the appropriate commas and "\n" symbols into a text file, which is saved under the file name specified on the command line.

In assignment 3 I found the data set "Natural Gas Consumption by ZIP Code - 2010" within the CUSP data facility and wrote a jupyter notebook that loads the associated .csv file stored on the data facility as a pandas data frame, displays the first 10 rows of the data frame, removes all but the two columns containing numerical values, and creates a scatterplot of the remaining columns.
