import re,datetime
def list_con(ss):
     word='Ai'
     pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
     pattern = re.compile(pattern, re.IGNORECASE)
     matches = re.search(pattern, ss)
     if matches==None:
         return False
     else:
         return True

ab=[]
ba=[]
def Tell_time():
    import datetime
    hour =int(datetime.datetime.now().hour)
    minutes =int(datetime.datetime.now().minute)
    seconds=int(datetime.datetime.now().second)
    return f"{hour}:{minutes}:{seconds}"


def show_ai_news():
    with open("database.csv","r+") as f:
        aaa =f.readlines()
        for i in range(len(aaa)):
            if(list_con(aaa[i])):
                ab.append(aaa[i])
        if len(ab)>=1:
            with open("ai_database.csv","r+") as f:
                a=f.readlines()
                cc=[]
                for i in range(len(a)):
                    if a[i].startswith("Time") or a[i].startswith('\n'):
                        continue
                    else:
                        cc.append(a[i])

                if len(cc)!=len(ab):
                    
                    with open('ai_database.csv',"a") as f:
                        f.write(f"Time and Date -:{datetime.date.today()} {Tell_time()}\n")
                        for i in range(len(ab)):
                            if ab[i] not in a:
                                f.write(f"{ab[i]}\n")
                    return True
        else:
            return False


def ai_news_data_base():
    pass

if __name__=="__main__":
    print(show_ai_news())