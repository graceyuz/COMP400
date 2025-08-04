# Part 2:
# Comments from the spreadsheet -> VADER evaluation -> Weighting with likes -> CSV

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
        VADER's compound sentiment score (float) of the comment
    """

    #analyses the sentiment polarity of the comment
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
    # read the csv file with comma as the delimiter
    reader = csv.reader(csv_file, delimiter=",")
    # writing to new file
    writer = csv.writer(output_csv)

    # for each row, send the comment to VADER and weight with likes
    for row in reader:
        # analyze with VADER
        sentiment = vader_analysis(row[1])

        # get like count
        like_count = int(row[0])

        # write like count, comment text, and sentiment score to the new file
        writer.writerow([like_count, row[1], sentiment])

        # account for the original comment's sentiment
        total_sentiment += sentiment
        # add weighted sentiment based on the number of likes
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

        # update total weighted and unweighted comment counters
        total_comments_weighted += (1 + like_count)
        unweighted_comments += 1

# output
print(f"{round(pos_comments/total_comments_weighted*100, 2)}% positive, number of positive comments (weighted): {pos_comments}")
print(f"{round(neg_comments/total_comments_weighted*100, 2)}% negative, number of negative comments (weighted): {neg_comments}")
print(f"{round(neu_comments/total_comments_weighted*100, 2)}% neutral, number of neutral comments (weighted): {neu_comments}")

print()

print(f"Total # of weighted comments: {total_comments_weighted}")
print(f"Average sentiment: {round(total_sentiment/total_comments_weighted, 4)}")

print()

print(f"Number of comments before weight: {unweighted_comments}")

print()

# confirmation
print(f"Sentiment data saved to {output_file}")