# Project2

For this project, we will create a lex bot that will help determine a competitieve price offer for homes in Seattle. The lex bot will be supported by a machine learning model that we will choose based off a high level analysis due to time constraints and to focus the majority of our time on the functionality of the lambda function and lex bot. The machine learning models will consist of key features of site/dwellings as well as the listing price and solve for selling price. Even though the listing price and selling price have a higher correlation, we ant the machine learning model to take in account the selling price so the offer price can be the most competitive. The machine learning model we choose will have the highest coefficient of determination testing score as well as the lowest mean absolute error. 

## User Story

As a real estate investor, I want to find a way to make a competitive offer based on historical data that takes into consideration site/dwelling features so my offer is the most desireable to the seller.

## Acceptance Criteria

Given the analysis of the Seattle market, we will create a bot that will recommend an offer amount based on the best machine learning model and how aggressive the client wants to make their offer.

## Method

- We will analyze 5 years of historical data from May 2017 to May 2022, in Seattle, using three different types of machine learning models: Decision Tree, Random Forest, and Linear Regression. 
- Specific features include Zip Code, Bathrooms, Bedrooms, Lot Square Footage, Listing Price, Sold to List Price Percentage, Square Footage, and Property Type
- We will then use the analysis to determine the best machine learning model to use in our lex bot
- The bot will then suggest an offer price that our client would offer for a property based on our model and user input.

## Lambda Code, LEX Bot and Required Files for AWS Deployment
The 'OfferAid_DeplymentFiles' contains all files along with a README with instructions and descriptions of everything required to deploy this prediction model within the AWS environment. 

## Technologies

This project is written in python.

### Data and Analysis - Machine Learning

The required libraries in order to use the ML_Model_Analysis application are:

INSERT SCREENSHOT
    
## Data and Analysis - Machine Learning

- Create and view the dataframe from the CSV file

INSERT SCREENSHOT

- Clean the data.
    - Keep columns that contain relevant features for the Machine Learning Model (Zip Code, Bathrooms, Bedrooms, Lot Square Footage, Listing Price, Selling Price, Sold to List Price Percentage, Square Footage, and Property Type)
    - Drop NaN values
    - Remove rows that contain "0" Values
    
INSERT SCREENSHOT

- Compare the features using Heatmap

INSERT SCREENSHOT

- Use 3 different Machine Learning Models and compare the highest coefficient of determination testing score as well as the lowest mean absolute error between each model.

### Machine Learning Models

- Linear Regression Model

INSERT SCREENSHOTS

- Decision Tree Model

INSERT SCREENSHOTS

- Random Forest Model

INSERT SCREENSHOTS

### Analysis

- Based on the Mean Absolute Error, we chose to use the Decision Tree Model with our lex bot.
- Decision trees support non linearity, where Linear Regression supports only linear solutions. When there are large number of features with fewer data-sets (with low noise), linear regressions may outperfomr Decision Trees/Random Forests. In general cases, Decision trees will have better average accuracy.


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
