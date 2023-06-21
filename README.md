# Java-server-controller-bot
A python coded discord bot that can control your minecraft java server from your pc. Forwarding minecraft server's port using Ngrok in this serssion.

1. Install the requirements using 'pip -r requirements.txt.'
2. Instruction are given in the codes, make sure to read them and change as instructed.

Go to https://discord.com/developers/applications, create new application and copy the bot's token.

For Ngrok,
1. Head to https://ngrok.com/
2. Create an account.
3. Copy your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
4. Download Ngrok from https://ngrok.com/download
5. Extract it and put it in your directory of choice
6. Run the ngrok.exe
7. Authenticate using: "ngrok config add-authtoken 'your authtoken' "
8. After you have authenticated successfully, start your tcp tunnel session using: ngrok tcp 25565
9. You can change the data center location using: 'ngrok tcp 25565 -region IN
10. It will forward your port so that other players can join to your server.
11. To get the ip address of your server, just copy the forwarding link from the console. copy with the port number as well. cut the 'tcp://' part. you will be left with the ip address of your server.

Feel free to add new cool stuff. For queries, hit me up in dms on discord,username: avik.py
