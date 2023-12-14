import requests
import pandas as pd
import re
import os
import datetime  # 转换时间用

# 这些功能可以帮助转换时间和性别
def trans_time(v_str):
	"""转换GMT时间为标准格式"""
	GMT_FORMAT = '%a %b %d %H:%M:%S +0800 %Y'
	timeArray = datetime.datetime.strptime(v_str, GMT_FORMAT)
	ret_time = timeArray.strftime("%Y-%m-%d %H:%M:%S")
	return ret_time

def tran_gender(gender):
    # 请在这里填入转换性别的函数内容
    pass

# 微博ID
weibo_id = '4806418774099867'

headers = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
}

# 初始化lists
page_list = []
id_list = []
text_list = []
time_list = []
like_count_list = []
source_list = []
user_name_list = []
user_id_list = []
user_gender_list = []
follow_count_list = []
followers_count_list = []

max_id = None
page = 1

while True:
    # 获取URL
    if page == 1:
        url = f'https://m.weibo.cn/comments/hotflow?id={weibo_id}&mid={weibo_id}&max_id_type=0'
    else:
        if max_id == '0':
            print('max_id is 0, break now')
            break
        url = f'https://m.weibo.cn/comments/hotflow?id={weibo_id}&mid={weibo_id}&max_id_type=0&max_id={max_id}'

    # 向微博页面发送请求
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.json())
    print(r.encoding)
    print ( r.text )
    # 解析数据
    datas = r.json()['data']['data']
    for data in datas:
        # page_list.append(page)
        # id_list.append(data['id'])
        dr = re.compile(r'<[^>]+>', re.S)
        text2 = dr.sub('', data['text'])
        text_list.append(text2)
        # time_list.append(trans_time(v_str=data['created_at']))
        # like_count_list.append(data['like_count'])
        # source_list.append(data['source'])
        user_name_list.append(data['user']['screen_name'])
        # user_id_list.append(data['user']['id'])
        # user_gender_list.append(tran_gender(data['user']['gender']))
        # follow_count_list.append(data['user']['follow_count'])
        # followers_count_list.append(data['user']['followers_count'])

    # 更新max_id和页码
    max_id = r.json()['data']['max_id']
    page += 1

# 保存数据到CSV文件
v_comment_file = 'comments.csv'
df = pd.DataFrame({
    '微博id': [weibo_id] * len(time_list),
    # '评论页码': page_list,
    # '评论id': id_list,
    # '评论时间': time_list,
    # '评论点赞数': like_count_list,
    # '评论者IP归属地': source_list,
    '评论者姓名': user_name_list,
    # '评论者id': user_id_list,
    # '评论者性别': user_gender_list,
    # '评论者关注数': follow_count_list,
    # '评论者粉丝数': followers_count_list,
    '评论内容': text_list
})

if os.path.exists(v_comment_file):
    header = False
else:
    header = True

df.to_csv(v_comment_file, mode='a+', index=False, header=header, encoding='utf_8_sig')
print(f'结果保存成功:{v_comment_file}')
