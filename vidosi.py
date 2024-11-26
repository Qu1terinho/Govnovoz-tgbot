from googleapiclient.discovery import build
import random
# Replace with your own API key
API_KEY = 'AIzaSyDBQNP_x_GbSUEtgKM0ot1uaeTB0RUrl38'
#CHANNEL_ID = 'UCook2IZlJTE_xQYNRUNrvRA'  # Replace with the channel ID

def get_channel_videos(api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get the videos in the uploads playlist
    videos = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId='PLGGxDqO8_aLNf-fW6NyTzo_exFbdK2HN7',
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            videos.append(video_url)
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return videos

if __name__ == "__main__":
    video_urls = get_channel_videos(API_KEY)
    f = open('urls.txt', 'w')
    for url in video_urls:
        f.write(f'{url}+,')
    f.close()