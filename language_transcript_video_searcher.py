

#def word_searcher(word):
    
    from youtube_transcript_api import YouTubeTranscriptApi

    #get what word to search for
    #print("enter word")
    #word = input()

    #language and region support
    print("enter language: 1 for Portuguese, 2 for Spanish")
    language = input()
    if language == "1":
        language = "pt"
    if language == "2":
        language = "es"
    print("enter region: 1 for Brazil, 2 for Mexico")
    region = input()
    if region == "1":
        region = "BR"
    if region == "2":
        region = "MX"

    ############# gets list of videos to search
    from googleapiclient.discovery import build

    api_key = "AIzaSyBiYF3UQfa2hskLxr7oec8-rTtV2YqbTCY"

    youtube = build('youtube', 'v3', developerKey=api_key)

    #gets list of videos from Most Popular
    #request = youtube.videos().list(
    #        part='snippet',
    #        hl='pt-br',
    #        chart='mostPopular',
    #        maxResults='10',
    #        regionCode='BR'
    #    )

    #how many videos to search
    videoNum = 3

    #searches word in youtube under region and language given
    request = youtube.search().list(
            part='snippet',
            q=word,
            type='video',
            #relevanceLanguage='pt-br',
            relevanceLanguage=language,
            maxResults=videoNum,
            #regionCode='BR'
            regionCode=region
        )
    #stores entire youtube search results list
    response = request.execute()

    #creates list for storing video ids from response
    id_list = []
    #stores just the video ids in id_list
    for i in range(0, videoNum):
        try:
            id_list.append(response['items'][i]['id']['videoId'])
        except:
            print("whoopsie")

    #if using MostPopular option for getting videos
    #id_list = []
    #n = 0
    #for i in response:
    #    id_list.append(response['items'][n]['id'])
    #    n = n + 1

    #############

    #create match list for storing videoid and start time of transcript block that contains the word
    match = []

    #uses transcript api to get transcript for each video
    for i in range(0, videoNum):
        video_id = id_list[i]
        print(video_id)
        try:
            video_transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
     
            #searches video transcript for word and stores video id and timestamp in a dictionary in the match list, update later to ignore upper/lower case
            for i in video_transcript:
                if word in i['text']:
                    match.append({'match_id': video_id, 'timestamp': i['start']})
        except:
            "no transcript available in selected language"


    #remove hundredths of a second from timestamp and convert timestamp to string
    for i in match:
        i['timestamp'] = ".".join(str(i['timestamp']).split(".")[:-1])

    #create timestamped url for all matches    
    for i in match:
        print("https://youtu.be/" + i['match_id'] + "?t=" + i['timestamp'])


