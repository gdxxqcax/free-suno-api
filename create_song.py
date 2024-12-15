"""
Use LoveAIAPI Suno API create song.

docs: https://docs.loveaiapi.com/docs/suno-ai-api/create-song-task
"""

import requests
import time
from configs import API_KEY
from get_song_task_info import get_song_task_info


url = "https://api.loveaiapi.com/music/suno/generate2"

payload = { 
  "prompt": "A happy and uplifting pop song",
  "title": "",
  "style": "",
  "instrumental": False,
  "custom": False,
  # You can add your business ID here, and during the callback, you can use this ID to implement logic.
  "callback_url": "https://example.com/webhook/?some_thing_your_need=xxx"
}
headers = {
  'Authorization': f'Bearer {API_KEY}',
  'Content-Type': 'application/json'
}

print('Creating song...')
response = requests.post(url, headers=headers, json=payload)
print(response.json())
task_id = response.json()['task_id']

time.sleep(40)

get_song_task_info(task_id)