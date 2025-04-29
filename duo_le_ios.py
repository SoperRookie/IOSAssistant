__author__ = "MaKino"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from common.screen_recorder import ScreenRecorder
import os
from datetime import datetime

if not cli_setup():
    # 修改: 生成包含时间戳的报告目录，确保每次运行时目录唯一
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = os.path.join(os.path.dirname(__file__), f"reports/duo_le/{timestamp}")
    os.makedirs(report_dir, exist_ok=True)
    # 修改: 设置logdir为False，避免在duo_le_ios.log中生成reports目录
    auto_setup(__file__, logdir=True, devices=["ios:///http://127.0.0.1:8100"])


# script content
print("开始进行多乐ios不掉签巡检任务")
def ios_download():
    """
    主要负责多乐ios不掉签h5证书下载和app下载巡检
    :return:
    """
    touch(Template(r"images/duo_le/tpl1745687473066.png", record_pos=(-0.119, 0.924), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687496768.png", record_pos=(0.002, 0.816), resolution=(1170, 2532)))
    text("https://duole.bet")
    wait(Template(r"images/duo_le/tpl1745687561990.png", record_pos=(-0.009, 0.111), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687573047.png", record_pos=(-0.004, 0.107), resolution=(1170, 2532)))
    wait(Template(r"images/duo_le/tpl1745687590156.png", record_pos=(0.352, -0.026), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687599502.png", record_pos=(0.35, -0.031), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687617496.png", record_pos=(-0.011, 0.138), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687627531.png", record_pos=(0.35, -0.028), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687643891.png", record_pos=(-0.009, -0.036), resolution=(1170, 2532)))
    wait(Template(r"images/duo_le/tpl1745687663864.png", record_pos=(0.009, -0.785), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687692805.png", record_pos=(-0.018, -0.732), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687709519.png", record_pos=(0.184, 0.119), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687727729.png", record_pos=(0.403, 0.945), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745687740922.png", record_pos=(0.282, -0.921), resolution=(1170, 2532)))
    keyevent("HOME")

def ios_h5_install():
    """
    主要负责多乐ios不掉签h5的安装巡检
    :return:
    """
    touch(Template(r"images/duo_le/tpl1745687971883.png", record_pos=(0.339, 0.921), resolution=(1170, 2532)))
    wait(Template(r"images/duo_le/tpl1745687985575.png", record_pos=(0.003, -0.228), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745688003945.png", record_pos=(-0.002, -0.228), resolution=(1170, 2532)))
    wait(Template(r"images/duo_le/tpl1745688021549.png", record_pos=(-0.004, -0.071), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745688030380.png", record_pos=(0.401, -0.862), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745688057747.png", record_pos=(0.004, 0.753), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745688072674.png", record_pos=(0.392, -0.867), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745688093277.png", record_pos=(-0.403, -0.912), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745688113609.png", record_pos=(-0.397, -0.915), resolution=(1170, 2532)))
    keyevent("HOME")

def ios_h5_login():
    """
    主要负责多乐ios不掉签h5的登陆巡检
    :return:
    """
    wait(Template(r"images/duo_le/tpl1745689301177.png", record_pos=(0.35, 0.197), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745689425477.png", record_pos=(0.345, 0.188), resolution=(1170, 2532)))
    wait(Template(r"images/duo_le/tpl1745689453017.png", record_pos=(-0.258, 0.202), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745689484939.png", record_pos=(-0.065, -0.256), resolution=(1170, 2532)))
    text("taroko19")
    touch(Template(r"images/duo_le/tpl1745689549974.png", record_pos=(-0.077, -0.073), resolution=(1170, 2532)))
    text("yin666666")
    touch(Template(r"images/duo_le/tpl1745689593900.png", record_pos=(0.195, 0.217), resolution=(1170, 2532)))
    assert_exists(Template(r"images/duo_le/tpl1745689740505.png", record_pos=(0.002, 0.009), resolution=(1170, 2532)), "Please fill in the test point.")
    keyevent("HOME")

def ios_h5_uninstall():
    """
    主要负责多乐ios不掉签h5的卸载巡检
    :return:
    """
    touch(Template(r"images/duo_le/tpl1745690019159.png", record_pos=(0.335, 0.921), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690055768.png", record_pos=(-0.005, 0.432), resolution=(1170, 2532)))
    swipe(Template(r"images/duo_le/tpl1745690074532.png", record_pos=(-0.014, 0.826), resolution=(1170, 2532)), vector=[0.0073, -0.7316])
    touch(Template(r"images/duo_le/tpl1745690101204.png", record_pos=(-0.185, 0.558), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690122417.png", record_pos=(-0.009, -0.286), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690150104.png", record_pos=(-0.013, -0.127), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690163514.png", record_pos=(-0.014, 0.751), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690181219.png", record_pos=(-0.395, -0.909), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690198661.png", record_pos=(-0.394, -0.903), resolution=(1170, 2532)))
    keyevent("HOME")

def ios_app_login():
    """
    主要负责多乐ios的不掉签app登陆巡检
    :return:
    """
    wait(Template(r"images/duo_le/tpl1745690406879.png", record_pos=(-0.126, 0.192), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690422653.png", record_pos=(-0.122, 0.197), resolution=(1170, 2532)))
    wait(Template(r"images/duo_le/tpl1745690440323.png", record_pos=(0.166, 0.146), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690454508.png", record_pos=(0.177, 0.144), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690473638.png", record_pos=(0.177, 0.142), resolution=(1170, 2532)))
    wait(Template(r"images/duo_le/tpl1745690494955.png", record_pos=(-0.256, 0.15), resolution=(1170, 2532)))
    touch(Template(r"images/duo_le/tpl1745690517721.png", record_pos=(0.184, 0.149), resolution=(1170, 2532)))
    assert_exists(Template(r"images/duo_le/tpl1745690538988.png", record_pos=(0.002, -0.105), resolution=(1170, 2532)), "Please fill in the test point.")
    keyevent("HOME")

def main():
    recorder = ScreenRecorder("duole")  # 创建录屏对象，指定 app_type 为 "duole"
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
        timestamp1 = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_dirs = os.path.join(os.path.dirname(__file__), f"reports/duo_le/{timestamp1}")
        os.makedirs(report_dirs, exist_ok=True)

        html_reports = LogToHtml(__file__,
                       export_dir=report_dir,
                       lang="zh"
                       )
        html_reports.report(output_file="report.html")  # 确保文件扩展名为 .html
        print(f"HTML report generated successfully at {os.path.join(report_dirs, 'report.html')}")
    except Exception as e:
        print(f"Failed to generate HTML report: {e}")

if __name__ == "__main__":
    main()
