import os
os.system('clear')
print('ListenCloud MiniProgram\n\n启动中请等待…')
import requests,re,random
from urllib.parse import quote
from bs4 import BeautifulSoup
urlList=[]
os.system('clear')
print('音乐工具 v5.1 - ListenCloud 小程序版\nListenCloud Inc. ListenCloud MiniProgram\n©2024～2026 ListenCloud Inc. 保留所有权利\n')
def get_input():
    name=input('输入名称(singer歌手下载)：')
    if name=='singer':
        num=random.randint(1,68)
        name=input('输入ID：')
        testURL='http://www.2t58.com/singer/{}.html'.format(name)
        testRES=requests.get(testURL)
        testB=BeautifulSoup(testRES.text,'lxml')
        t=testB.find_all('title')
        t=str(t)[8:-21]
        t=list(t)
        for i in t:
            if i.isdigit() or i=='[' or i==']' or i=='全' or i=='部' or i=='歌' or i=='曲' or i=='第' or i=='页':
                t.remove(i)
        t=''.join(t)
        t=t[(len(t)//2)+2:]
        page=int(input('输入页数（一页68项）：'))
        pswd=input('输入过滤词（空代表用默认，多个词用英文,分隔）：')
        if pswd=='':
            pswd='Live,live,现场,铃声,片段,伴奏,纯音乐'
        pswd=pswd.split(',')
        for i in range(page):
            url='http://www.2t58.com/singer/{}/{}.html'.format(name,i+1)
            urlList.append(url)
    else:
        num=random.randint(1,68)
        page=int(input('输入页数：'))
        for i in range(page):
            url='http://www.2t58.com/so/{}/{}.html'.format(quote(name),i+1)
            urlList.append(url)
    return [name,t,pswd]
headers={'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh;q=0.9','Connection':'keep-alive','Content-Length':'26','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Cookie':'Hm_lvt_b8f2e33447143b75e7e4463e224d6b7f=1690974946; Hm_lpvt_b8f2e33447143b75e7e4463e224d6b7f=1690976158','Host':'www.2t58.com','Origin':'http://www.2t58.com','Referer':'http://www.2t58.com/song/bWhzc3hud25u.html','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
myChoose1=[]
def music(name,t,pswd):
    count=0
    for i in urlList:
        response=requests.get(i)
        ex='<div class="name"><a href="/song/(.*?).html" target="_mp3">.*?</a></div>'
        musicIndex=re.findall(ex,response.text,re.S)
        myChoose1.append(musicIndex)
    all=0
    for i in myChoose1:
        all=all+len(i)
    print('共有'+str(all)+'首歌曲！')
    for i in myChoose1:
        for j in i:
            data={'id':j,'type':'music'}
            url2='http://www.2t58.com/js/play.php'
            try:   
                response2=requests.post(url2,headers=headers,data=data)
                json_data=response2.json()
                musicList=json_data['url']
                musicResponse=requests.get(musicList)
                try:
                    filename=json_data['title']+'.mp3'
                    rfn=filename
                except TypeError:
                    filename=str(random.randint(10000000,99999999))+'.mp3'
                    rfn='?unknown?.mp3'
                if len(filename)>60:
                    filename=str(random.randint(10000000,99999999))+'.mp3'
                    rfn=json_data['title']+'.mp3'
                if '?' in filename or '|' in filename or '\\' in filename or '/' in filename or ':' in filename or '*' in filename or '<' in filename or '>' in filename or '…' in filename or "'" in filename or '"' in filename or '^' in filename:
                    filename=str(random.randint(10000000,99999999))+'.mp3'
                    rfn=json_data['title']+'.mp3'
                os.system('clear')
                print('音乐下载器 v5.1 - ListenCloud 小程序版\nListenCloud Inc. ListenCloud MiniProgram\n©2024～2026 ListenCloud Inc. 保留所有权利\n\n正在下载第'+str(count)+'项，共'+str(all)+'项(进度：'+str((count/all)*100)+'%)')
                count+=1
                with open(t+'/'+filename,'wb') as f:
                    f.write(musicResponse.content)
                    print('已下载：'+rfn[:-4]+'，消耗'+str(os.path.getsize(t+'/'+filename))+' 字节空间')
                if os.path.getsize(t+'/'+filename)<=109000:
                    print(rfn[:-4]+'需开通VIP才可收听，已删除！')
                    os.remove(t+'/'+filename)
                if os.path.getsize(t+'/'+filename)>=116000 and os.path.getsize(t+'/'+filename)<=116500:
                    print(rfn[:-4]+'无音源，已删除！')
                    os.remove(t+'/'+filename)
                for i in pswd:
                    if i in filename:
                        print(rfn[:-4]+'包含设置的过滤词，已删除！')
                        os.remove(t+'/'+filename)
                        break
            except Exception as e:
                os.system('clear')
                print('音乐下载器 v5.1 - ListenCloud 小程序版\nListenCloud Inc. ListenCloud MiniProgram\n©2024～2026 ListenCloud Inc. 保留所有权利\n\n正在下载第'+str(count)+'项，共'+str(all)+'项(进度：'+str((count/all)*100)+'%)')
                count+=1
                with open('Download.log','a') as f:
                    f.write('Error:'+str(e)+'\n')
                print('发生错误，已保存信息！')
                continue
def lyric(song_name,song_id):
    url='http://music.163.com/api/song/lyric?id={}&lv=-1&kv=-1&tv=-1'.format(song_id)
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36','Referer': 'https://music.163.com/','Host': 'music.163.com'}
    res=requests.get(url=url,headers=headers).text
    json_obj=json.loads(res)
    try:
        lyric=json_obj['lrc']['lyric']
    except KeyError:
        input('获取失败！')
        quit()
    c=input('1.LRC文件\n2.TXT文件\n请选择(1/2)：')
    if c=='2':
        reg=re.compile(r'\[.*\]')
        lrc_text=re.sub(reg,'',lyric).strip()
        return [song_name,lrc_text,'.txt']
    if c=='1':
        return [song_name,lyric,'.lrc']
    else:
        quit()
def get_signature(text):
    new_md5=md5()
    new_md5.update(text.encode(encoding='utf-8'))   
    signature=new_md5.hexdigest()
    return signature
def get_list(keyword):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'}
    mid='ccc842dce7da774774ce9278c0591119'
    url='https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime={time}&mid={mid}&uuid={mid}&dfid=0R7g5f2OX6eY2EBfN92rrRN0&keyword={keyword}&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature={signature}'
    key_code='NVPh5oo715z5DIWAeQlhMDsWXXQV4hwtappid=1014bitrate=0callback=callback123clienttime={time}clientver=1000dfid=0R7g5f2OX6eY2EBfN92rrRN0filter=10inputtype=0iscorrection=1isfuzzy=0keyword={keyword}mid={mid}page=1pagesize=30platform=WebFilterprivilege_filter=0srcappid=2919token=userid=0uuid={mid}NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt'
    millis=str(round(time.time()*1000))
    p=key_code.format(time=millis,mid=mid,keyword=keyword)
    signature=get_signature(p)
    search_url=url.format(keyword=keyword,time=millis,signature=signature,mid=mid)
    list_res=requests.get(search_url,headers=headers)
    return list_res
def show_list(song_list):
    all=[]
    for i,song in enumerate(song_list):
        a=[]
        name=song.get('SongName')
        artist=song.get('SingerName')
        a.append(artist)
        a.append(name)
        all.append(a)
        print(f'版本{i+1}\n名称：{song.get("SongName")}\n艺术家：{song.get("SingerName")}\nID：{song.get("EMixSongID")}\n')
    return all
def save_music(num,song_list,si):
    info_url=f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id={song_list[int(num)-1].get("EMixSongID")}'
    headers2={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47','Cookie':'kg_mid=ccc842dce7da774774ce9278c0591119; kg_dfid=0R7g5f2OX6eY2EBfN92rrRN0; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1696760245; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1696762195'}
    info_res=requests.get(info_url, headers = headers2)
    try:
        m_url=info_res.json()['data']['play_url']
        m_res=requests.get(m_url, headers = headers2)
        singer=si[0]
        song=si[1]
        with open(singer+' - '+song+'.mp3','wb') as f:
            f.write(m_res.content)
        size=os.path.getsize(singer+' - '+song+'.mp3')
        if size<1024*1024:
            choose=input('这是付费歌曲！\n按下N移除：')
            if choose.lower()=='n':
                os.remove(singer+' - '+song+'.mp3')
                input('\n歌曲移除成功！\n回车退出…')
                quit()
        input('下载成功！')
    except TypeError:
        input('下载失败！请更换版本，然后重试。')
def change(p,t,a,l):
    audiofile=eyed3.load(p)
    audiofile.tag.title=t
    audiofile.tag.artist=a
    audiofile.tag.album=l
    audiofile.tag.album_artist=a
    audiofile.tag.save(version=eyed3.id3.ID3_DEFAULT_VERSION,encoding='utf-8')
def divFile():
    old=input('源文件路径：')
    try:
        f=open(old,'rb')
        f.close()
    except FileNotFoundError:
        print('找不到文件')
        quit()
    f=open(old,'rb')
    data=f.read()
    f.close()
    after=['.3g2','.aac','.amr','.ape',
    '.awb','.flac','.imy','.m4a','.mid',
    '.mka','.mp3','.mpga','.ogg','.ra',
    '.rtttl','.smf','.wav','.wma','.xmf']
    for i in after:
        try:
            os.mkdir('./Divisions')
        except:
            pass
        f=open('Divisions/out'+i,'wb')
        print('正在创建文件：\nDivisions/out'+i+'…',end='')
        f.write(data)
        print('Done')
        f.close()
    choose=input('是否进行压缩？(Y/n)：')
    if choose.lower()=='n':
        quit()
    import zipfile
    try:
        os.mkdir('./ZipOut')
    except:
        pass
    zip=zipfile.ZipFile('ZipOut/Out.zip',"w",zipfile.ZIP_DEFLATED)
    for path,dirnames,filenames in os.walk('Divisions'):
        fpath=path.replace(os.path.dirname('Divisions'), '')
        for filename in filenames:
            zip.write(os.path.join(path,filename),os.path.join(fpath, filename))
            print('正在处理文件：'+filename)
        zip.close()
        print('压缩完成')
if __name__=='__main__':
    f=False
    choice=input('1.歌曲下载(2t58/酷狗音乐)\n2.歌词下载(网易云音乐)\n3.更改MP3信息(EyeD3)\n4.多文件后缀创建(ZipFile)\n请选择(1/2/3/4)：')
    if choice=='1':
        f=True
        ch2=input('选择源(1.2t58，2.酷狗音乐)\n请输入：')
        if ch2=='1':
            a=get_input()
            try:
                os.mkdir(a[1])
            except:
                pass
            print('文件夹名称：'+a[1])
            music(a[0],a[1],a[2])
        if ch2=='2':
            import json,time
            from hashlib import md5
            keyword=input('输入歌曲名称：')
            list_res=get_list(keyword)
            song_list=json.loads(list_res.text[12:-2])['data']['lists']
            sl=show_list(song_list)
            num=input('版本号：')
            si=sl[int(num)-1]
            save_music(num,song_list,si)
        else:
            quit()
    if choice=='2':
        import json
        f=True
        name=input('输入歌曲名称：')
        ids=input('输入ID(网易云音乐ID)：')
        a=lyric(name,ids)
        files=open(a[0]+a[2],'w')
        files.write(a[1])
        files.close()
        print('文件写入完成！')
    if choice=='3':
        f=True
        import eyed3
        path=input('文件路径：')
        title=input('输入标题：')
        artist=input('输入作者：')
        album=input('输入专辑：')
        change(path,title,artist,album)
    if choice=='4':
        f=True
        divFile()
    if f:
        os.system('clear')
        print('ListenCloud MiniProgram\n\n退出中请等待…')