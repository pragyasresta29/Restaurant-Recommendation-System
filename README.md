# Restaurant-Recommendation-System
A recommendation model built in python which recommends restaurants to user based on their preferences.
The project used a scaled down version of Yelp Dataset available from the website of Kaggle. Since, the yelp dataset consists of reviews and business information of businesses other than restaurants, the dataset was further cleaned up by removing irrelevant data.

## Recommendation Model
The recommendation model is based on the similarity score which is calculated using Pearson’s correlation coefficient. In this system, Pearson’s correlation coefficient was used to calculate the similarity between users and generate recommendation based on the similarity. The recommendation model worked with decent accuracy of 80.71%. 

## Working
In the getRecommendations.py file we first load the dataset(reviews,restaurants) into dictionary named prefs. Prefs can be considered as a critics for generating recommendations for users. To get recommendations from users we use the getRecommendation function by passing the user id of the user for which we wish to get Recommendation. The function will return a list of recommendations of restaurants with their predicted rating by the user for that restaurant. 

Note: The model will not return recommendation if there is not enough reviews for users. 
