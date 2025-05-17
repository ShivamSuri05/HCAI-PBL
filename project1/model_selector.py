import pandas as pd

def check_model_type(data):

    target = data[data.columns[-1]]

    #Check if target is numeric or categorical

    if target.dtype in ['int64', 'float64']:
        # Numeric target (Regression)
        if target.nunique() <= 10:  # If target has only a few unique values, treat it like classification
            return "Recommendation: Classification could be applied as the target variable is numeric with limited unique values."
        else:
            return "Recommendation: Regression should be applied as the target variable is continuous."
    elif target.dtype == 'object':
        # Categorical target (Classification)
        return "Recommendation: Classification should be applied as the target is categorical."
    else:
        return "Unable to determine the model type based on the target variable. We recommend checking the data visualization of the target variable to better understand its distribution."