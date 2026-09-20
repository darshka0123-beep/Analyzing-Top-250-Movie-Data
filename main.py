import pandas as pd
import matplotlib.pyplot as plt

pd.set_option( 'display.max_columns', None)
pd.set_option('max_colwidth', None)

#Top 100 IMDb movies dataset csv
movieData = pd.read_csv('IMDb Top 250 Movies.csv')
#csv stands for comma seperated values that stores data like spreadsheets. Each line represents a row of data. Individual columns are seperated by a comma. 
favMovie = "Spirited Away"
print("My favorite movie is " + favMovie + ".")

# print(movieData.head())
# print(movieData["movie_title"])

#Filter Data
print("\nThe data for my favorite movie is:\n")

# Create a new variable to store your favorite movie information
fav_movie_boolean_list = movieData["name"] == favMovie
#print(fav_movie_boolean_list)

favMovieData = movieData.loc[fav_movie_boolean_list]
print(favMovieData)

print("\n\n")
# what that mean: \n creates a new line break. Two \n's mean two new line breaks. 

#Create a new variable to store a new data set with a certain genre
average_movie_rating_list = movieData["rating"].mean()
print("The average movie rating for this dataset is " + str(average_movie_rating_list))

adventuremoviebooleanlist = movieData["genre"].str.contains("Adventure")
adventuremoviedata = movieData.loc[adventuremoviebooleanlist]

numOfMovies = adventuremoviedata.shape[0]

print("We will be comparing " + favMovie + " to other movies under the Adventure genre in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Adventure.")

print("..............................................................................\n")
input("Press enter to see more information about how " + favMovie + "compares to other movies in Adventure.\n")

#minimum rating
min_rating = adventuremoviedata["rating"].min()
print("The highest audience rating of the data set is: " + str(min_rating))
min_difference = 8.6 - min_rating
print(favMovie + " is " + str(min_difference) + " higher than the lowest rating in the adventure genre.")

# maximum rating
max_rating = adventuremoviedata["rating"].max()
print("The lowest audience rating of the data set is " + str(max_rating))
max_difference = max_rating - 8.6
print(favMovie + " is " + str(max_difference) +" lower than the highest rating in the adventure genre. ")
print()

# find mean
mean = adventuremoviedata["rating"].mean()
print("The mean audience rating of the data set it: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median

median = adventuremoviedata["rating"].median()
print("The median audience rating of the data set is: " +str(median))
print(favMovie + " is higher than the median movie rating." )

print("................................................................")
input("Press enter to see data visualizations. \n")

# Part 6 Create graphs
# Create histogram
plt.hist(movieData["rating"], range = (8,10), bins = 20)
# whats a bins (=20): bins are what the x axis goes by or what every dash is worth

# Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Top 250 Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Movies")

#Prints interpration of Histogram
print(
    "According to the histogram, most movies fall under the rating from 8 to 10. The shape of the histogram is a skewed bell curve which shows that it is not likely normally distributed. "
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")
plt.close()

# Convert string values to float/int
movieData["budget"] = pd.to_numeric(movieData["budget"], errors="coerce")
movieData["box_office"] = pd.to_numeric(movieData["box_office"], errors="coerce")

#Create Scatterplot
plt.scatter(data = movieData, x= "budget", y= "box_office")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Budget vs Box Office")
plt. xlabel("Budget")
plt.ylabel("Box Office")


# Prints interpreatation of scatterplot
print("According to the scatter plot, there is a positive correlation with two extreme outliers that have compressed the main cluster against the y axis.")
print() 

plt.show()
print("\nThank you for reading through my data analysis!")

