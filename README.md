# Java-server-controller-bot
A python coded discord bot that can control your minecraft java server from your pc. Forwarding minecraft server's port using Ngrok in this serssion.
Addition: a discord webhook that will collect the Ngrok tcp tunnel's address and post it in the discord chat.

1. Install the requirements using pip -r requirements.txt.
2. Instruction are given in the codes, make sure to read them and change as instructed.

For the additional discord webhook, create a webhook and put your webhook's url in line 7.

For Ngrok,
1. Head to https://ngrok.com/
2. Create an account.
3. Copy your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
4. Download Ngrok from https://ngrok.com/download
5. Extract it and put it in your directory of choice
6. Run the ngrok.exe
7. Authenticate using: 'ngrok config add-authtoken <your authtoken>'
8. After you have authenticated successfully, start your tcp tunnel session using: ngrok tcp 25565
9. You can change the data center location using: 'ngrok tcp 25565 -region IN
10. It will forward your port so that other players can join to your server.
11. to get the ip, just copy the forwarding link. copy with the port number as well. cut the 'tcp://' part. you will be left with the ip address of your server.
