import json
import requests
import os

def main():

    webhook_url = 'your webhook's url'
    agent = 'Minecraft Server'

    tunnel_url = requests.get("http://localhost:4040/api/tunnels").text
    j = json.loads(tunnel_url)
    tunnel_url = j['tunnels'][0]['public_url']
    
    content = json.dumps({"content": tunnel_url})

    header =  {
        'User-Agent': agent,
        "Content-Type": "application/json"
    }
    
    request = requests.post(webhook_url,
                            headers=header,
                            data=content)

if __name__ == '__main__':
    main()
