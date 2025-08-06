# Do Female YouTubers Receive More Negative Comments Than Male YouTubers?

## Introduction
For my COMP400 project I chose to look into if female YouTubers receive more negative comments than male YouTubers by doing a literature review as well as a replication/improvement of methodologies. 

The final paper found [here](https://github.com/graceyuz/COMP400/blob/main/COMP400-Final-Paper.pdf) provides the full literature review, an explanation of methodology, and the results of the study.

## Repository Organization
This repository includes all information for the project:
* The final paper is found [here](https://github.com/graceyuz/COMP400/blob/main/COMP400-Final-Paper.pdf)
* The Python script which pulls and stores the YouTube comments is found [here](https://github.com/graceyuz/COMP400/blob/main/comments-to-spreadsheet.py)
* The Python script which evaluates the sentiment of the YouTube comments is found [here](https://github.com/graceyuz/COMP400/blob/main/spreadsheet-to-VADER.py)
* All comment data used in the study is found [here](https://github.com/graceyuz/COMP400/tree/main/Comment-Data). This comment data is organized by YouTuber, and each YouTuber has two CSV files:
    * A file titled `YouTuber-Name_comments.csv` where the results from `comments-to-spreadsheet.py` are stored
    * A file titled `YouTuber-Name_VADER.csv` where the results from `spreadsheet-to-VADER.py` are stored

## Dependencies
For the separate Python scripts, each has different dependencies:
* `comments-to-spreadsheet.py` depends on `google-api-python-client` to access YouTube comments
* `spreadsheet-to-VADER.py` depends on `vaderSentiment` for sentiment analysis

In order to use `comments-to-spreadsheet.py`, you must have a valid YouTube Data API v3 key stored as an environment variable. Set the variable like this:
    `API_KEY='your-api-key-here'`

## Acknowledgements
The included comment data was retrieved via the YouTube Data API v3. All data is publicly available, and no user-identifiable information has been included, in accordance with YouTube’s API Services Terms of Service.

Portions of this code were inspired by public examples of YouTube Data API usage. No code was copied, and all logic was implemented independently.
