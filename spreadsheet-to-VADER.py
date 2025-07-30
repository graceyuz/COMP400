# Part 2:
# Comments from the spreadsheet -> VADER evalutation -> Balancing with likes

import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# the csv file name
file_name = input("File name: ")
output_file = input("New file name to save with sentiment: ")

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
total_comments_weighted = 0
unweighted_comments = 0
total_sentiment = 0

with open(file_name, "r", encoding="utf-8") as csv_file, \
     open(output_file, "w", encoding="utf-8", newline="") as output_csv:
    # specify the delimeter is a comma
    reader = csv.reader(csv_file, delimiter=",")
    #writting to new file
    writer = csv.writer(output_csv)

    # for each row, send the comment to VADER and weight with likes
    for row in reader:
        # send to VADER
        sentiment = vader_analysis(row[1])

        # check like count
        like_count = int(row[0])

        # add sentiment score and all else to new file for review 
        writer.writerow([like_count, row[1], sentiment])

        # account for the original comment's sentiment
        total_sentiment += sentiment
        # account for the sentiment of liked comments
        if like_count > 0:
            total_sentiment += (like_count*sentiment)
        
        # track comment sentiment totals, including likes on all comments
        # if positive
        if sentiment > 0.05:      
            pos_comments += (1 + like_count)
        # if negative
        elif sentiment < -0.05:     
            neg_comments += (1 + like_count)
        # if neutral
        else:                   
            neu_comments += (1 + like_count)

        # total comment tracker
        total_comments_weighted += (1 + like_count)
        unweighted_comments += 1

# output
print(round(pos_comments/total_comments_weighted*100, 2), "% positive", ", number of positive comments: ", pos_comments, sep="")
print(round(neg_comments/total_comments_weighted*100, 2), "% negative", ", number of negative comments: ", neg_comments, sep="")
print(round(neu_comments/total_comments_weighted*100,2), "% neutral", ", number of neutral comments: ", neu_comments, sep="")
print("total # weighted comments: ", total_comments_weighted, sep="")
print(round(total_sentiment/total_comments_weighted, 4), "was the average sentiment")
print("Number of comments before weight:", unweighted_comments)

# confirmation
print(f"Sentiment data saved to {output_file}")