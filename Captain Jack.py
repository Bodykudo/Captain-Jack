import discord, asyncio, random, time, requests, json, os, pyimgur
from urllib.request import urlopen

characters={
    '!luffy':[("**Monkey D. Luffy**\nAge : 19\nBirthday : May 5th\nHeight : 174 cm\nBounty : 500.000.000","http://i.imgur.com/0h950jm.png")],
    '!zoro':[("**Roronoa Zoro**\nAge : 21\nBirthday : November 11th\nHeight : 181 cm\nBounty : 320.000.000","http://i.imgur.com/DESTc2W.png")],
    '!nami':[("**Nami**\nAge : 20\nBirthday : July 3rd\nHeight : 170 cm\nBounty : 66.000.000\n3 Sizes :-\nBreasts : 98\nWaist : 58\nHip measurements : 88","http://i.imgur.com/RxZjlKQ.png")],
    '!usopp':[("**Usopp**\nAge : 19\nBirthday : April 1st\nHeight : 176 cm\nBounty : 200.000.000","http://i.imgur.com/WbrjJ4g.png")],
    '!sanji':[("**Vinsmoke Sanji**\nAge : 21\nBirthday : March 2nd\nHeight : 188 cm\nBounty : 177.000.000","http://i.imgur.com/VDxVn6p.png")],
    '!chopper':[("**Tony Tony Chopper**\nAge : 17\nBirthday : December 24th\nHeight : 90 cm\nBounty : 100","http://i.imgur.com/De2MvFg.png")],
    '!robin':[("**Nico Robin**\nAge : 30\nBirthday : February 6th\nHeight : 188 cm\nBounty : 130.000.000\n3 Sizes :-\nBreasts : 100\nWaist : 60\nHip measurements : 90","http://i.imgur.com/OfjIeQQ.png")],
    '!franky':[("**Franky**\nAge : 36\nBirthday : March 9th\nHeight : 240 cm\nBounty : 94.000.000","http://i.imgur.com/Wf6IwEm.png")],
    '!brook':[("**Brook**\nAge : 90\nBirthday : April 3rd\nHeight : 277 cm\nBounty : 83.000.000","http://i.imgur.com/ladX5xq.png")],
    '!jinbe':[("**Jinbe**\nAge : 46\nBirthday : April 2nd\nHeight : 301 cm\nBounty : 400.000.000","http://i.imgur.com/IpdWxOP.png")],
    '!ace':[("**Portgas D. Ace**\nAge : 20\nBirthday :  January 1st\nHeight :  185cm\nBounty : 550.000.000","http://i.imgur.com/fPxGiMD.png")],
    '!crocodile':[("**Crocodile**\nAge : 46\nBirthday :  September 5th\nHeight :  253cm\nBounty : 81.000.000","http://i.imgur.com/jVvFs0l.png")],
    '!doflamingo':[("**Donquixote Doflamingo**\nAge : 41\nBirthday :  October 23rd\nHeight :  305cm\nBounty : 340.000.000","http://i.imgur.com/08yKVVE.png")],
    '!dragon':[("**Monkey D. Dragon**\nAge : Unknown\nBirthday : October 5th\nHeight : Unknown\nBounty : Unknown","http://i.imgur.com/EDTecEA.png")],
    '!enel':[("**Enel**\nAge : Unknown\nBirthday :  May 6th\nHeight : Unknown\nBounty : No Bounty","http://i.imgur.com/z0Pf5HL.png")],
    '!kuma':[("**Bartholomew Kuma**\nAge : 47\nBirthday :  February 9th\nHeight :  689cm\nBounty : 296.000.000","http://i.imgur.com/MgyO9ug.png")],
    '!hancock':[("**Boa Hancock**\nAge : 31\nBirthday :  September 2nd\nHeight :  191cm\nBounty : 80.000.000\n3 Sizes :-\nBreasts : 111\nWaist : 61\nHip measurements : 91","http://i.imgur.com/FtQNc4Q.png")],
    '!mihawk':[("**Dracule Mihawk**\nAge : 43\nBirthday :  March 9th\nHeight :  198cm\nBounty : Unknown","http://i.imgur.com/rxbvp9s.png")],
    '!moria':[("**Gekko Moria**\nAge : 50\nBirthday :  September 6th\nHeight :  692cm\nBounty : 320.000.000","http://i.imgur.com/kegsOQQ.png")],
    '!roger':[("**Gol D. Roger**\nAge : 53\nBirthday : December 31st\nHeight :  Unknowncm\nBounty : Unknown","http://i.imgur.com/bUesaVg.png")],
    '!garp':[("**Monkey D. Garp**\nAge : 78\nBirthday : May 2nd\nHeight : Unknown\nBounty : No Bounty","http://i.imgur.com/DOxW2n1.png")],
    '!sabo':[("**Sabo**\nAge : 22\nBirthday :  March 20th\nHeight :  187cm\nBounty : Unknown","http://i.imgur.com/pEbflDt.png")],
    '!rayleigh':[("**Silvers Rayleigh**\nAge : 78\nBirthday : May 13th\nHeight : Unknown\nBounty : Unknown","http://i.imgur.com/o0G3eeE.png")],
    '!law':[("**Trafalgar D. Water Law**\nAge : 26\nBirthday :  October 6th\nHeight : 191cm\nBounty : 500.000.00","http://i.imgur.com/qroRmlb.png")],
    '!vivi':[("**Nefeltari Vivi**\nAge : 18\nBirthday :  February 2nd\nHeight :  Unknown\nBounty : No Bounty","http://i.imgur.com/yoGO8JY.png")],
    '!bonney':[("**Jewelry Bonney**\nAge : 24\nBirthday : September 1st\nHeight : 174cm\nBounty : 140.000.000","http://i.imgur.com/SEwHw9Y.png")],
    '!kid':[("**Eustass Kid**\nAge : 23\nBirthday : January 10th\nHeight : 205cm\nBounty : 470.000.000","http://i.imgur.com/rf3iC2s.png")],
    '!killer':[("**Killer**\nAge : 27\nBirthday : February 2nd\nHeight : 195cm\nBounty : 200.000.000","http://i.imgur.com/apdau8Y.png")],
    '!apoo':[("**Scratchmen Apoo**\nAge : 31\nBirthday :  March 19th\nHeight : 256cm\nBounty : 350.000.000","http://i.imgur.com/3yUfoWk.png")],
    '!hawkins':[("**Basil Hawkins**\nAge : 31\nBirthday : September 9th\nHeight : 210cm\nBounty : 320.000.000","http://i.imgur.com/6agmyTj.png")],
    '!capone bege':[("**Capone Bege**\nAge : 42\nBirthday : January 17th\nHeight : 1666cm\nBounty : 300.000.000","http://i.imgur.com/nnprZFa.png")],
    '!x drake':[("**X Drake**\nAge : 33\nBirthday : October 24th\nHeight : 233cm\nBounty : 222.000.000","http://i.imgur.com/0apM82w.png")],
    '!urouge':[("**Urouge**\nAge : 47\nBirthday : August 1st\nHeight : 388cm\nBounty : 108.000.000","http://i.imgur.com/wqHXls5.png")],
    '!shanks':[("**Shanks**\nAge : 39\nBirthday : March 9th\nHeight : Unknown\nBounty : Unknown","http://i.imgur.com/eVxYt7d.png")],
    '!whitebeard':[("**Edward Newgate**\nAge : 72\nBirthday : April 6th\nHeight : Unknown\nBounty : Unknown","http://i.imgur.com/ZwcAU7S.png")],
    '!white beard':[("**Edward Newgate**\nAge : 72\nBirthday : April 6th\nHeight : Unknown\nBounty : Unknown","http://i.imgur.com/ZwcAU7S.png")],
    '!blackbeard':[("**Marshall D. Teach**\nAge : 40\nBirthday : August 3rd\nHeight : 344cm\nBounty : Unknown","http://i.imgur.com/NDGLVxN.png")],
    '!black beard':[("**Marshall D. Teach**\nAge : 40\nBirthday : August 3rd\nHeight : 344cm\nBounty : Unknown","http://i.imgur.com/NDGLVxN.png")],
    '!bigmom':[("**Charlotte Linlin**\nAge : 68\nBirthday : February 15th\nHeight : Unknown\nBounty : Unknown","http://i.imgur.com/OTTBPyo.png")],
    '!big mom':[("**Charlotte Linlin**\nAge : 68\nBirthday : February 15th\nHeight : Unknown\nBounty : Unknown","http://i.imgur.com/OTTBPyo.png")],
    '!kaido':[("**Kaido**\nAge : Unknown\nBirthday : May 1st\nHeight : Unknown\nBounty : Unknown","http://i.imgur.com/70LkGcm.png")]
}

client = discord.Client()
user = 'User'
key = 'Key'
Id = "Id"
client2 = pyimgur.Imgur(Id)

@client.event
async def on_ready():
    os.system('title Captain Jack')
    os.system('color 30')
    print('Logged in as '+client.user.name+'\nID : '+client.user.id+'\nIn '+str(len(client.servers))+' servers\n------')
    await client.change_presence(game=discord.Game(name='With The Pirates'))

def DownloadFile(url,file):
    f = open(file,'wb')
    f.write(requests.get(url).content)
    f.close()

@client.event
async def on_message(message):
    author = message.author
    if not message.author.bot:
        if message.content.startswith(client.user.mention):
            await client.send_typing(message.channel)
            txt = message.content.replace(message.server.me.mention,'') if message.server else message.content
            r = json.loads(requests.post('https://cleverbot.io/1.0/ask', json={'user':user, 'key':key, 'nick':'frost', 'text':txt}).text)
            if r['status'] == 'success':
                await client.send_message(message.channel, str(author.mention)+", "+r['response'] )
        try:
            characters[message.content][0]
            await client.send_message(message.channel, characters[message.content][0][0]+"\n"+characters[message.content][0][1])
        except:
            if message.content.startswith('!messages'):
                counter = 0
                tmp = await client.send_message(message.channel, 'Calculating messages...')
                async for log in client.logs_from(message.channel, limit=100):
                    if log.author == message.author:
                        counter += 1
                await client.edit_message(tmp, 'You have {} messages.'.format(counter))
                await client.send_message(message.channel, character[0][0]+"\n"+character[0][1])
            elif message.content.startswith('!clear') and str(message.channel)=="admin":
                channelname=message.content.split('!clear ')[1]
                channel = discord.utils.get(client.get_all_channels(), server__name=str(message.server), name=str(channelname))
                tmp = await client.send_message(channel, 'Clearing messages...')
                async for msg in client.logs_from(channel):
                    await client.delete_message(msg)
            elif message.content.startswith('!skills '):
                tmp1 = await client.send_message(message.channel, 'Wait please...')
                name = message.content.split('!skills ')[1]
                DownloadFile("http://api.micetigri.fr/skills/profil/"+str(name)+"/","D:/Bodykudo/Work/Captain Jack/skills/"+str(name)+".png")
                await client.delete_message(tmp1)
                await client.send_file(message.channel, "D:/Bodykudo/Work/Captain Jack/skills/"+str(name)+".png")
                os.remove("D:/Bodykudo/Work/Captain Jack/skills/"+str(name)+".png")
            elif message.content.startswith('!image '):
                tmp1 = await client.send_message(message.channel, 'Wait please...')
                url = message.content.split('!image ')[1]
                image = url.split('/')[-1]
                image = image if len(image.split('.')) == 2 else image+".png"
                DownloadFile(url,"D:/Bodykudo/Work/Captain Jack/images/"+str(image)+"")
                uploaded_image = client2.upload_image("D:/بودى 10/Work/Captain Jack/images/"+str(image)+"", title=str(image))
                await client.send_message(message.channel, "**"+str(uploaded_image.title)+"**\nType : **"+str(uploaded_image.type)+"**\nSize : **"+str(uploaded_image.size)+"**\n**"+str(uploaded_image.link)+"**")
                await client.delete_message(tmp1)
                os.remove("D:/Bodykudo/Work/Captain Jack/images/"+str(image)+"")
            elif message.content.startswith('!profile '):
                tmp1 = await client.send_message(message.channel, 'Wait please...')
                name = message.content.split('!profile ')[1]
                DownloadFile("https://api.mices.es/base.php/?user="+str(te)+"","D:/Bodykudo/Work/Captain Jack/profile/"+str(name)+".png")
                await client.delete_message(tmp1)
                await client.send_file(message.channel, "D:/Bodykudo/Work/Captain Jack/profile/"+str(name)+".png")
                os.remove("D:/Bodykudo/Work/Captain Jack/profile/"+str(name)+".png")
            elif message.content.startswith('!badges '):
                tmp1 = await client.send_message(message.channel, 'Wait please...')
                name = message.content.split('!badges ')[1]
                DownloadFile("http://warfenix.com/sentinel/badges/image.php?nick="+str(name)+"","D:/Bodykudo/Work/Captain Jack/badges/"+str(name)+".png")
                await client.delete_message(tmp1)
                await client.send_file(message.channel, "D:/Bodykudo/Work/Captain Jack/badges/"+str(name)+".png")
                os.remove("D:/Bodykudo/Work/Captain Jack/badges/"+str(name)+".png")
            elif message.content.startswith('!avatar '):
                tmp1 = await client.send_message(message.channel, 'Wait please...')
                name = message.content.split('!avatar ')[1]
                DownloadFile("http://outil.derpolino.shost.ca/avatar/avatar.php?p="+str(name)+"","D:/Bodykudo/Work/Captain Jack/avatar/"+str(name)+".png")
                await client.delete_message(tmp1)
                await client.send_file(message.channel, "D:/Bodykudo/Work/Captain Jack/avatar/"+str(name)+".png")
                os.remove("D:/Bodykudo/Work/Captain Jack/avatar/"+str(name)+".png")
            elif message.content.startswith('!random'):
                character=random.choice(list(characters.keys()))
                inf1,inf2 = characters[character][0]
                await client.send_message(message.channel,str(inf1)+"\n"+str(inf2))
            elif message.content.startswith('!8ball'):
                choice1 = message.content.split('!8ball ')[1].split(' or')[0]
                choice2 = message.content.split('or ')[1]
                answer = random.choice([choice1, choice2])
                await client.send_message(message.channel,answer)
            elif message.content.startswith('!embed'):
                em = discord.Embed(title='My Embed Title', description='My Embed Content.', colour=0xDEADBF)
                em.set_author(name=client.user, icon_url=client.user.avatar_url)
                await client.send_message(message.author, embed=em)
            elif message.content.startswith('!help'):
                help='```Welcome to the Help menu of Captain Jack\n![character name] ~> shows you the image and some information about this character\n!random ~> shows the image and some information about random character\n!messages ~> to calculate your messages\n!8ball [Choice1] or [Choice2] ~> makes the bot choose one of the two choices\n!ep [episode number] ~> shows you the episode you want from one piece anime\n!ch [chapter number] ~> shows you the chapter you want from one piece manga\n!cat ~> shows you random cat image\n!guess ~> to play the guess game with the bot\n!youtube [video name] ~> to search in youtube about video\n!profile [name] ~> to show the player profile in Transformice\n!skills [name] ~> to show the player skills in Transformice\n!avatar [name] ~> to shows the player avatar in Atelier801 forums\n!badges [name] ~> to show the player badges in Atelier801 forums```'
                await client.send_message(message.author,help)
            elif message.content.startswith('!youtube '):
                Text = message.content.split('!youtube ')[1].replace(' ','+')
                link = "https://www.youtube.com/results?search_query="+str(Text)+""
                page = str(str(urlopen(link).read(),'utf-8'))
                page = page.split('href="/watch?v=')[2]
                url = "https://www.youtube.com/watch?v="+str(page.split('"')[0])+""
                title = page.split('title="')[1].split('"')[0]
                await client.send_message(message.channel, '**'+str(title)+'** \n'+url+'')
            elif message.content.startswith('!say') and str(message.channel)=="admin":
                channel = discord.utils.get(client.get_all_channels(), server__name=str(message.server), name='chat')
                message = message.content.split('!say ')[1]
                if message != None:
                    await client.send_message(channel,message)
            elif message.content.startswith('!ep'):
                ep = message.content.split('!ep ')[1]
                if int(ep) <= 791 and int(ep) > 0:
                    link = "http://toofy.co/watch.php?q=one-piece-"+ep+""
                    tmp1 = await client.send_message(message.channel, 'Wait please...')
                    DownloadFile("http://imgs.toofy.co/imgs/watch/sm/one-piece-"+str(ep)+".jpg","D:/بودى 10/Work/Captain Jack/ep/"+str(ep)+".png")
                    await client.delete_message(tmp1)
                    await client.send_message(message.channel,''+str(author.mention)+' The episode '+ep+' of One Piece!\nEnjoy!\n'+link)
                    await client.send_file(message.channel, "D:/بودى 10/Work/Captain Jack/ep/"+str(ep)+".png")
                    os.remove("D:/بودى 10/Work/Captain Jack/ep/"+str(ep)+".png")
            elif message.content.startswith('!ch'):
                ch = message.content.split('!ch ')[1]
                if int(ch) <= 869 and int(ch) > 0:
                    link2="http://www.manga.ae/one-piece1/"+ch+"/1/"
                    await client.send_message(message.channel, ''+str(author.mention)+' The chapter '+ch+' of One Piece!\nEnjoy!\n'+link2)
            elif message.content.startswith('!cat'):
                _page=str(urlopen("http://random.cat/view?i=1").read())
                __catnumbers=_page.find("Cat Count: ")
                _catnumbers=_page[__catnumbers:].find("<br />")
                catnumbers=_page[__catnumbers+11:__catnumbers+_catnumbers]
                page=str(urlopen("http://random.cat/view?i=%d" % random.randint(0, int(catnumbers))).read())
                __image=page.find('<img src="i/')
                _image=page[__image:].find('" alt=""')
                imagelink="http://random.cat/i/"+page[__image+12:__image+_image]
                await client.send_message(message.channel,imagelink)
            elif message.content.startswith('http://atelier801.com/topic?'):
                link = message.content
                f = link.split('f=')[1].split('&')[0]
                t = link.split('t=')[1].split('&')[0]
                n_comment=""
                Name_Topic=""
                last_comment=""
                creator_topic=""
                coeur=""
                if f != None and t != None:
                    tmpp = await client.send_message(message.channel, 'Wait please...')
                    fff = str(urlopen(link).read())
                    page = fff.split('class="span12"')[1].split('<div')[1].split('</div>')[0].split('class="groupe-boutons-barre-droite ">')[1]
                    if page != "  ":
                        max_page = fff.split('class="btn btn-inverse"')[1].split('/ ')[1].split('</a>')[0]
                        Last_page = str(urlopen("http://atelier801.com/topic?f="+f+"&t="+t+"&p="+max_page+"").read(),'utf-8')
                    First_page = str(urlopen("http://atelier801.com/topic?f="+f+"&t="+t+"&p=1").read(),'utf-8')
                    if page != "  ":
                        n=Last_page.split('class="numero-message"')
                        n=len(n)-1
                        n_comment=Last_page.split('class="numero-message"')[n].split('">')[1].split('</a>')[0].split('#')[1]
                    else:
                        n=First_page.split('class="numero-message"')
                        n=len(n)-1
                        n_comment=First_page.split('class="numero-message"')[n].split('">')[1].split('</a>')[0].split('#')[1]
                    if page != "  ":
                        la=Last_page.split('class="dropdown-toggle highlightit"')
                        la=len(la)-1
                        last_comment=Last_page.split('class="dropdown-toggle highlightit"')[la].split('alt="">')[1].split('</span>')[0].split('  ')[1]
                    else:
                        la=First_page.split('class="dropdown-toggle highlightit"')
                        la=len(la)-1
                        last_comment=First_page.split('class="dropdown-toggle highlightit"')[la].split('alt="">')[1].split('</span>')[0].split('  ')[1]
                    creator_topic=First_page.split('class="dropdown-toggle highlightit"')[1].split('alt="">')[1].split('</span>')[0].split('  ')[1]
                    nt = First_page.split('<ul class=\"barre-navigation  ltr\">')[1].split('</ul>')[0].split('<li>')
                    ntt = len(nt)-1
                    im = len(nt[ntt].split('<img '))
                    if im == 1:
                        Name_Topic=nt[ntt].split('class=" active">')[1].split('</a>')[0]
                    elif im == 2:
                        Name_Topic=nt[ntt].split('/>')[1].split('</a>')[0]
                    elif im == 3:
                        Name_Topic=nt[ntt].split('/>')[2].split('</a>')[0]
                    Name_Topic=Name_Topic.replace("&#39;", "\'").replace("  ", "")
                    coeur=First_page.split('class="coeur"')[1].split('</span>')[1].split('</span>')[0]
                    coeur=coeur.replace(" ", "").replace("&nbsp;", "")
                    await client.edit_message(tmpp, '**Title :** '+str(Name_Topic)+' \n**Author :** '+creator_topic+'\n**Posts :** '+n_comment+' \n **The last post :** '+last_comment+'\n'+coeur+':heart:')
            elif message.content.startswith('https://anvilgod.com/threads/'):
                m = await client.send_message(message.channel, 'Wait please...')
                link = message.content
                page = str(urlopen(link).read(),'utf-8')
                topic_title = page.split('class="titleBar">')[1].split('<h1>')[1].split('</h1>')[0]
                topic_author = page.split('class="username">')[1].split("</a>")[0]
                topic_createdAt = page.split('class="DateTime" title="')[1].split('">')[0]
                topic_pages = page.split('class="pageNavHeader">Page ')[1].split('of')[1].split('</span>')[0]
                await client.edit_message(m, topic_title+'\nAuthor : '+topic_author+'\nWas created at : '+topic_createdAt+'\nPages : '+topic_pages+' pages')
        if message.author == client.user:
            return
        if message.content.startswith('!guess'):
            await client.send_message(message.channel, 'Guess a number between 1 to 10')
            def guess_check(m):
                return m.content.isdigit()
            guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
            answer = random.randint(1, 10)
            if guess is None:
                fmt = 'Sorry, you took too long. It was {}.'
                await client.send_message(message.channel, fmt.format(answer))
                return
            if int(guess.content) == answer:
                await client.send_message(message.channel, 'You are right!')
            else:
                await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))


@client.event
async def on_message_delete(message):
    if message.author.id != client.user.id:
        channel = discord.utils.get(client.get_all_channels(), server__name=str(message.server), name='messages')
        fmt = '{0.author.mention} has deleted his message: {0.content}'
        await client.send_message(channel, fmt.format(message))

@client.event
async def on_message_edit(before, after):
    if before.author.id != client.user.id:
        channel = discord.utils.get(client.get_all_channels(), server__name=str(before.server), name='messages')
        fmt = '{0.author.mention} edited his message: {1.content}'
        await client.send_message(channel, fmt.format(after, before))

@client.event
async def on_member_join(member):
    server = member.server
    channel = discord.utils.get(client.get_all_channels(), server__name=str(server), name='welcome')
    fmt = 'Welcome {0.mention} to our server {1.name}!'
    await client.send_message(channel, fmt.format(member, server))

requests.post('https://cleverbot.io/1.0/create', json={'user':user, 'key':key, 'nick':'frost'})
client.run('Token')
