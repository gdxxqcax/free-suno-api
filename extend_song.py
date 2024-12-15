import requests
from configs import API_KEY
import time
from get_song_task_info import get_song_task_info

url = "https://api.loveaiapi.com/music/suno/extend"

payload = {
  "audio_id": "a7fddd29-47dd-4d8c-843c-c718ffde570d",
  "style": "pop",
  "title": "Extend Song Title",
  "prompt": "Extend Song Description",
  "continue_at": 60,
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