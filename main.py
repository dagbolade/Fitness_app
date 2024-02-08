import pandas as pd

# Convert json to csv
# exercises_data = 'exercises.json'
# df = pd.read_json(exercises_data)
# df.to_csv('exercises.csv', index=False)

import requests
from pathlib import Path

import requests
from pathlib import Path


import requests
from pathlib import Path

# GitHub API base URL for the contents of the exercise directory
api_url = "https://api.github.com/repos/yuhonas/free-exercise-db/contents/exercises"
base_raw_url = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises"

# Directory to save downloaded images
save_directory = Path('images')
save_directory.mkdir(parents=True, exist_ok=True)

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

def fetch_and_download_images(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        folders = response.json()
        for folder in folders:
            # Check if the item is a directory (folder)
            if folder['type'] == 'dir':
                exercise_name = folder['name']
                exercise_api_url = folder['url']
                # Fetch the contents of the folder
                exercise_response = requests.get(exercise_api_url)
                if exercise_response.status_code == 200:
                    exercise_files = exercise_response.json()
                    for file in exercise_files:
                        if file['name'].endswith('.jpg'):
                            image_url = f"{base_raw_url}/{exercise_name}/{file['name']}"
                            save_path = save_directory / file['name']
                            download_image(image_url, save_path)
                            print(f"Downloaded {file['name']}")

fetch_and_download_images(api_url)


