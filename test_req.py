import requests
requests.packages.urllib3.disable_warnings()


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
}

resp = requests.get('https://muse.jhu.edu/article/596226/pdf', headers=headers, verify=False)
print(resp.status_code)
with open('./test.pdf', 'wb') as f:
    f.write(resp.content)
