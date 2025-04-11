# Real-Estate-Recommender-System-and-Analytics
Our real estate website provides city-level analytics, including spatial analysis, price distribution, and feature word clouds. It features a price prediction module based on property attributes, a recommender system for similar apartments, and insightful visualizations, all websites made with help of streamlit are deployed on AWS using to help users make informed property decisions.

<p align="center">
  <img src="https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/a5520829-27fb-4928-b7b0-941028233030" alt="test1">
</p>


# 1. Introduction:
Our project is a real estate platform that leverages analytics, price prediction, and recommendation systems to help users make informed property decisions through visual insights and data-driven predictions. Real Estate Recommender website deployed on AWS -> http://13.48.57.211:8501

# 2 Webscrapping
I have done webscrapping on 99acres.com to extract infomration about city named Gurgaon. I have uploaded the webscrapping code. We all extracted following datasets after webscrapping which includes : Independent house, Residential land, Flats and Real Estate data (data of societies)

# 2. Description of the dataset:
We have 5 datasets files.

#### 2.1 Shape of our dataset:
Our flat dataset has 3017 rows and 20 columns.

![Image](https://github.com/user-attachments/assets/9e5dad21-5c40-4071-bec8-8636215ee255)

Our Independent houses dataset has 

![Image](https://github.com/user-attachments/assets/9323d500-2275-4151-a035-85d8a49e2fa0)

![Image](https://github.com/user-attachments/assets/166eed51-c0eb-4600-9ea1-5cdbe75f2df7)

# 3. Preprocessing and Data Cleaning for EDA

#### 3.1 Detecting Null values in our dataset:

![Screenshot 2024-05-22 132813](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/667e87e4-f5cc-4458-b100-74d6e5615383)

There are 2 each null values in Smokes and Alkhol columns. There is one null value in Age column. 


# 4. Exploratory Data Analysis

#### 4.1 Overview of dataset using statistics:

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/d5b38c22-cae2-4f8d-bc3c-689f69cd1e0e)

Approximately 50% people who smoke are below age 40. This group smokes approximately 15 cigarettes and consumes 3 drinks a day.

#### 4.2 Comprehensive Analysis of Age, Smoking, and Drinking Habits in Relation to Lung Cancer

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/fac4d932-0f9e-4e67-92ce-a12f6a772892)

![test2](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/8386c7e2-061d-4726-8895-e3ba806526cb)

![test3](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/bad18162-dc2c-42ed-8791-96f5aa8e602b)

![test4](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/3d5ac5ba-a32c-4a7a-be50-b460175fea68)

Fig a : Majority of the people in our dataset are from age groups 20 to 39.

Fig b : Approximately 19 cigarettes are smoked by people of age group 50 to 59.

Fig c : Approximately 33% people take 2 to 3 drinks per day

Fig d : From our barplot, we come to know that majority of people do both smoking and drinking.

Fig e : Majority of people affected by Lung cancer are approximately above age 47.

Fig f : There is an outlier in our dataset where a user smokes approximately 35 cigarettes at the age of 27. 

Fig g : Our data appears to be scattered.

Fig h : We plotted a box plot to visually analyze the distribution and spread of the 'Age' and 'Smokes' variables in the dataset. We were not able to see any outliers in our plot


# 5. Polishing our data for model training

#### 5.1 Outlier detection and treating using Z-score

Shape of our original dataset :

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/4b8baa6b-60e4-450a-920e-58fdb2c0ac41)

Shape after treating outliers :

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/4b8baa6b-60e4-450a-920e-58fdb2c0ac41)

No outliers were detected.

#### 5.2 One-Hot Encoding :

We are doing One-Hot Encoding to convert categorical variables are converted into binary vectors.

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/a50eb7dc-4034-45dc-8983-5174475de613)

#### 5.3 Standarization

We need to bring all the values of each column onto a common scale which will help us to train our model effiency.

Our x_train after standarization :

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/32f9a6dc-f184-416f-b549-c5d932e08c8b)

Our x_test after standarization :

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/211856bb-5483-44fc-89f3-3e73e115cb6c)

# 6. Model Building and Model Evaluation

#### 6.1 Calculating accuracy of our models

We used Logisitc Regression, Decision Tree, Random Forest and Support Vector Machine to train our model.

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/f34ccbe2-42eb-4649-b02c-f0fd63d79669)

We are getting high accuracy for all four of our machine learning models.

#### 6.2 Calculating Precision, R2 score and F1 score

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/0334b109-77ea-4066-b53b-1d762ae4d107)

Precision, Recall and F1-score of all our four models is excellent

#### 6.3 Calculating confusion Matrix

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/0f901358-70a9-4269-b579-cdf7b34dcf48)

Our confusion matrix is working well


# 7. Actual vs. Predicted Values:

![test1](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/17bcb751-e8d8-4178-a098-0bf4fb54fc2d)

![test2](https://github.com/Mervin50/ML_Project2_LungCancer_Classification/assets/167336864/8286ab87-7994-4748-a256-631d6bf03da1)


# 8. Conclusion : 

1. Lung cancer is caused among people who are above approximately 39 years old.
2. All the 4 models : Logisitc Regression, Decision Tree, Random Forest and Support Vector Machine used provided high accuracy.


















