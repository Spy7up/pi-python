# -*- coding:utf-8 -*-

import schedule
import requests
import json
import time

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://glados.rocks",
    "Pragma": "no-cache",
    "Referer": "https://glados.rocks/console/checkin",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

data = {"token": "glados.one"}
url = "https://glados.rocks/api/user/checkin"

def job():
    auth = get_auth()
    headers["Authorization"] = auth["Authorization"]
    headers["Cookie"] = auth["Cookie"]
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # 解析响应内容，并获取需要的信息
    resp_json = json.loads(response.text)
    code = resp_json["code"]
    message = resp_json["message"]
    list_data = resp_json["list"]
    first_item = list_data[0]  # 获取列表的第一项
    with open("log.log", "a", encoding="utf-8") as f:
        f.write("[%s] [code:%s] [message:%s] [current_point:%s] \n" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), code, message, first_item["balance"]))

def get_auth():
    with open("auth.json", "r") as f:
        auth = json.load(f)
        return {"Authorization": auth["Authorization"], "Cookie": auth["cookie"]}

def main():
    # 每天 10 点执行一次 job 函数
    schedule.every().day.at("10:00").do(job)
    print("----启动定时任务----")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
    #job()
