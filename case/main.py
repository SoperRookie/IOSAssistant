#!/usr/bin/env python
# -*- encoding=utf8 -*-
"""
主程序入口
支持自定义分钟间隔执行任务
使用方法：
python main.py  # 默认立即执行一次
python main.py 30  # 每30分钟执行一次
"""

import os
import sys
import time
import logging
import subprocess
import shutil
from datetime import datetime
from pathlib import Path
import schedule
import argparse

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from common.robot_message import RobotMessage

# 初始化机器人消息
robot = RobotMessage()

def run_script(script_path, app_type, report_base_dir):
    """运行脚本并录制屏幕
    
    Args:
        script_path: 脚本路径
        app_type: 应用类型，'duo_le'或'bao_wang'
        report_base_dir: 报告基础目录路径
    """
    try:
        # 创建报告目录
        report_dir = os.path.join(report_base_dir, app_type)
        os.makedirs(report_dir, exist_ok=True)
        
        # 设置日志文件
        log_file = os.path.join(report_dir, f"{app_type}_ios.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)
        
        # 运行脚本并录制屏幕
        cmd = [
            sys.executable,
            os.path.join(project_root, "common", "screen_recorder.py"),
            app_type,
            script_path,
            report_dir
        ]
        
        logger.info(f"执行命令: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=False)
        
        if result.returncode != 0:
            logger.error(f"脚本执行失败，返回代码: {result.returncode}")
            return False
        
        logger.info("脚本执行成功")
        return True
    except Exception as e:
        logger.error(f"执行脚本时发生错误: {e}")
        return False
    finally:
        # 移除文件处理器
        logger.removeHandler(file_handler)

def scheduled_task():
    """定时执行的任务"""
    # 生成一个统一的时间戳目录
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_base_dir = os.path.join("reports", timestamp)
    
    # 运行多乐脚本
    logger.info("开始运行多乐脚本...")
    duo_le_script = os.path.join(project_root, "duo_le_ios.py")
    duo_le_success = run_script(duo_le_script, "duo_le", report_base_dir)
    
    # 等待一段时间
    time.sleep(5)
    
    # 运行包网脚本
    logger.info("开始运行包网脚本...")
    bao_wang_script = os.path.join(project_root, "bao_wang_ios.py")
    bao_wang_success = run_script(bao_wang_script, "bao_wang", report_base_dir)
    
    # 检查结果
    if not duo_le_success or not bao_wang_success:
        logger.error("部分脚本执行失败")
        return False
    
    logger.info("所有脚本执行完成")
    return True

def main():
    """主函数"""
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='执行自动化测试脚本')
    parser.add_argument('interval', nargs='?', type=int, default=0,
                      help='执行间隔（分钟）。默认为0，表示只执行一次')
    args = parser.parse_args()
    
    # 立即执行一次
    logger.info("开始首次执行...")
    scheduled_task()
    
    # 如果设置了间隔时间，则设置定时任务
    if args.interval > 0:
        logger.info(f"设置定时任务，每{args.interval}分钟执行一次")
        schedule.every(args.interval).minutes.do(scheduled_task)
        
        # 持续运行，等待定时任务
        while True:
            schedule.run_pending()
            time.sleep(60)  # 每分钟检查一次是否有待执行的任务
    else:
        logger.info("未设置定时间隔，程序执行完毕")

if __name__ == "__main__":
    main()