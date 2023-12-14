import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd #读取csv文件的库

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


header = ["评价", "评分"]
f=open("两江四湖.csv",mode="w",newline="")
csvwriter=csv.writer(f)
csvwriter.writerow(header)

url="https://you.ctrip.com/sight/guilin28/5925.html"

def scrolldown(driver,begin,step,times):

    scroll_y=begin

    for i in range(times):
        time.sleep(1)
        #用js进行滑动
        driver.execute_script("window.scrollTo(0,{})".format(scroll_y))
        scroll_y+=step



def main () :
    # 指定新的 chromedriver 路径
    driver_path = r"E:\a谷歌浏览器下载内容\chromedriver-win642\chromedriver-win64\chromedriver.exe"
    service = Service ( driver_path )
    driver = webdriver.Chrome ( service=service )
    # 使用新的 driver_path 初始化 webdriver

    # 假设 'url' 是您想要打开的网址
    driver.get ( url )
    driver.maximize_window ()
    time.sleep ( 3 )

    while True :
        user_input = input ( "请输入1以说明登陆成功: " )
        if user_input == "1" :
            break

    i = 1
    time.sleep ( 2 )
    scrolldown ( driver, 1000, 1000, 10 )

    time_sort_btn = driver.find_element ( "xpath",
                                          '//*[@id="commentModule"]/div[@class="sortList"]/span[@class="sortTag"]' )
    time_sort_btn.click ()
    get_comments ( driver, i )


def get_comments(driver,i):
    commentList=driver.find_element("xpath",'//*[@id="commentModule"]/div[@class="commentList"]')
    comment_items=commentList.find_elements("xpath",'./div[@class="commentItem"]')
    for c in comment_items:
        comment_info=c.find_element("xpath",'./div[@class="contentInfo"]/div[@class="commentDetail"]').text
        rating=c.find_element("xpath",'./div[@class="contentInfo"]/div[@class="scroreInfo"]/span[@class="averageScore"]').text
        rating = ''.join ( filter ( str.isdigit, str(rating) ) )
        print(comment_info,rating)
        csvwriter.writerow ( [comment_info, rating] )
    next_btn=driver.find_element("xpath",'//*[@id="commentModule"]/div[@class="myPagination"]/ul[@class="ant-pagination"]/li[@title="下一页"]/span[@class="ant-pagination-item-comment"]')
    driver.execute_script ( "arguments[0].click();", next_btn )
    i=i+1
    if i<1000:
        get_comments(driver,i)
        time.sleep ( 2 )


if __name__ == "__main__":
    main()