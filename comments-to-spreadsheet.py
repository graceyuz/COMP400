# Part 1:
# Retreival of comments from YouTube playlist -> Video IDs -> Comments collection

import os
import csv
from googleapiclient.discovery import build

# using an environment variable for api key
api_key = os.environ["API_KEY"]

# getting the wanted playlist
playlist_id = input("Playlist Id: ")

# building 
with build("youtube", "v3", developerKey=api_key) as youtube:

    # getting the video IDs from the playlist id
    def get_video_ids(playlist_id):
        """
        Retreives the YouTube video IDs from a given playlist ID

        Args:
            playlist_id: A string which is a valid YouTube playlist ID 
            containing a max of 10 videos
        
        Returns:
            A list of the YouTube video IDs which are in the given 
            playlist
        
        """

        return None    
    

    def get_comments():
        """
        Retreives the comments from the supplied YouTube video IDs

        Args:
            video_ids: A list containing valid YouTube video IDs 
        
        Returns:
            A nested list containing the video's comments, the date
            that the comment was published, and the number of likes 
            of the comment
        """

        return None
    
    