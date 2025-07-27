# Part 2:
# Comments from the spreadsheet -> VADER evalutation -> Balancing with likes

import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# the csv file name
file_name = input("File name: ")


def vader_analysis (comment):
    """
    VADER compound evaluation of the given comment

    Args: 
        comment: The comment to be evaluated
    
    Returns:
        VADER's int compound analysis of the comment
    """

    #analyses the polarity of the comment
    vs = analyzer.polarity_scores(comment)

    # return the compound (overall) score
    return vs["compound"]


# Take all comments, pass them to VADER, weigh accordingly with likes
pos_comments = 0
neg_comments = 0
neu_comments = 0
total_comments = 0
total_sentiment = 0

with open(file_name, "r", encoding="utf-8") as csv_file:
    # specify the delimeter is a comma
    reader = csv.reader(csv_file, delimeter=",")

    # for each row, send the comment to VADER and weight with likes
    for row in reader:
        # send to VADER
        sentiment = vader_analysis(row[1])

        # check like count
        like_count = row[0]

        if like_count > 0:
            # counting sentiment of all likes
            total_sentiment += (like_count*sentiment)
        
        # track comment sentiment totals, including likes on all comments
        # if positive
        if sentiment > 0.05:      
            positive_comments += (1 + like_count)
        # if negative
        elif sentiment < -0.05:     
            negative_comments += (1 + like_count)
        # if neutral
        else:                   
            neutral_comments += (1 + like_count)

        # total comment tracker
        total_comments += (1 + like_count)

print(positive_comments/total_comments*100, "% positive", "# pos comments: ", positive_comments, sep="")
print(negative_comments/total_comments*100, "# neg comments: ", negative_comments, "% negative", sep="")
print(neutral_comments/total_comments*100, "% neutral", "# neutral comments: ", neutral_comments, sep="")
print("total # comments: ", total_comments, sep="")
print("average sentiment:", total_sentiment/total_comments)
