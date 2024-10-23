## Project overview
The real estate company Immo Eliza wants to establish itself as the biggest Belgian real estate services provider. 
 To achieve that goal, they need to more accurately and faster than their competitors estimate the value of properties, 
 to pick out those properties that are most valuable to them and their clients.
Enter creating a machine learning model to predict the prices of properties across Belgium. Having no in-house data scientists, 
 they are looking for talented people to do it for them. Since our last encounter with them went great, they continue 
 to rely on us to do the job. Everything is in our hands now!

By the end of this week, Immo Eliza's management wants to see a preliminary analysis based on the dataset we previously 
scraped. The management has no technical background. Broadly speaking, they have two main questions:
    What are currently the most interesting insights about the Belgian real estate market?
    What variables are the most important when determining the price of a property?

## Dataset description and sanitization 
The original scraped dataset is from the project repo of Kelli Griffin https://github.com/kgriff21/immoeliza_scraping
10,000+ listings were scraped based on 17 different property parameters. Upon analysis of these data, the data was 
further sanitized by dropping the column "Number of facades" as we concluded this would not bring valuable information
to the final analysis. Additionally, there were many missing values for this criteria.
We decided to drop rows with Nan in specific columns without assignment for Living area m², Number of bedrooms and 
Building condition. Retaining the NaN values in the dataset would hinder the quality of the final analysis, as these 
missing values pertain to important criteria necessary for drawing meaningful conclusions.
The data was also sorted by price to include a cutoff of listings over 1 million euros to exclude outliers skewing the 
analysis. The top 16 listings were excluded and considered as 'bad data' because these houses/apartments were for sale with
a monthly annuity. However, the pre-sorted analysis (excluding bad data properties) was used for outlier conclusion visualizations. 

In total, we have 15 features of 9033 listings. The proportion of missing values is as follows:

Garden area m²:                0.714381

Terrace surface m²:            0.519097

Number of facades:             0.295140

The other property features give 0% missing values. 

The final sanitized property listings data can be found here: Data/Cleaned/sanitized_property_listings_Kelli_final.csv

## Repo and directory structure
The repo can be found here: https://github.com/Kevin-Van-Hoorebeek/immoeliza_data_analysis/tree/main

Analysis: To view data analysis and notebooks from each team member.

Archive: Contains pre-completed sanitized data.

Data: Contains two subfolders 1. Cleaned with the final csv of sanitized data which was used for the analysis 2. 
Raw folder which contains a csv file from Vanessa and the original scraped csv from Kelli (obtained from previous 
section of the project).

.gitignore: Containing files and directories that Git should ignore when tracking changes in the repository.

requirement.txt: Containing necessary library installations to run the code.

README.md: Project overview 


## Dependencies/Installation
The required packages and libraries to successfully run this code and be installed via the requirements.txt

## Group contributions
This was a group effort by Anastasiia Korostelova, Kelli Griffin (team lead), Kevin Van Hoorebeek (repo manager), 
Maarten Warnez and Yeliz Kaya.
Each person was assigned questions to answer about the data and produce visualizations to present to the class.

Kevin Van Hoorebeek and Kelli Griffin were assigned the questions: How many qualitative and quantitative variables are there? 
How would you transform the qualitative values into numerical values? What variables are most subject to outliers?

Anastasiia Korostelova: What are the least/most expensive municipalities in Belgium/Wallonia/Flanders? (in terms of 
price per m², average price, and median price)

Maarten Warnez: How are the variables themselves correlated to each other? Can you find groups of variables that are 
correlated together?

Yeliz Kaya: What is the correlation between the variables and the price? Why do you think some variables are more 
correlated than others? 

## Results
The visual graphs and images were presented to the
class.
https://docs.google.com/presentation/d/1eiQeFjKJOGb96rREQTS7X82Ly_EIRpRAhyQ2701bf-4/edit?usp=sharing

## How to run the code
The final conclusions from each team member have been collected in a notebook: Analysis/data_analysis_final_all.ipynb
The notebook is divided into sections based on each individuals work.



