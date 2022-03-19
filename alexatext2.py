from keep_alive import keep_alive
import os
import random
from os import system
import urllib
import json
from json import dumps, load
import argparse
from urllib.request import urlopen
from time import sleep
keep_alive()
import threading
system("pip install gtts")
system("pip install requests")
import aminofix
import time
from gtts import gTTS
import requests
from uuid import uuid4
client=aminofix.Client()
os.system("clear")
os.system("pip install amino.fix==2.2.3")
print("\t\033[1;32m Alexa1.0  \033[1;36m Community Bot \n\n")
email="gky06b@oosln.com"
password="prince"
client.login(email=email,password=password)
cid="3"
cidy=3

adm=[]
self=client.socket
def generate_transaction_id(self):
        return str(uuid4())
transaction=generate_transaction_id(self)

admx=["http://aminoapps.com/p/0j106z5,http://aminoapps.com/p/9rkn9p"]

subclient=aminofix.SubClient(comId=cid,profile=client.profile)
msg="""
Follow GC rules
1.Do not spam
2.Respect Host and Cohosts
3.Don't spread hate
4.Be polite in chatrooms

[biuc] MY ADMIN KWEL 
[IC] CHECK MY BIO FOR ADMIN 


"""
print("Alexa 1.0 Ready")
l=[]
lis = ["It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful","yes","No" ,"Probably","100%", "Not sure"]

@client.event("on_group_member_join")
def on_group_member_join(data):
	if data.comId==cidy:
		try:
			x=data.message.author.icon
			response=requests.get(f"{x}")
			file=open("sample.png","wb")
			file.write(response.content)
			file.close()
			img=open("sample.png","rb")
			subclient.send_message(chatId=data.message.chatId,message=f"""
[C]━━━━━━━━━━━━━━━
[c]Welcome <${data.message.author.nickname}$>
[C]━━━━━━━━━━━━━━━""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
			print(f"\nwelcomed {data.message.author.nickname} to gc ")
		except Exception as e:
			print(e)
@client.event("on_group_member_leave")
def on_group_member_leave(data):
	if data.comId==cidy:
		try:
			subclient.send_message(chatId=data.message.chatId,message="""[c]Somone Left the GC""")
			print(f"Someone left the gc")
		except Exception as e:
			print(e)
@client.event("on_text_message")
def on_text_message(data):
	if data.comId==cidy:
		ex=data.message.content
		cd=ex.split(' ')
		x=cd[0]
		c=cd[1:]
		adx=[]
		for w in cd:
			adx.append(w)
		print(adx)
		if ex:
			for i in adx:
				if len(i)<=50:
					if i[:23]=="http://aminoapps.com/p/" or i[:23]=="http://aminoapps.com/c/":
						fok=client.get_from_code(i)
						cidx=fok.path[1:fok.path.index("/")]
						if cidx!=cid:
							try:
								subclient.delete_message(chatId=data.message.chatId,messageId=data.message.messageId,asStaff=True)
								s=subclient.get_chat_thread(data.message.chatId).title
								subclient.start_chat(userId=adm,message=f"ndc://x{cid}/user/profile/{data.message.author.userId} was advertisng in {s}")
								
								subclient.send_message(chatId=data.message.chatId,message=f"<${data.message.author.nickname} don't advertise here")
								print("spotted advertiser")
							except Exception as e:
								print(e)
			if x.lower()=="/info" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="[ci]Hey there i m a communtiy Bot and my name is alexa , Kwel's bot                            admin link : http://aminoapps.com/p/9rkn9p 👈 for contact ")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/global":
				try:
					for i in c:
						mention = subclient.get_message_info(chatId=data.message.chatId, messageId=data.message.messageId).mentionUserIds
						for user in mention:
							h=subclient.get_user_info(userId=str(user)).nickname
							AID=client.get_user_info(userId=str(user)).aminoId
							d=client.get_from_code(i).objectId
							subclient.send_message(chatId=data.message.chatId,message="https://aminoapps.com/u/"+str(AID),embedTitle="Global Id",embedContent=f"{h}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/clear":
				if x.lower() not in l:
					try:
						for i in c:
							d=int(i)
							a=subclient.get_chat_messages(chatId=data.message.chatId,size=d)
							for i in a.messageId:
								subclient.delete_message(chatId=data.message.chatId,messageId=i,asStaff=True,reason="clear")
							subclient.send_message(chatId=data.message.chatId,message=f"Cleared {d} messages")
					except:
						subclient.send_message(chatId=data.message.chatId,message="[ci]Give Leader or Curator to the Bot to clear")
				else:
					subclient.send_message(chatId=data.message.chatId,message="Clear command is locked")
			if x.lower()=="/llock" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"Locked commands {l}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/lock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.append(i)
							subclient.send_message(chatId=data.message.chatId,message=f"locked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is only accessible to admin")
					except Exception as e:
						print(e)
			if x.lower()=="/unlock":
				if data.message.author.userId in adm:
					try:
						for i in c:
							l.remove(i)
							subclient.send_message(chatId=data.message.chatId,message=f"Unlocked {i} command")
							print(l)
							print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="This command is only accessible to admin")
					except Exception as e:
						print(e)
			if x.lower()=="/say":
				if x.lower() not in l:
					if c==[]:
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"{data.message.author.nickname}, i can't talk unless you write something after say !")
						except:
							pass
					else:
						try:
							t=''
							lx='en'
							for i in c:
								t=t+i
							out=gTTS(text=t,lang=lx,tld='co.in',slow=False)
							out.save("soundfx.mp3")
							with open("soundfx.mp3","rb") as f:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
							f.close()
							print(f"Info requested by {data.message.author.nickname}")
						except Exception as e:
							print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="say command is locked")
					except:
						pass
			if x.lower()=="!join":
				if c==[]:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"{data.message.author.nickname}, you have to paste the link after join")
					except:
						pass
				else:
					try:
						for i in c:
							try:
								d=client.get_from_code(i).objectId
								subclient.join_chat(chatId=d)
								subclient.send_message(chatId=data.message.chatId,message="Joined chatroom !!")
							except Exception as e:
								print(e)
						print(f"Info requested by {data.message.author.nickname}")
					except Exception as e:
						print(e)
			if x.lower()=="/vc" and c==[]:
				try:
					subclient.invite_to_vc(userId=data.message.author.userId,chatId=data.message.chatId)
					print(f"Invited {data.message.author.nickname} to vc")
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co/host/host/staff id to invite u to vc, <$@{data.message.author.nickname}$>")
			if x.lower()=="/inviteall" and c==[]:
				if x.lower() not in l:
					try:
						h=subclient.get_all_users(start=0,size=1000).profile.userId
						m=len(h)
						for u in h:
							try:
								subclient.invite_to_chat(userId=u,chatId=data.message.chatId)
							except Exception as e:
								print(e)
								pass
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]Invited {m} users in GC")
						print(f"invited {data.message.author.nickname} to vc")
					except Exception as e:
						print(e)
						subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co/host/host/staff id to invite u to vc, <$@{data.message.author.nickname}$>")
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Inviteall command is locked")
					except:
						pass
			if x.lower()=="/pm" and c==[]:
				if x.lower() not in l:
					try:
						subclient.start_chat(userId=data.message.author.userId,message="Hey Alexa here !")
						subclient.send_message(chatId=data.message.chatId,message=f"Check your pm <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
						print(f"invite {data.message.author.nickname} to pm")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Pm command is locked <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="/startvc" and c==[]:
				if x.lower() not in l:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Starting VC in 5 seconds")
						time.sleep(2)
						client.start_vc(comId=cid,chatId=data.message.chatId,joinType=1)
						#subclient.send_message(chatId=data.message.chatId,message=f"Vc started")
						print(f"VC started")
					except Exception as e:
						print(e)
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co/host/host id to run that command, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Start command is locked <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="/endlive" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="Ending VC in 5 seconds")
					time.sleep(5)
					client.end_vc(comId=cid,chatId=data.message.chatId,joinType=2)
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic]I dont have co/host/host/staff id to run that command, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
			if x.lower()=="/onlinemem" and c==[]:
				if x.lower() not in l:
					try:
						o=""
						q=subclient.get_online_users(start=0,size=1000)
						for uid in q.profile.nickname:
							o=o+uid+"\n"
						subclient.send_message(chatId=data.message.chatId,message=f"""[c]Online Members
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
						print("done")
					except Exception as e:
						print(e)
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Members command is locked")
					except:
						pass

			if x.lower()=="/goodmorning" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[cb]Good morning <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/follow" and c==[]:
				try:
					subclient.follow(userId=data.message.author.userId)
					subclient.send_message(chatId=data.message.chatId,message=f"[c]I started following <${data.message.author.nickname}$> ",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/goodevening" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[cb] Good Evening <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/love":
				try:
					for i in c:
						msg = i + " null null "
						msg = msg.split(" ")
						msg[1]
						subclient.send_message(chatId=data.message.chatId, message=f"""[c]-----------------
[c]Match ❤️  {random.randint(0,100)}%
[c]---------------""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/Hate":
				try:
					for i in c:
						msg = i + " null null "
						msg = msg.split(" ")
						msg[1]
						subclient.send_message(chatId=data.message.chatId, message=f"""[c]-----------------
[c]Hate 💔  {random.randint(0,100)}%
[c]---------------""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/dance" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
(_＼ヽ
　 ＼＼ .Λ＿Λ.
　　 ＼(　ˇωˇ)　
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
`ノ ) 　 Lﾉ
(_／""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/help" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[c]Alexa Commands
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁     💕 /global
💕 /say ( Bot will say that line )
💕 /pm ( alexa will pm you)
💕 /goodmorning 
💕 /unlock ( admin command)
💕 /startvc  
💕 /dance
💕 /goodnight 
💕 /inviteall (100 users will be invited but newbies)
💕 /play ( maybe not working it will be fixed later)

💕 /goodnight
💕 /endlive ( to close live mode)
💕 /meme (not available right now )
💕 /aboutalexa
💕 /admin ( for talking to Bot admin)
💕 /info
💕 /chocolate 
💕 /dance
💕 /joke ( will be available later)
💕 /follow     
💕 /coin ( fake coins )
💕 /onlinemem  
💕 /lock (admin command)
💕 /love ( example /love Name name) 
💕 /hate
💕 /gf

[ci]Alexa by KWEL
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/coin":
				try:
					for i in c:
						d=int(i)
						print(transaction)
						subclient.send_coins(coins=d, chatId=data.message.chatId, transactionId=transaction)
						subclient.send_message(chatId=data.message.chatId,message=f"Sent {d} coins to Host")
				except Exception as e:
					print(e)
			if x.lower()=="/goodnight" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=f"[cb]Good night <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/music" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[ci]Party all night..party all night...bidu party all night""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/nickname":
				try:
					t=''
					for i in c:
						t=t+i
						subclient.edit_profile(nickname=t)
						subclient.send_message(chatId=data.message.chatId,message=f"My name changed to {i}")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/profilepic" and c==[]:
				try:
					info = subclient.get_message_info(chatId = data.message.chatId, messageId = data.message.messageId)
					reply_message = info.json['extensions']
					if reply_message:
						image = info.json['extensions']['replyMessage']['mediaValue']
						filename = image.split("/")[-1]
						filetype = image.split(".")[-1]
						urllib.request.urlretrieve(image, filename)
						with open(filename, 'rb') as fp:
							for i in range(1,8):
								try:
									subclient.edit_profile(icon=fp)
								except Exception as e:
									subclient.send_message(data.message.chatId, message="Profile pic changed",replyTo=data.message.messageId)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/playlist" and c==[]:
				try:
					files=os.listdir("music")
					o=""
					for f in files:
						o=o+f+"\n"
					subclient.send_message(chatId=data.message.chatId,message=f"""
[c]Music Playlist
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/gf" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[bi] <${data.message.author.nickname}$> are single (づ｡◕‿‿◕｡)づ
[i]I m here for you...""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/joke" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""[i]joke command will be available soon or later """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/8ball":
				try:
					subclient.send_message(chatId=data.message.chatId,message=str(random.choice(lis)),replyTo=data.message.messageId)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/play":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					mx=random.choice(os.listdir("music"))
					if x.lower() not in l:
						sounds=f"music/{mx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="audio")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message="command is locked")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="command works only in pm, type /pm to make Alexa join pm")
					except:
						pass
			if x.lower()=="/meme":
				if subclient.get_chat_thread(data.message.chatId).title!=None:
					hx=random.choice(os.listdir("memes"))
					if x.lower() not in l:
						sounds=f"memes/{hx}"
						with open(sounds,"rb") as f:
							try:
								subclient.send_message(chatId=data.message.chatId,file=f,fileType="image")
								print(f"Info requested by {data.message.author.nickname}")
							except Exception as e:
								print(e)
					else:
						try:
							subclient.send_message(chatId=data.message.chatId,message=" command is locked")
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message="command works only in pm, type /pm to make Alexa join pm")
					except:
						pass
			if x.lower()=="/admin" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="                                                                        Alexa's admin : http://aminoapps.com/p/9rkn9p                                                                                                              ")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/aboutme" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=""" {data.message.author.userId} are a good person,you will get girlfriend/boyfriend here for sure""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/chocolate" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
╔╦╦
╠╬╬╬╣
╠╬╬╬╣ I ♥
╠╬╬╬╣ Chocolate
╚╩╩╩╝""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="?check" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""                                                                                                                                                                                    
╔     I'M ONLINE     ╝                                                                                                                                                                                       """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/iloveyou" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=""" I LOVE YOU TOO """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/will you marry me?" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=""" I wish i could but I can't :') because I'm just a robot """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/Hi" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=""" !<${data.message.author.nickname}$>Meaw 🐈 """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/whatsyourname?" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=""" My name is alexa  👀 why are you asking? you love me? """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/doyouloveme?" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=""" No i don't love <${data.message.author.nickname}$> """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			if x.lower()=="/ihy" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message=""" I hate <${data.message.author.nickname}$> too 👀 """)
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)