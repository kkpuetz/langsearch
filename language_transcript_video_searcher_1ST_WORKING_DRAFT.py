from youtube_transcript_api import YouTubeTranscriptApi

#get what word to search for
print("give me a word")
word = input()


############# gets list of videos to search
from googleapiclient.discovery import build

api_key = "AIzaSyBiYF3UQfa2hskLxr7oec8-rTtV2YqbTCY"

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.videos().list(
        part='snippet',
        hl='pt-br',
        chart='mostPopular',
        maxResults='5',
        regionCode='BR'
    )

response = request.execute()

#stores just the video ids in id_list
id_list = []
n = 0
for i in response:
    id_list.append(response['items'][n]['id'])
    n = n + 1

print(id_list)
#############

#variable for iterating through list of videos
n = 0

#create match list for storing videoid and start time of transcript block that contains the word
match = []

#uses transcript api to get transcript for each video
for i in id_list:
    video_id = id_list[n]
    try:
        video_transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])

#searches video transcript for word and stores video id and timestamp in a dictionary in the match list, update later to ignore upper/lower case
        for i in video_transcript:
           if word in i['text']:
              #print("yes")
              match.append({'match_id': video_id, 'timestamp': i['start']})
           #else:
              #print("no")

    except:
        "no transcript available in selected language"

    n = n + 1

#added try and except since language wasn't available in 3rd transcript so it gave an error and didn't continue.  had to indent everything

#just for checking to make sure it finds a match
#for i in match:
#    print(i)
    
#format and display urls from match_id
#url = "https://www.youtube.com/watch?v="
#for i in match:
#    print(url + i['match_id'])

url = "https://youtu.be/"

#remove hundredths of a second from timestamp and convert timestamp to string
for i in match:
    i['timestamp'] = ".".join(str(i['timestamp']).split(".")[:-1])

#create timestamped url for all matches    
for i in match:
    print(url + i['match_id'] + "?t=" + i['timestamp'])
