import requests
import time
from configs import API_KEY
from get_song_task_info import get_song_task_info

url = "https://api.loveaiapi.com/music/suno/merge"

payload = {
  # The `audio_id` must be the extended song ID.
  "audio_id": "546425e5-aa6c-40c7-9de9-d675f35cb181",
  "callback_url": "https://example.com/webhook"
}
headers = {
  'Authorization': f'Bearer {API_KEY}',
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json=payload)

print(response.json())

task_id = response.json()['task_id']
time.sleep(20)
get_song_task_info(task_id)