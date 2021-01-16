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

#############

video_id = id_list[0]

#language=YouTubeTranscriptApi.list_transcripts(video_id)
#print(language)
#if the GENERATED language = "pt" then we can use this video
#if not, don't use
#can use list transcripts  and use language parameter and then see if that is set to true.

video_transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])

#prints entire transcript for given video
#print(video_transcript)

#searches video transcript for word, update later to ignore upper/lower case
#if word in video_transcript[0]['text']:
#	print("I found it")
#else:
#	print("nope")

for i in video_transcript:
   print(i)

match = []

#searches video transcript for word and stores video id and timestamp in a dictionary in the match list, update later to ignore upper/lower case
for i in video_transcript:
   if word in i['text']:
      print("yes")
      match.append({'match_id': video_id, 'timestamp': i['start']})
   else:
      print("no")

print(match)

