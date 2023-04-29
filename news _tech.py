import html5lib ,re ,requests,win32com.client
import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]
from bs4 import BeautifulSoup, NavigableString

from ai_news_link import show_ai_news

import requests
import pyttsx3
# import speech_recognition as sr
import datetime
import requests
from requests import get
engine = pyttsx3.init()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

false=True

def sp(audio):
    speak = win32com.client.Dispatch("SAPI.SpVoice")
    speak.Speak(audio)

def Tell_time():
    import datetime
    hour =int(datetime.datetime.now().hour)
    minutes =int(datetime.datetime.now().minute)
    seconds=int(datetime.datetime.now().second)
    return f"{hour}:{minutes}:{seconds}"

def greet():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning RVC Sir.")
        sp("Good Morning RVC Sir.")

    elif hour>=12 and hour<19:
        print(("Good Afternoon! RVC Sir."))
        sp("Good Afternoon! RVC Sir.")
    else:
        print(("Good Evening RVC Sir. ")) 
        sp("Good Evening RVC Sir. ")

def collect_news_link():
        url='https://techcrunch.com/'
        r=requests.get(url)
        html_doc=r.content

        soup=BeautifulSoup(html_doc,'html.parser')
        # print(soup.prettify())
        news_links=soup.select(".post-block__title__link")
        link_news=[]
        for xi in news_links:
                    link_news.append(xi.get('href'))
        return (list(set(link_news)))

def ai_news_bool():
    a=show_ai_news()
    if a==True:
        print("An New AI news has also been added sir")
        sp("An New AI news has also been added sir")
    else:
         pass
    
def collect_news():

    url='https://techcrunch.com/'
    r=requests.get(url)
    html_doc=r.content

    soup=BeautifulSoup(html_doc,'html.parser')
    # print(soup.prettify())
    new_head_lines=soup.select(".post-block__title__link")



    new_list=[]

    def list_remover_of_t_n(dd):
        res = []
        for sub in dd: 
            res.append(sub.replace("\t", ""))
        gg=[]
        for ss in res:
                gg.append(ss.replace('\n',''))   
        return gg[0]



    for news in range(len(new_head_lines)):
        if len(new_head_lines[news].contents)==1 and ((new_head_lines[news].contents) not in new_list):

            new_list.append(list_remover_of_t_n(new_head_lines[news].contents))

    return list(set(new_list))

def read_news(news,news_links):
        
        cc=[]    
        dd=[]  
        bb=news_links  
        print()
        with open("database.csv",'r+') as f:
                aa=f.readlines()
                for i in range(len(aa)):
                    if aa[i].startswith("Time"):
                        continue
                    else:
                         dd.append(aa[i])

                for i in range(len(bb)):
                    if f'{bb[i]}\n' not in dd:
                         cc.append(bb[i])
        if len(cc)!=0:
            print(f"Time is {Tell_time()}")
            sp(f"Time is {Tell_time()}")
            newss_collects=news
            print("I am starting with latest news")
            sp("I am starting with latest news")
            
            counts=['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth','thirteenth','''fourteenth''',
                    'fifteenth','sixteenth','seventeenth','eighteenth','nineteenth','twentieth',
                    'Twenty-First','Twenty second ','Twenty third','Twenty fourth','Twenty fifth','Twenty sixth','Twenty seventh','Twenty eighth','Twenty ninth','Thirtieth']
            for i in range(len(newss_collects)):
                print(f"{counts[i]} news is : {newss_collects[i]}")
                sp(f"{counts[i]} news is : {newss_collects[i]}")
            sp("Thats all for Now sir...")
            sp("now i am attaching all the news Links in the database sir...")
            print()
            


            with open("database.csv",'a') as f:

                f.write('\n')
                f.write(f'Time and Date-: {datetime.date.today()} {Tell_time()} ')
                f.write("\n")
                for i in range(len(cc)):
                    f.write(f"{cc[i]}\n")    
            
        else:
                print("There are No Latest news to be told sir")
                sp("There are No Latest news to be told sir")
        



if __name__=="__main__":
    # import time
    # while false:
        
        news=collect_news()
        news_link=collect_news_link()
        greet()
        read_news(news,news_link)
        ai_news_bool()
        print("signing off sir , have a good day ahead")
        sp("signing off sir , have a good day ahead")