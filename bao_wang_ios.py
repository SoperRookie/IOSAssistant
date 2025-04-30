# -*- encoding=utf8 -*-
__author__ = "makino"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from common.screen_recorder import ScreenRecorder
import os
import shutil
import stat
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["ios:///http://127.0.0.1:8100",])


# script content
print("开始进行包网ios不掉签巡检任务")

def ios_download():
    try:
        # 每个步骤都放在 try 块中，捕获异常
        touch(Template(r"images/bao_wang/tpl1745754858493.png", record_pos=(-0.118, 0.924), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745754874131.png", record_pos=(-0.029, 0.803), resolution=(1170, 2532)))
        text("https://download.bet4999.com")
        swipe(Template(r"images/bao_wang/tpl1745754955714.png", record_pos=(-0.001, 0.7), resolution=(1170, 2532)), vector=[0.0478, -0.3537])
        touch(Template(r"images/bao_wang/tpl1745754977724.png", record_pos=(-0.018, -0.797), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745754991771.png", record_pos=(0.344, -0.024), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755014727.png", record_pos=(-0.005, 0.14), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755028082.png", record_pos=(0.349, -0.026), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755046930.png", record_pos=(-0.005, -0.656), resolution=(1170, 2532)))
        wait(Template(r"images/bao_wang/tpl1745755066804.png", record_pos=(-0.006, -0.788), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755077572.png", record_pos=(-0.02, -0.735), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755104258.png", record_pos=(0.168, 0.115), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755115764.png", record_pos=(0.42, 0.948), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755131126.png", record_pos=(0.256, -0.91), resolution=(1170, 2532)))
        keyevent("HOME")
    except Exception as e:
        # 如果有任何一步失败，打印错误信息并抛出异常
        print(f"ios_download failed at step: {e}")
        raise

def ios_h5_install():
    try:
        touch(Template(r"images/bao_wang/tpl1745755197183.png", record_pos=(0.349, 0.921), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755211085.png", record_pos=(-0.193, -0.216), resolution=(1170, 2532)))
        wait(Template(r"images/bao_wang/tpl1745755224512.png", record_pos=(0.01, 0.291), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755238161.png", record_pos=(0.398, -0.867), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755248971.png", record_pos=(0.009, 0.757), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755259900.png", record_pos=(0.4, -0.868), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755277718.png", record_pos=(-0.399, -0.915), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755289964.png", record_pos=(-0.392, -0.912), resolution=(1170, 2532)))
        keyevent("HOME")
    except Exception as e:
        # 如果有任何一步失败，打印错误信息并抛出异常
        print(f"ios_h5_install failed at step: {e}")
        raise

def ios_h5_login():
    try:
        touch(Template(r"images/bao_wang/tpl1745755338953.png", record_pos=(0.341, 0.197), resolution=(1170, 2532)))
        wait(Template(r"images/bao_wang/tpl1745755354736.png", record_pos=(-0.083, -0.903), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755368071.png", record_pos=(-0.029, -0.897), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755380466.png", record_pos=(-0.252, -0.074), resolution=(1170, 2532)))
        text("scusdt01")
        touch(Template(r"images/bao_wang/tpl1745755411343.png", record_pos=(-0.276, 0.101), resolution=(1170, 2532)))
        text("yin666666")
        touch(Template(r"images/bao_wang/tpl1745755472035.png", record_pos=(0.003, 0.39), resolution=(1170, 2532)))
        wait(Template(r"images/bao_wang/tpl1745755482915.png", record_pos=(0.007, -0.602), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755495874.png", record_pos=(0.388, -0.615), resolution=(1170, 2532)))
        keyevent("HOME")
    except  Exception as e:
        # 如果有任何一步失败，打印错误信息并抛出异常
        print(f"ios_h5_login failed at step: {e}")
        raise

def ios_h5_uninstall():
    try:
        touch(Template(r"images/bao_wang/tpl1745755567676.png", record_pos=(0.334, 0.921), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755579259.png", record_pos=(-0.101, 0.421), resolution=(1170, 2532)))
        swipe(Template(r"images/bao_wang/tpl1745755595322.png", record_pos=(-0.114, 0.827), resolution=(1170, 2532)), vector=[0.0989, -0.6049])
        touch(Template(r"images/bao_wang/tpl1745755613629.png", record_pos=(-0.138, 0.508), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755629777.png", record_pos=(-0.205, -0.299), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755637495.png", record_pos=(-0.031, 0.223), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755646883.png", record_pos=(0.011, 0.752), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755659658.png", record_pos=(-0.393, -0.905), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755672126.png", record_pos=(-0.385, -0.913), resolution=(1170, 2532)))
        keyevent("HOME")
    except Exception as e:
        # 如果有任何一步失败，打印错误信息并抛出异常
        print(f"ios_h5_uninstall failed at step: {e}")
        raise

def ios_app_login():
    sleep(5)
    try:
        wait(Template(r"images/bao_wang/tpl1745755730431.png", record_pos=(-0.357, 0.184), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745764209261.png", record_pos=(-0.357, 0.189), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755744953.png", record_pos=(0.164, 0.143), resolution=(1170, 2532)))
        wait(Template(r"images/bao_wang/tpl1745755758825.png", record_pos=(-0.079, -0.906), resolution=(1170, 2532)))
        touch(Template(r"images/bao_wang/tpl1745755766218.png", record_pos=(-0.017, -0.913), resolution=(1170, 2532)))
        sleep(1)
        touch(Template(r"images/bao_wang/tpl1745755783870.png", record_pos=(0.171, 0.144), resolution=(1170, 2532)))
        if exists(Template(r"images/bao_wang/tpl1745755815548.png", record_pos=(-0.245, -0.059), resolution=(1170, 2532))):
            touch(Template(r"images/bao_wang/tpl1745755845052.png", record_pos=(-0.005, 0.394), resolution=(1170, 2532)))
            keyevent("HOME")
        else:
            touch(Template(r"images/bao_wang/tpl1745755892316.png", record_pos=(-0.274, -0.083), resolution=(1170, 2532)))
            text("scusdt01")
            text("yin666666")
            touch(Template(r"images/bao_wang/tpl1745755984990.png", record_pos=(-0.002, 0.383), resolution=(1170, 2532)))
            exists(Template(r"images/bao_wang/tpl1745756005917.png", record_pos=(0.004, -0.683), resolution=(1170, 2532)))
            touch(Template(r"images/bao_wang/tpl1745756028561.png", record_pos=(0.391, -0.674), resolution=(1170, 2532)))
            keyevent("HOME")
    except Exception as e:
        # 如果有任何一步失败，打印错误信息并抛出异常
        print(f"ios_app_login failed at step: {e}")
        raise

def cleanup_directories():
    """
    Clean up log and recordings directories after script completion
    """
    try:
        # 修正路径构造逻辑，直接使用当前脚本所在目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 定义需要清理的目录（调整到正确路径）
        log_dir = os.path.join(script_dir, "log")
        recordings_dir = os.path.join(script_dir, "recordings")
        
        # 新增调试信息
        print(f"Attempting to remove log directory: {log_dir}")
        print(f"Attempting to remove recordings directory: {recordings_dir}")

        # 增加权限处理逻辑
        def remove_readonly(func, path, _):
            os.chmod(path, stat.S_IWRITE)
            func(path)

        if os.path.exists(log_dir):
            shutil.rmtree(log_dir, onerror=remove_readonly)
            print(f"Successfully removed log directory: {log_dir}")
            if os.path.exists(log_dir):
                print(f"WARNING: Log directory still exists: {log_dir}")
        
        if os.path.exists(recordings_dir):
            shutil.rmtree(recordings_dir, onerror=remove_readonly)
            print(f"Successfully removed recordings directory: {recordings_dir}")
            if os.path.exists(recordings_dir):
                print(f"WARNING: Recordings directory still exists: {recordings_dir}")
                
    except Exception as e:
        print(f"Error during cleanup: {str(e)}")
        import traceback
        traceback.print_exc()

def main():
    recorder = ScreenRecorder("baowang")  # 创建录屏对象，指定 app_type 为 "baowang"
    recorder.start_recording()  # 启动录屏

    uninstall_success = False  # 新增变量，用于标记 ios_h5_uninstall 是否成功执行
    try:
        # 修改: 在执行每个方法前打印日志，便于排查问题
        print("Starting ios_download...")
        ios_download()
        print("Starting ios_h5_install...")
        ios_h5_install()
        print("Starting ios_h5_login...")
        ios_h5_login()
        print("Starting ios_h5_uninstall...")
        ios_h5_uninstall()
        uninstall_success = True  # 标记卸载成功
        print("Starting ios_app_login...")
        ios_app_login()
        print("All tasks completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        keyevent("HOME")
        if not uninstall_success:  # 如果卸载未成功，则执行卸载操作
            print("Attempting to uninstall H5 app due to failure...")
            ios_h5_uninstall()
    finally:
        recorder.stop_recording()  # 停止录屏

    try:
        # 修改: 移除 logpath 参数，确保报告只包含当前运行的 Python 文件
        from airtest.report.report import LogToHtml
        import os
        from datetime import datetime

        # 修改: 生成包含时间戳的报告目录，确保每次运行时目录唯一
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dir = os.path.join(os.path.dirname(__file__), f"reports/bao_wang/{timestamp}")
        os.makedirs(report_dir, exist_ok=True)

        html_reports = LogToHtml(__file__,
                       export_dir=report_dir,
                       lang="zh"
                       )
        html_reports.report(output_file="report.html")  # 确保文件扩展名为 .html
        print(f"HTML report generated successfully at {os.path.join(report_dir, 'report.html')}")
    except Exception as e:
        print(f"Failed to generate HTML report: {e}")
    finally:
        print("开始删除log目录")
        cleanup_directories()

if __name__ == "__main__":
    main()
