# Part 1:
# Retreival of comments from YouTube playlist -> Video IDs -> Comments collection csv

import os
import csv
from googleapiclient.discovery import build

# using an environment variable for api key
api_key = os.environ["API_KEY"]

# building 
with build("youtube", "v3", developerKey=api_key) as youtube:

    # getting the video IDs from the playlist id
    def get_video_ids(playlist_id):
        """
        Retrieves the YouTube video IDs from a given playlist ID

        Args:
            playlist_id: A string which is a valid YouTube playlist ID 
            containing a max of 10 videos
        
        Returns:
            A list of the YouTube video IDs which are in the given 
            playlist
        
        """

        # list of all video ids
        video_ids = []

        # get the video ids from specified playlist
        playlist_request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=10   # decided that playlists will be of length 10
        )

        playlist_response = playlist_request.execute()

        # getting video IDs:
        # 'playlist_response' is a dictionary which contains a key called 'items',
        # 'items' -> a list of items (each representing a video in the playlist)
        # each item is a dictionary which contains a 'contentDetails' key,
        # 'contentDetails' -> another dictionary containing a 'videoId' key
        # that 'videoId' -> actual video ID.
        for item in playlist_response["items"]:
            video_ids.append(item["contentDetails"]["videoId"])

        return video_ids    
    

    def get_comments(video_ids):
        """
        Retreives the comments from the supplied YouTube video IDs

        Args:
            video_ids: A list containing valid YouTube video IDs 
        
        Returns:
            A nested list containing the video's comments, the date
            that the comment was published, and the number of likes 
            of the comment
        """

        # list of all comments, publish dates, and likes
        comments = []

        # going through all video IDs and getting all comments
        for video_id in video_ids:
                
            # next page token to track if there are unseen comments
            next_page_token = None
            
            # continuous until there is no next page
            while True:

                 # requesting the comments
                comment_request = youtube.commentThreads().list(
                    part="snippet",                 # want snippet
                    videoId=video_id,               # specify video ID
                    maxResults=100,                  # most results possible
                    textFormat="plainText",         # for csv file
                    pageToken=next_page_token       # to get through pages
                )

                comment_response = comment_request.execute()

                # comment_response is a dictionary which contains key 'items'
                # 'items' -> list of comment threads which we want to iterate through 
                for item in comment_response["items"]:
                    # each item is a dictionary
                    # inside each item dictionary there is a snippet dictionary
                        # which contains a topLevelComment dictionary
                        # which contains a snippet dictionary
                
                    # get access to information we want in the second snippet
                    comment_info = item["snippet"]["topLevelComment"]["snippet"]

                    # getting the text, date, and likes of comment
                    comment_text = comment_info["textDisplay"]
                    like_count = comment_info["likeCount"]

                    # append to list of comments
                    comments.append([like_count, comment_text])

                # next page token
                next_page_token = comment_response.get("nextPageToken")

                # if there is no next page token, done
                if not next_page_token:
                    break

        return comments


    # calling and output
    playlist_id = input("Playlist ID: ")

    name_file = input("Name of csv file to generate: ")

    comments = get_comments(get_video_ids(playlist_id))

    # creating csv file
    with open(name_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # no need for a header row
        writer.writerows(comments)

    # confirmation message
    print(f"Saved {len(comments)} comments to {name_file}")
