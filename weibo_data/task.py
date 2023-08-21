# _*_ coding;utf-8 _*_

import logging
import schedule
import time
import subprocess

# 配置日志
logging.basicConfig(filename='scheduler.log', level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# 定义任务
def run_weibo():
    try:
        subprocess.call(["python3", "weibo.py"])  # 调用weibo.py脚本
        logging.info("定时任务已成功执行")
    except Exception as e:
        logging.error(f"定时任务执行错误：{e}")

# 定义定时器
schedule.every(10).minutes.do(run_weibo)  # 每5分钟执行一次任务

# 运行定时器
while True:
    schedule.run_pending()  # 执行所有待运行的任务
    time.sleep(1)  # 暂停1秒
