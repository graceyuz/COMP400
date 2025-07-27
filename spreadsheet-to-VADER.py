# Part 2:
# Comments from the spreadsheet -> VADER evalutation -> Balancing with likes

import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def vader_analysis (comment):
    """
    VADER compound evaluation of the given comment

    Args: 
        comment: The comment to be evaluated
    
    Returns:
        VADER's int compound analysis of the comment
    """

    return None