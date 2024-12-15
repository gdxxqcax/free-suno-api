import requests
from configs import API_KEY


def get_song_task_info(task_id):
    # Check the task status
    url = f"https://api.loveaiapi.com/music/suno/task?task_id={task_id}"

    headers = {
    'Authorization': f'Bearer {API_KEY}'
    }

    response = requests.get(url, headers=headers)
    print('Checking task status...')
    print(response.json())
