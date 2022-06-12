# Project2

For this project, we will create a lex bot that will help determine a competitieve price offer for homes in Seattle. The lex bot will be supported by a machine learning model that we will choose based off a high level analysis due to time constraints and to focus the majority of our time on the functionality of the lambda function and lex bot. The machine learning models will consist of key features of site/dwellings as well as the listing price and solve for selling price. Even though the listing price and selling price have a higher correlation, we want the machine learning model to take in account the selling price so the offer price can be the most competitive. The machine learning model we choose will have the highest coefficient of determination testing score as well as the lowest mean absolute error. **Note to Graders: Please see section below, "Adjustments based on feedback".**

## User Story

As a real estate investor, I want to find a way to make a competitive offer based on historical data that takes into consideration site/dwelling features so my offer is the most desireable to the seller.

## Acceptance Criteria

Given the analysis of the Seattle market, we will create a bot that will recommend an offer amount based on the best machine learning model and how aggressive the client wants to make their offer.

## Method

- We will analyze 5 years of historical data from May 2017 to May 2022, in Seattle, using three different types of machine learning models: Decision Tree, Random Forest, and Linear Regression. 
- Specific features include Zip Code, Bathrooms, Bedrooms, Lot Square Footage, Listing Price, Sold to List Price Percentage, Square Footage, and Property Type.
- We will then use the analysis to determine the best machine learning model to use in our lex bot.
- The bot will then suggest an offer price that our client would offer for a property based on our model and user input.

## Machine Learning Files
The machine learning model code (ML_Model_Analysis_Original.ipynb) is located in the "Project_2_Data_and_Analysis" folder.

The csv with the data (Sold_And_Stats_New_a.csv) is located in the "Project_2_Data_and_Analysis" folder.

All screenshots and screen recordings of the project are located in the "Screenshots" subfolder of the "Resources" folder. 

(Please note, the screenrecording of the Lex bot "Amazon Lex - Google Chrome 2022-06-10 21-41-36.mp4" is quite large. In order to open in Git Hub, you will need to download it by selecting "View raw".)

The project presentation is saved as "Project 2 Fintech Bootcamp.pdf" in the "Resources" folder.


## Lambda Code, LEX Bot and Required Files for AWS Deployment
The 'OfferAid_DeploymentFiles' contains all files along with a README with instructions and descriptions of everything required to deploy this prediction model within the AWS environment. 

## Technologies

This project is written in Python.

### Data and Analysis - Machine Learning

The required libraries in order to use the ML_Model_Analysis application are:

![Data_analysis_imports](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Data_Analysis_imports.png "Data_analysis_imports")
    
### Lambda Function

The required libraries in order to run the lambda function are:

![Lambda_Function_imports](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Lambda_Function_imports.png "Lambda_Funcion_imports")

### AWS

- Lambda
- S3
- Lex Bot
- Cloud Watch

## Data and Analysis - Machine Learning

- Create and view the dataframe from the CSV file

![Raw_Data_Frame](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Raw_Data_Frame.png "Raw_Data_Frame")

- Clean the data.
    - Keep columns that contain relevant features for the Machine Learning Model (Zip Code, Bathrooms, Bedrooms, Lot Square Footage, Listing Price, Selling Price, Sold to List Price Percentage, Square Footage, and Property Type)
    - Drop NaN values
    - Remove rows that contain "0" Values
    
![Cleaned_Data_Frame](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Cleaned_Data_Frame.png "Cleaned_Data_Frame")

- Compare the features using Heatmap

![Features_Heatmap](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Features_Heatmap.png "Features_Heatmap")

- Use 3 different Machine Learning Models and compare the highest coefficient of determination testing score as well as the lowest mean absolute error between each model.

### Machine Learning Models

- Linear Regression Model

    - Code
    
    ![Linear_Regression_Model_Code](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Linear_Regression_Model_Code.png "Linear_Regression_Model_Code")
    
    
    - Results
    
    ![Linear_Regression_Model_Results](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Linear_Regression_Model_Results.png "Linear_Regression_Model_Results")
    

- Decision Tree Model

    - Code
    
    ![Decision_Tree_Model_Code](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Decision_Tree_Model_Code.png "Decision_Tree_Model_Code")
    
    
    - Results
    
    ![Decision_Tree_Model_Results](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Decision_Tree_Model_Results.png "Decision_Tree_Model_Results")
    

- Random Forest Model

    - Code
    
    ![Random_Forest_Model_Code](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Random_Forest_Model_Code.png "Random_Forest_Model_Code")
    
    
    - Results
    
    ![Random_Forest_Model_Results](https://github.com/arfylarfy/Project2/blob/main/Resources/Screenshots/Random_Forest_Model_Results.png "Random_Forest_Model_Results")
  

### Analysis

- Based on the Mean Absolute Error, we chose to use the Decision Tree Model with our lex bot.
- Decision trees support non linearity, where Linear Regression supports only linear solutions. When there are large number of features with fewer data-sets (with low noise), linear regressions may outperform Decision Trees/Random Forests. In general cases, Decision trees will have better average accuracy.

## Lex Bot

- See ReadMe within the OfferAid_DeploymentFiles
https://github.com/arfylarfy/Project2/blob/main/OfferAid_DeploymentFiles/README.md

## Adjustments Based on Feedback

After our presentation, the instructors gave us very valuable feedback regarding our machine learning model. When completing the original code, we debated on whether or not we should include "Listing Price" as a feature in our model. Upon further discussion with our instructors, we realize that by including "Listing Price", it heavily influenced the models and accuracy predictions. We are including a file named, "ML_Model_Analysis_NEW.ipynb" in the "Project_2_Data_and_Analysis" folder which shows the machine learning code and results with the "Listing Price" removed. You will notice the Coefficient of Determination (testing) in all three models was reduced significantly. Additionally, the Mean Absolute Error of all 3 models increased significantly as well. The new performance measurements would change our choice of model from Decision Trees to Random Forests for our Lambda Function and Lex Bot. Due to time contraints, we are not including revised code for the Lambda function and Lex Bot in this project. If we had more time, we would alter the entire project to reflect this important change to our features list. 


## Contributors

Cody Schroeder, codeman@uw.edu

Hilary Willis, hilarywillis@gmail.com

Theo Prentice, theoprentice14@gmail.com

Aaron Bumgarner, aaron.j.bumgarner@gmail.com

Aranda Furth, arandafurth@gmail.com



## License

Copyright 2022 Cody Schroeder, Hilary Willis, Theo Prentice, Aaron Bumgarner, Aranda Furth

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
