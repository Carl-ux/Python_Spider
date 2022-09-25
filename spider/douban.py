from bs4 import BeautifulSoup   #Web page parsing & Get data
import re                       #Regular expressions for text matching
import urllib                   #Make URL to get web page data
import xlwt                     #Excel operation
import sqlite3                  #Perform SQLite database operation

#global variable
findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)    #re.S represents match pattern
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge  = re.compile(r'<span>(\d*)人评价</span>')  
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.Crawl web pages
    #2.Parse Data  
    datalist = getData(baseurl)  
    #3.Store date
    DBPATH = "movie.db"  
    saveData(datalist,DBPATH)


#crawl web page
def getData(baseurl):
    datalist = []
    for i in range(0,10):               #Call Func askURL() 10 tirmes
        url = baseurl + str(i*25)
        html = askURL(url)

        #parse data one by one
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):     #Find strings meet the requirements to list
            data = []    #save all info of one movie
            item = str(item)

            #use re to get superlink of movies
            link = re.findall(findLink,item)[0]             #Return a list
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle,item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")          #remove Irrelevant symbol
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")                            #Leave a blank
            
            rating = re.findall(findRating,item)[0]
            data.append(rating)
            
            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?',' ',bd)         #remove <br/>
            bd = re.sub('/'," ",bd)                         #replace /
            data.append(bd.strip())                         #remove blanks

            datalist.append(data)
    
    return datalist


#Get a web page content with a specified URL
def askURL(url):
    head = {              #Simulate browser header information , Send a message to the server
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }                     #user agent
    request = urllib.request.Request(url,headers=head)
    html = ""             #web page to return
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        #func hasattr() 
        #Used to determine whether an object contains corresponding attributes.
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


#save(store) data
def saveData(datalist,db):
    #init_db(db)
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    for data in datalist:
        for index in range(len(data)):          #each coloum
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250
                (
                    info_link,pic_lnk,cname,ename,score,rated,introduction,info)
                    values(%s)'''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

def init_db(db):
    #create data table
    sql = '''
        create table movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pic_lnk text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
        )
    '''       
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()