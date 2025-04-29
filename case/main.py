# -*- encoding=utf8 -*-
__author__ = "makino"

import os
import time
import json
from datetime import datetime

# 全局变量用于统计汇总信息
today = datetime.now().strftime("%Y-%m-%d")
total_runs = 0
successful_runs = 0
duo_le_runs = 0
duo_le_success = 0
bao_wang_runs = 0
bao_wang_success = 0

def run_script(script_path):
    """
    运行指定的脚本文件
    :param script_path: 脚本文件路径
    """
    global total_runs, successful_runs, duo_le_runs, duo_le_success, bao_wang_runs, bao_wang_success
    total_runs += 1
    try:
        print(f"Running script: {script_path}")
        # 修改: 使用 os.system 替代 exec，确保脚本正确执行
        os.system(f"python {script_path}")
        successful_runs += 1
        if "duo_le" in script_path:
            duo_le_runs += 1
            duo_le_success += 1
        elif "bao_wang" in script_path:
            bao_wang_runs += 1
            bao_wang_success += 1
    except Exception as e:
        print(f"Error running script {script_path}: {e}")
        if "duo_le" in script_path:
            duo_le_runs += 1
        elif "bao_wang" in script_path:
            bao_wang_runs += 1

def print_summary():
    """
    打印汇总信息
    """
    print("\n--- Summary ---")
    print(f"Today's date: {today}")
    print(f"Total runs: {total_runs}")
    print(f"Successful runs: {successful_runs}")
    print(f"Duo Le runs: {duo_le_runs}, Successful: {duo_le_success}")
    print(f"Bao Wang runs: {bao_wang_runs}, Successful: {bao_wang_success}")

def save_summary_to_json():
    """
    将汇总信息保存到本地 JSON 文件
    """
    summary_data = {
        "date": today,
        "total_runs": total_runs,
        "successful_runs": successful_runs,
        "duo_le_runs": duo_le_runs,
        "duo_le_success": duo_le_success,
        "bao_wang_runs": bao_wang_runs,
        "bao_wang_success": bao_wang_success
    }
    summary_file = os.path.join(os.path.dirname(__file__), "summary.json")
    with open(summary_file, "w") as f:
        json.dump(summary_data, f, indent=4)
    print(f"Summary saved to {summary_file}")

def job():
    """
    定时任务：依次运行 duo_le_ios.py 和 bao_wang_ios.py
    """
    run_script("duo_le_ios.py")
    run_script("bao_wang_ios.py")
    print_summary()
    save_summary_to_json()

if __name__ == "__main__":
    # 设置定时任务，每5分钟运行一次
    while True:
        job()
        time.sleep(120)  # 等待5分钟