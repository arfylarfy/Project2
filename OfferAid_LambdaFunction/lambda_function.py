### Required Libraries ###
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.tree import DecisionTreeRegressor
from imblearn.metrics import sensitivity_specificity_support

from datetime import datetime
from dateutil.relativedelta import relativedelta

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


def validate_data(bedrooms, bathrooms, sqft, sqftunfinished, lotsize, yrbuilt, zipcode, aggressionLevel, intent_request):
    """
    Validates the data provided by the user.
    """
    def isint(var):
        if var is not None and var is not "skip":
            var = parse_int(var)
            if var < 0:
                return build_validation_result(
                False,
                var,
                "Numeric response must be greater than zero," 
                "if the value is unknown type \"skip\" to default to the average value for the zip code",
                )

    isint(bedrooms)
    isint(bathrooms)
    isint(sqft)
    isint(sqftunfinished)
    isint(lotsize)
    isint(yrbuilt)
    isint(zipcode)

    #propTypeList = ["House", "Condo", "Townhouse"]
    # Validate that the input is one of the three valid property types
    #if propertyType is not None:
    #    if propertyType not in propTypeList:
    #        return build_validation_result(
    #            False,
    #            "propertyType",
    #            "The property type must be either House, Condo, or Townhouse in order to use this service, "
    #            "please provide a different property type.",
    #        )

    # Validate the listing price, it should be > 0
    #if listingPrice is not None:
    #    listingPrice = parse_int(
    #        listingPrice
    #    )  # Since parameters are strings it's important to cast values
    #    if listingPrice < 0:
    #        return build_validation_result(
    #            False,
    #            "listingPrice",
    #            "The listing price should be greater than 0$,"
    #            "please provide a valid listing amount in dollars." 
    #            "If the real listing price is 0$," 
    #            "you should make an offer because it sounds like a great deal!",
    #        )
    
    aggressionOptions = ["low", "average", "high"]
    # Validate that the user input a valid level of aggression
    if aggressionLevel is not None:
        if aggressionLevel not in aggressionOptions:
            return build_validation_result(
                False,
                "aggressionLevel",
                "Please choose from one of the responses listed in order to get an accurate response,"
                "the level of aggression can be either \"low\", \"average\" or \"high\"."
            )

    return build_validation_result(True, None, None, None, None, None, None, None, None)

def readCSV():
    data = pd.read_csv('data.csv')
    return data

def cleanData(data):
    data['bedrooms'] = data['bedrooms'].round().astype(int)
    data['bathrooms'] = data['bathrooms'].round().astype(int)
    data['price'] = data['price'].round(decimals=2)
    data['statezip'] = data['statezip'].replace("WA 9", "9",regex=True).astype(int)
    missing = data.loc[(data['price'] == 0)].append(data.loc[(data['bathrooms'] == 0)])
    missing_index_list = missing.reset_index()['index'].to_list()
    missing_index_list.sort(reverse = True)
    data = data.drop(missing_index_list,axis=0)
    return data

def trainModel(data):
    features = data.drop(["date","street","country", "city", "waterfront", "view", "condition", "yr_renovated", "sqft_above", "floors"],axis=1)

    y = features['price']
    X = features.drop(['price'],axis=1)


    dt = DecisionTreeRegressor(max_depth=18)
    dt.fit(X, y)
    
    return dt


def getresponse(userDF, aggressionLevel):
    data = readCSV()
    data = cleanData(data)
    dtpred = trainModel(data)
    offerEstimate = dtpred.predict(userDF)
    if aggressionLevel == "low":
        offerEstimate = offerEstimate*.95
    elif aggressionLevel == "high":
        offerEstimate = offerEstimate*1.05

    return f"Using the information provided, {offerEstimate} would be a reasonable offer for this property"


### Intents Handlers ###
def offerAid(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """

    #propertyType = get_slots(intent_request)["propertyType"]
    #listingPrice = get_slots(intent_request)["listingPrice"]
    bedrooms = get_slots(intent_request)["bedrooms"]
    bathrooms = get_slots(intent_request)["bathrooms"]
    sqft = get_slots(intent_request)["sqft"]
    sqftunfinished = get_slots(intent_request)["sqftunfinished"]
    lotsize = get_slots(intent_request)["lotsize"]
    #acresorsqft = get_slots(intent_request)["acresorsqft"]
    yrbuilt = get_slots(intent_request)["yrbuilt"]
    zipcode = get_slots(intent_request)["zip"]
    aggressionLevel = get_slots(intent_request)["aggressionLevel"]
    source = intent_request["invocationSource"]
    
    
    if source == "DialogCodeHook":
        # This code performs basic validation on the supplied input slots.

        # Gets all the slots
        slots = get_slots(intent_request)

        # Validates user's input using the validate_data function
        validation_result = validate_data(bedrooms, bathrooms, sqft, sqftunfinished, lotsize, yrbuilt, zipcode, aggressionLevel, intent_request)

        # If the data provided by the user is not valid,
        # the elicitSlot dialog action is used to re-prompt for the first violation detected.
        if not validation_result["isValid"]: 
            slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Fetch current session attributes
        output_session_attributes = intent_request["sessionAttributes"]

        # Once all slots are valid, a delegate dialog is returned to Lex to choose the next course of action.
        return delegate(output_session_attributes, get_slots(intent_request))

    userData = [{'bedrooms': 3, 'bathrooms': 1, 'sqft_living': 1200, 'sqft_lot': 4000, 'sqft_basement': 300, 'yr_built': 1980, 'statezip': 98056}]
    userDF = pd.DataFrame(userData)

    # Return a message with conversion's result.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": getresponse(userDF, aggressionLevel)
            },
    )


### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "offerAid":
        return offerAid(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
