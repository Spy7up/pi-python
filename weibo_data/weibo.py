# _*_ coding;utf-8 _*_

import json
import requests
import time
import datetime
import pymysql

url = 'https://weibo.com/ajax/statuses/hot_band'
params = {
    'sudaref': 'weibo.com',
    'retcode': 6102,
    'type': 1,
    'cate': 'realtimehot',
    '_t': 0,
    'callback': 'STK_' + str(time.time()).replace('.', '')[:-3],
}
headers = {
    'Referer': 'https://weibo.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'SUB=_2AkMTYDr7f8NxqwFRmfgRymzqa411zwDEieKlPMsgJRMxHRl-yT9vqm8-tRB6OOAUFGjK1MFoo0SNtVoQJ1U6_Dfj0_yh; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWe6YdYF_fOnlQmgnamwefr; SINAGLOBAL=1649305209992.2822.1681700302203; ULV=1681700302204:1:1:1:1649305209992.2822.1681700302203:; wb_view_log=1536*8641.25; XSRF-TOKEN=BzwCi-BR2YUWp27FYEaMaqp4; WBPSESS=dyscpFUgaqyCOptJAjoGR5Xv9QyF5M6yCd6pMUuxgksqcF5FBayDgZKa_g6yJdQp2qIq-tQE6HC-bRjSF3wsrurFpUtVPBkdrMnwT4YpWAHwx3meYeffIG3Jpwf3C7GPBJyQAEDXwsdHd_2QhSKHlJJsOmYISdqEFG3KTHTXB5M='
}

# 连接MySQL
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="weibo_data"
)

# 在前面加上
requests.packages.urllib3.disable_warnings()
response = requests.get(url, params=params, headers=headers, verify=False)

if connection.open:
    # 创建数据表
    cursor = connection.cursor()
    if response.status_code == 200:
        text = response.text
        try:
            # 解析JSON数据
            parsed_data = json.loads(text)
            # 取出band_list列表
            band_list = parsed_data.get("data", {}).get("band_list", [])
            # 将数据插入到数据表
            for data in band_list:
                if data:
                    #排除广告
                    if "ad_type" in data:
                        continue
                    else:
                        sql = "INSERT INTO hot_search_all (word_scheme, star_word, star_name, fun_word, raw_hot, subject_label, subject_querys, extension, rank, category, realpos, note, topic_flag, num, channel_type, flag, onboard_time, label_name, ad_info, expand, emoticon, word) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        val = (data['word_scheme'], data['star_word'], str(data['star_name']), data['fun_word'], data['raw_hot'], data['subject_label'], data['subject_querys'], data['extension'], data['rank'], data['category'], data['realpos'], data['note'], data['topic_flag'], data['num'], data['channel_type'], data['flag'], data['onboard_time'], data['label_name'], str(data['ad_info']), data['expand'], data['emoticon'], data['word'])
                        cursor.execute(sql, val)
                        connection.commit()
        except json.JSONDecodeError:
            print("JSON解码错误")
    else:
        print(f"请求失败，状态码：{response.status_code}")

# 关闭连接
cursor.close()
connection.close()
