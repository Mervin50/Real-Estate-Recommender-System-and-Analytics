# Real-Estate-Recommender-System-and-Analytics [Link](http://localhost:8501/)
Our real estate website provides city-level analytics, including spatial analysis, price distribution, and feature word clouds. It features a price prediction module based on property attributes, a recommender system for similar apartments, and insightful visualizations, all websites made with help of streamlit are deployed on AWS using to help users make informed property decisions.

<p align="center">
  <img src="https://github.com/user-attachments/assets/4219a9fd-3b92-4ad3-b5b8-4ba4ce1f1abf" alt="test1"
</p>


# 1. Introduction:
Our project is a real estate platform that leverages analytics, price prediction, and recommendation systems to help users make informed property decisions through visual insights and data-driven predictions. Real Estate Recommender [website](http://localhost:8501/) deployed on AWS.

# 2 Webscrapping
I have done webscrapping on 99acres.com to extract infomration about city named Gurgaon. I have uploaded the webscrapping code. We all extracted following datasets after webscrapping which includes : Independent house, Residential land, Flats and Real Estate data (data of societies)

# 3. Description of the dataset:
We have 5 datasets files.

#### 3.1 Shape of our dataset:
Our flat dataset has 3017 rows and 20 columns.

![Image](https://github.com/user-attachments/assets/9e5dad21-5c40-4071-bec8-8636215ee255)

Our Independent houses dataset has 1095 rows and 21 columns.

![Image](https://github.com/user-attachments/assets/166eed51-c0eb-4600-9ea1-5cdbe75f2df7)

We have cleaned both the above datasets and merged them into one named as Gurgaon Properties

![Image](https://github.com/user-attachments/assets/f096c7bf-989f-46b3-ba8d-fb03085fc2ac)

# 4. Feature Engineering 

We have extracted buildup area values and convert it into square meter.  

![Image](https://github.com/user-attachments/assets/f85a8659-92a0-4cfb-9874-f67d2c743316)

We have populated columns 'study room', 'servant room', 'store room', 'pooja room', 'others' into newly created column named additional room column

![Image](https://github.com/user-attachments/assets/84a3ffe6-5cdd-4aff-a588-55c442759d09)

We categorized the agePossession column based on property age or possession time. Missing or unclear values were labeled as "Undefined" or "Under Construction."

![Image](https://github.com/user-attachments/assets/7d4516bd-b404-4672-a6a4-7970a23a15fe)

We extracted all unique furnishing items from the furnishDetails column and cleaned their names.
Then, for each furnishing, we created new columns showing how many of each item is present.

![Image](https://github.com/user-attachments/assets/cfa0c80d-f01e-4c6f-b302-78857bd0f2d2)

After that, we have used standard scaler on above furnishing column. ALso, we have used elbow method to find optimum number clusters for k-means

# 5. Exploratory Data Analysis

#### 5.1 Overview of dataset using Univariate Analysis:

![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/ec5d4df7-eaaf-4d9b-af21-fdc368f71e88)

Figure1 Observation : The dataset is dominated by flats, making up the majority of listings.
Houses have significantly fewer listings, indicating a flat-heavy market.

Figure2 Observation: Most properties are listed as "independent," showing a high preference for standalone homes.
Among societies, "Tulip Violet" and "SS The Leaf" are the most popular, indicating strong demand for premium housing communities.

Figure3 Observation: The table shows the number of listings for each housing society.
Popular societies like Tulip Violet and SS The Leaf have the highest number of listings, indicating high activity or demand.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/28d1ce17-6410-4af7-9d2e-675b80625e1d)

![Screenshot 2025-04-11 052936](https://github.com/user-attachments/assets/3f35ab42-dd32-46dc-8a91-0d8d9456eb14)

Figure1 Observation: The majority of property listings are concentrated around Sohna Road, followed by sectors like 85, 102, and 92.
This suggests these areas are the most active or in-demand real estate zones in the dataset.

Figure2 Observation: Majority Prices of the real estate is between 0 to 5cr.

Figure3 Observation Observations:
Descriptive Statistics:
Count: There are 3,660 non-missing price entries.
Mean Price: The average price is approximately 2.53 crores.
Median Price: The median (or 50th percentile) price is 1.52 crores.
Standard Deviation: The prices have a standard deviation of 2.98, indicating variability in the prices.
Range: Prices range from a minimum of 0.07 crores to a maximum of 31.5 crores.
IQR: The interquartile range (difference between 75th and 25th percentile) is from 0.95 crores to 2.75 crores.

Visualizations: Distribution: The histogram indicates that most properties are priced in the lower range (below 5 crores), with a few properties going beyond 10 crores.
Box Plot: The box plot showcases the spread of the data and potential outliers. Properties priced above approximately 10 crores might be considered outliers as they lie beyond the upper whisker of the box plot.

Figure 4 Observation: Skewness: The price distribution has a skewness of approximately 3.28, indicating a positive skew. This means that the distribution tail is skewed to the right, which aligns with our observation from the histogram where most properties have prices on the lower end with a few high-priced properties.

Kurtosis: The kurtosis value is approximately 14.93. A kurtosis value greater than 3 indicates a distribution with heavier tails and more outliers compared to a normal distribution.


![Image](https://github.com/user-attachments/assets/433da5a2-6687-4565-a7c6-f650b3b2eff3)             

Observations: 
Quantile Analysis:
1% Quantile: Only 1% of properties are priced below 0.25 crores.
5% Quantile: 5% of properties are priced below 0.37 crores.
95% Quantile: 95% of properties are priced below 8.5 crores.
99% Quantile: 99% of properties are priced below 15.26 crores, indicating that very few properties are priced above this value.

![Image](https://github.com/user-attachments/assets/7d3baa2f-26a8-4b08-b58c-9d932617c209)

Observations: 
Outliers Analysis (using IQR method):
Based on the IQR method, there are 425 properties considered as outliers.
These outliers have an average price of approximately 9.24 crores.
The range for these outliers is from 5.46 crores to 31.5 crores.


![Image](https://github.com/user-attachments/assets/b6458161-1911-4cbf-90a7-c80e231cb30d)

![Image](https://github.com/user-attachments/assets/3153ad9e-f090-4aa0-9fe8-e7dcca978531)

Observations: 
1. np.log1p(x): This function computes the natural logarithm of 1+x. It's designed to provide more accurate results for values of x that are very close to zero.
2. Using np.log1p helps in transforming the price column while ensuring that any value (including zero, if present) is handled appropriately. When we need to reverse the transformation, we can use np.expm1 which computes e^x-1


![Screenshot 2025-04-11 052936](https://github.com/user-attachments/assets/19b8495d-c3e2-4380-ac96-3d711b309d22)

Figure 1 Observation:
1. The majority of properties are priced in the "1-2 crores" and "2-3 crores" ranges.
2. There's a significant drop in the number of properties priced above "5 crores."

Figure 2 Observations: 
1. Most properties have a price_per_sqft ranging between approximately ₹0 and ₹40,000.
2. There is a significant concentration in the lower range, with a few properties having exceptionally high price_per_sqft.

Figure 3 Observations: Prices are highly concentrated between 0 to 3 crores.


![image](https://github.com/user-attachments/assets/dc04688b-ee04-4f6c-b2af-92d1f048b3c0)

![Screenshot 2025-04-11 052936](https://github.com/user-attachments/assets/ff5f42bc-66be-44ad-9f70-b40082c26f8e)

Figure 1 & 2 Observation: 
1. The dataset shows the distribution of properties based on the number of bedrooms.
2. The most common property has 3 bedrooms, followed by 2 bedrooms, while properties with 5 bedrooms are least frequent.

Figure 3 & 4 Observation: 
1. The data shows the distribution of properties by the number of bathrooms, with the majority having between 2 and 5 bathrooms.
2. Properties with more than 10 bathrooms are rare, indicating they are outliers or luxury properties.


![Image](https://github.com/user-attachments/assets/955f15f9-3cc1-4a20-bd16-5d848a18188b)

![Image](https://github.com/user-attachments/assets/e8124a27-5421-49f8-b5f4-d81555f7a63e)

Observation: The majority of properties have either 3 or more balconies (31.87%).
A significant number of properties have 2 balconies (24.04%), while fewer have 1 or none.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/aec8d4f1-a0af-439f-9e84-10cd047ef96e)

![Screenshot 2025-04-11 052936](https://github.com/user-attachments/assets/8d090cd7-cbdc-4545-b92b-a324506c69de)

Observations:
1. The majority of the properties lie between the ground floor (0) and the 25th floor.
2. Floors 1 to 4 are particularly common, with the 3rd floor being the most frequent.
3. There are a few properties located at higher floors, but their frequency is much lower.
4. The box plot reveals that the majority of the properties are concentrated around the lower floors. The interquartile range (IQR) lies between approximately the 2nd and 10th floors.
5. Data points beyond the "whiskers" of the box plot, especially on the higher side, indicate potential outliers.
 

![Image](https://github.com/user-attachments/assets/75e66804-2975-4d6e-b708-3b0cc792cc9a)

![Image](https://github.com/user-attachments/assets/f447fee3-535a-4519-a094-93afbe235b08)

1. Most properties have a built-up area ranging roughly between 500 sq.ft and 3,500 sq.ft.
2. There are very few properties with a much larger built-up area, leading to a highly right-skewed distribution.
3. The box plot confirms the presence of significant outliers on the higher side. The data's interquartile range (IQR) is relatively compact, but the "whiskers" of the box plot are stretched due to the outliers.
4. The presence of extreme values, especially on the higher side, suggests that there may be outliers or data errors. This could also be due to some properties being exceptionally large, like a commercial complex or an entire building being listed.


![Image](https://github.com/user-attachments/assets/5e122357-161f-4adb-b750-149d37e04869)

![Image](https://github.com/user-attachments/assets/b1ae1816-509d-4832-8304-a564d98369d3)

Observation: The data shows the presence (orange color) or absence (blue color) of specific rooms in properties. Study rooms, servant rooms, and stores are less common, while others are more frequently found.


![Screenshot 2025-04-11 052936](https://github.com/user-attachments/assets/b25951c3-c6db-4bd2-9765-902c7b6f130a)

![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/e6864c26-cf85-490b-bccb-52f9c04150ef)

Observations: The luxury score distribution has multiple peaks, suggesting a multi-modal distribution. There's a significant number of properties with lower luxury scores (around 0-50), and another peak is observed around the 110-130 range. The box plot reveals that the majority of the properties have luxury scores between approximately 30 and 110. The interquartile range (IQR) lies between these values.


#### 5.2 Overview of dataset using Multivariate Analysis:

![Image](https://github.com/user-attachments/assets/25bd2e21-bd22-46da-952f-ce4d96580d10)

Observation: The dataset shows the average price for different property types. Flats are priced at 1.38 crore, while houses are priced at 4.25 crore on average.


![Image](https://github.com/user-attachments/assets/fd7ea086-0227-4318-9137-455002a6b55e)

Observation: The mean price for flats is lower than houses, with flats averaging 1.71 and houses 5.28. Flats have less price variability (SD = 1.39) compared to houses (SD = 4.73), indicating more price stability.


![Image](https://github.com/user-attachments/assets/6047055c-51f8-4d3c-8b8c-ebd530534464)

Observation: The average built_up_area for a flat is 1626.5 square feet, while for a house it's 1800 square feet. This suggests that houses tend to have slightly larger built-up areas compared to flats.


![Image](https://github.com/user-attachments/assets/b388b2c7-58bd-44c2-a845-f41754629b45)

Observation: The average built_up_area for a flat is 1626.5 square feet, while for a house it's 1800 square feet. This suggests that houses tend to have slightly larger built-up areas compared to flats.


![Image](https://github.com/user-attachments/assets/4bb41436-805e-45a1-859e-5d3c66b13ba1)

![Image](https://github.com/user-attachments/assets/c7102986-3710-45b5-8014-2257ad617605)

Observation: The median price per square foot for flats is significantly lower than houses, indicating a higher cost for house properties. This suggests that houses typically offer more space or are located in more expensive areas compared to flats.


![Image](https://github.com/user-attachments/assets/ce908fd5-5d4e-4e82-b1a9-15fe64b13487)

Observations: The table shows the distribution of properties by bedroom count across different property types (flat and house). Flats are more concentrated in lower bedroom counts, while houses have a wider spread, including higher bedroom counts.


![Image](https://github.com/user-attachments/assets/8705eb34-632f-4cc8-be43-92ff1e90a11e)

![Image](https://github.com/user-attachments/assets/ee7ecaaf-f9c5-4e97-8cfa-53de8f784335)

Observations: We calculated the average floor number for each property type using the groupby method. The result shows that flats tend to have higher average floors than houses.


![Image](https://github.com/user-attachments/assets/95c0c5bb-9d23-413f-b969-71e19a078bb6)

Observation: The data shows the distribution of property ages across different property types. Flats are more likely to be new or moderately old, while houses have a higher percentage of older or undefined properties.


![Image](https://github.com/user-attachments/assets/f4a59c01-e6dc-4236-a656-560af9ea6d0a)

Observation: The table shows the average count of property types (flat vs house) for each age possession category. Houses generally have higher values across most categories, particularly for "Relatively New" and "Under Construction.


![Image](https://github.com/user-attachments/assets/3807ace7-710b-4806-8348-ade79a51b6ca)

Observation: The table shows the average number of bedrooms for different property types (flat vs house). It highlights the distribution of bedrooms across property types, with more variation for houses compared to flats.


![image](https://github.com/user-attachments/assets/b3263dfe-3362-4a14-af29-8ebae883694f)

Observation: The table shows the distribution of furnishing types across different property types (flat vs house). For flats, most have furnishing type 0, while houses show a more balanced spread across the types.


![Screenshot 2025-04-11 052936](https://github.com/user-attachments/assets/7f8ea1e2-2484-4d5a-a338-f37ec3559ed1)

Observation: The table shows the average furnishing type counts for each property type (flat/house) across different categories (0, 1, 2). Houses generally have higher furnishing counts compared to flats in all categories, indicating more furnished features.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/f23e4fb0-e4fc-4e66-8756-ac70e7c33473)

![Screenshot 2025-04-11 052936](https://github.com/user-attachments/assets/f9316c61-2dbe-40e2-ac7b-31d9e7992187)

Observation: Flats have a significantly higher average luxury score (78.74) compared to houses (47.85). This suggests that flats may generally offer more luxurious features or amenities than houses.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/fd20c39e-f1db-4dac-aaba-401bcac4a744)

Observation: This dataset shows the count of flat and house properties across different sectors, including both well-known areas (like Dwarka Expressway) and less common sectors. The data allows for the analysis of property distribution based on location and type, providing insights into regional property availability.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/ecca28bc-b6e0-4945-922d-9c201e2a2176)

Observation: The data shows the average price for various sectors, with a wide range from lower-priced sectors (e.g., sohna road road at 0.57) to high-priced ones (e.g., sector 26 at 12.68). The variation suggests differing property values based on location and sector status, highlighting potential market trends across regions.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/2bb0c51f-e0ed-4291-b9d9-b86276b416f4)

Observation: The dataset contains 115 entries showing sectors and their respective price per square foot.
Price per square foot varies across sectors, with some areas like "sector 3 phase 3 extension" having higher prices.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/3129eb01-8315-42cb-b9b0-1706ede64eb1)

Observation: The dataset presents luxury scores for various sectors, with each sector showing a different level of luxury. The scores are sorted by sector number, revealing disparities in luxury across locations like Dwarka Expressway and Sohna Road.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/f45a2623-af48-493c-b097-77395dc31855)

Observation: The table shows the average area and price for different bedroom counts. Generally, larger properties (more bedrooms) have higher average prices, but there are some fluctuations in the trend.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/df476bfb-665b-4955-aabb-5542f3e0aa99)

Observation: The statistics show that 'area' and 'price' have a positive correlation (0.67), while 'agePossession' is missing for most entries.
The basic statistics reveal that the 'area' varies widely, while 'price' has a much narrower range with a few outliers.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/599e8684-3055-4dae-98cd-c4ffd58ab719)

Observation: The correlation of 0.67 between area and price indicates a moderate positive relationship.
Properties with furnishing type '2' tend to have the largest average area and price.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/4210f1d5-f6a4-4706-9007-cd275a3ece7a)

Observation: The data shows how the price increases with the number of bedrooms, with a noticeable jump in price for 12 and 16 bedrooms. Larger homes (12+ bedrooms) have higher variability in price, indicating possible luxury or unique properties.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/03d4aaa4-c283-4ba5-babd-85ef9ac5c063)

Observation: The median price for each agePossession category shows varying property values. "Moderately Old" properties have the highest median price, while "Undefined" properties have the lowest.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/581b14e8-a1c7-4ec4-b0e0-16a5eeea45f2)

Observation: Moderately Old properties have the largest average area, while Undefined ones have the smallest. Newer properties generally have slightly smaller areas compared to older ones, suggesting older homes may be more spacious


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/77d12e8e-4929-4e93-919d-57b5753e5ff3)

Observation: The average property prices for each furnishing type are 1.31, 2.12, and 2.40 (in lakhs or respective unit). This shows that better or more furnished properties tend to have higher average prices.


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/07f8996a-e99d-4e20-98ef-7296c2074d54)

Observation: The luxury_score shows the distribution of properties based on their luxury level. Most properties have lower luxury scores, while very high luxury scores are rare.


![image](https://github.com/user-attachments/assets/c6e0b299-540c-4551-8d2c-0d881c030fc7)

Above diagram represents correlation between features. 


![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/8a00f45e-23d7-40a6-a4c4-f88c460aca0a)

Above diagram represents Pairplot of our features

#### 6. Outlier Treatment

We have frequently used fillna() in our code. In onw instances, we have dropped rows after attempting to handle missing values. However, some columns that were not properly defined are still being labeled as "undefined". To explore this further, you can review my code.


#### 7. Missing Value Imputation

![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/91c0ad38-6a42-4475-b1a4-33505e5156f1)

Observation: We have plotted scatter plot to know if there is any linear relationship. Please go through my jupyter notebook to check how I have treated outliers. I have frequently used fillna() in my code. In one instances, I dropped rows after attempting to handle missing values. However, some columns that were not properly defined are still being labeled as "undefined". To explore this further, you can review my code


#### 8. Feature Selection

![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/81b3198b-06b3-4f79-813e-ab3011b7f2cf)

We have done ordinal encoding. We use ordinal encoding to convert categorical variables into numerical values that machine learning models can interpret and learn from.

Technique 1 for feature selection -> Correlation

![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/e6109f49-662d-4b7b-a4a2-ea76e18ece83)

Technique 2 for feature selection -> Random Forest Feature Importance

![Screenshot 2025-04-11 052936](https://github.com/user-attachments/assets/f791d361-8371-46a9-a5bd-c3f147de75b1)

Technique 3 for feature selection -> Gradient Boosting Feature importances

![Screenshot 2025-04-09 113538](https://github.com/user-attachments/assets/8bba6254-0d04-43be-883d-f4c87a9e3549)

Technique 4 for feature selection -> Permutation Importance

![image](https://github.com/user-attachments/assets/d6a80442-f5ae-4db5-b9ee-f76094becc16)

Technique 5 for feature selection -> LASSO

![Screenshot 2025-04-09 113538](https://github.com/user-attachments/assets/bbfcaeea-af8b-476b-9d98-7e6a967b6a41)

Technique 6 for feature selection -> RFE

![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/49a90236-7e8b-4bfa-a07f-1d406971d583)

Technique 7 for feature selection -> Linear Regression Weights

![Screenshot 2025-04-11 061755](https://github.com/user-attachments/assets/17df93e9-64be-479c-9c57-e6f3ff249912)

Technique 8 for feature selection -> SHAP

![Screenshot 2025-04-09 113538](https://github.com/user-attachments/assets/cc3c6658-0a2e-45da-9cab-12180471b132)

#### 9. Model Selection and Productization: 
We built a machine learning pipeline that applies preprocessing (scaling numerical features and ordinal encoding categorical ones) and fits a linear regression, SVR, Ridge, LASSO, decision tree, random forest, extra trees, gradient boosting, adaboost, MLP and xgboost. We evaluated its performance using 10-fold cross-validation and then trained it on a train-test split of the data for final predictions.

![Screenshot 2025-04-09 113538](https://github.com/user-attachments/assets/4deceb53-6d26-4aa9-84a2-fbf14d08cfb6)


#### 10. Building Analytics model to deploy on AWS website [Link](http://localhost:8501/Analysis_App)

Our Real Estate Recommender comprises of 4 pages[Lin:
1. Home
2. Analysis app
3. Price Predictor
4. Recommended Apartments

In our analytics Module, we have shown following things:
1. Geo Map
2. Word CLoud Amenities
3. Scatterplot (Area vs Price)
4. Pie chart (filtered out BHK by sector)
5. Side by side bedroom price
6. Displot of price of flat and house

#### 11. Recommender System

Recommender systems are a subclass of information filtering systems that aim to predict the "rating" or "preference" a user would give to an item. 

![Screenshot 2025-04-09 113538](https://github.com/user-attachments/assets/9a976669-7dbb-4755-b342-a2be7b2899f3)

In our case,
1. The user selects a location and radius, and the recommender system suggests the most popular localities nearby.
2. Upon selecting an apartment, the system recommends similar apartments based on the highest similarity scores.


#### 12. Deploying application on AWS

We have used following 7 steps to deploy our Real Estate recommender on AWS using streamlit: 

Step 1. Setting Up an EC2 Instance

Step 2. Connecting to the EC2 Instance

Step 3. Preparing the Instance

Step 4. Transferring Files to the EC2 Instance

Step 5. Installing Dependencies

Step 6. Running the Streamlit App

Step 7. Running the App in the Background




















































