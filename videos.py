import json
import subprocess
with open("./liked_posts.json", "r") as file:
    parsed = json.load(file)

href_values = []
for entry in parsed["likes_media_likes"]:
    href_value = entry["string_list_data"][0]["href"]
    href_values.append(href_value)

command = "yt-dlp {} "

for href_value in href_values:
    subprocess.run(command.format(href_value), shell=True)
