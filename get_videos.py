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

#for i in response:
#    print(response)

#for i in response:
#    print(response[i]['id'])

#find out how to pull just the video id from the results
#find out what data structure the request is.

#print(response[0]['id'])


#might be on to something. this one just return the items 
#print(response['items'])

#this one returnse just the 1st video items
#print(response['items'][0])

#works, returns just the video id
#print(response['items'][0]['id'])

#n = 0
#for i in response:
#    print(response['items'][n]['id'])
#    n = n + 1

id_list = []
n = 0
for i in response:
    id_list.append(response['items'][n]['id'])
    n = n + 1


#"https://www.youtube.com/watch?v="
