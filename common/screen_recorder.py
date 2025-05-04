#!/usr/bin/env python
# -*- encoding=utf8 -*-
"""
屏幕录制模块
使用ffmpeg实时录制屏幕，并在视频中央添加日期时间水印
"""

import os
import sys
import time
import signal
import logging
import subprocess
import shlex
import tempfile
import uuid
import shutil
from datetime import datetime
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,  # 提高日志级别以便调试
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('../../screen_recorder.log')
    ]
)
logger = logging.getLogger(__name__)

class ScreenRecorder:
    """屏幕录制器类"""
    
    def __init__(self, app_type, report_dir):
        """初始化录屏器
        
        Args:
            app_type: 应用类型，'duo_le'或'bao_wang'
            report_dir: 报告目录路径
        """
        # 统一目录名称
        if app_type == "duole":
            app_type = "duo_le"
        elif app_type == "baowang":
            app_type = "bao_wang"
            
        self.app_type = app_type
        self.report_dir = report_dir
        self.process = None
        self.screenshot_process = None
        self.output_file = None
        self.start_time = None
        self.temp_dir = os.path.join(tempfile.gettempdir(), f"screen_recorder_{uuid.uuid4().hex}")
        os.makedirs(self.temp_dir, exist_ok=True)
        self.screenshots_dir = os.path.join(self.temp_dir, "screenshots")
        os.makedirs(self.screenshots_dir, exist_ok=True)
        self.font_file = self._prepare_font()
        
    def _prepare_font(self):
        """准备字体文件
        
        Returns:
            字体文件路径
        """
        # 优先使用系统自带的字体
        font_paths = [
            # macOS字体
            "/System/Library/Fonts/PingFang.ttc",  # 苹方字体，支持中文
            "/System/Library/Fonts/Helvetica.ttc",
            "/Library/Fonts/Arial.ttf",
            # 项目本地字体（可以添加到项目中）
            "fonts/Arial.ttf"
        ]
        
        for path in font_paths:
            if os.path.exists(path):
                return path
        
        # 如果找不到任何字体，使用一个临时字体
        logger.warning("找不到可用的字体文件，将使用临时字体")
        return None
    
    def _check_tools(self):
        """检查必要的工具是否可用"""
        # 检查ffmpeg
        try:
            result = subprocess.run(
                ["ffmpeg", "-version"], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                check=False
            )
            if result.returncode != 0:
                logger.error("ffmpeg 命令运行失败")
                return False
            
            # 在macOS上检查screencapture
            if sys.platform == 'darwin':
                result = subprocess.run(
                    ["which", "screencapture"], 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE,
                    check=False
                )
                if result.returncode != 0:
                    logger.error("screencapture 命令不可用")
                    return False
            
            logger.debug("所有必要工具都可用")
            return True
        except Exception as e:
            logger.error(f"检查工具时出错: {e}")
            return False
    
    def _start_screenshot_capture(self):
        """启动截图捕获进程，用于在macOS上录制屏幕"""
        # 创建截图脚本
        script_path = os.path.join(self.temp_dir, "capture_script.sh")
        
        # 编写截图脚本内容
        script_content = f"""#!/bin/bash
# 截图脚本
counter=0
while true; do
    # 使用screencapture捕获整个屏幕
    screencapture -x -t jpg -o "{self.screenshots_dir}/screen_$(printf '%06d' $counter).jpg"
    counter=$((counter+1))
    # 等待一小段时间（控制帧率，可以调整）
    sleep 0.1
done
"""
        # 写入脚本文件
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        # 添加执行权限
        os.chmod(script_path, 0o755)
        
        # 启动脚本
        logger.info(f"启动截图捕获脚本: {script_path}")
        self.screenshot_process = subprocess.Popen(
            ["/bin/bash", script_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # 等待一段时间，确保有一些截图生成
        time.sleep(2)
        
        # 检查是否有截图生成
        screenshots = os.listdir(self.screenshots_dir)
        if not screenshots:
            logger.error("没有生成任何截图，截图捕获可能失败")
            return False
        
        logger.info(f"成功启动截图捕获，已生成 {len(screenshots)} 张初始截图")
        return True
    
    def start_recording(self):
        """开始录制屏幕"""
        if not self._check_tools():
            logger.error("必要的工具不可用，无法进行录制")
            return False
            
        if self.process and self.process.poll() is None:
            logger.warning("录制已经在进行中")
            return False
        
        self.start_time = datetime.now()
        timestamp = self.start_time.strftime("%Y%m%d_%H%M%S")
        
        # 创建输出文件路径
        output_dir = os.path.join(self.report_dir, "recordings")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        self.output_file = os.path.join(output_dir, f"{self.app_type}_{timestamp}.mp4")
        
        try:
            # 在macOS上，我们使用screencapture来捕获屏幕快照
            if sys.platform == 'darwin':
                # 启动截图捕获进程
                if not self._start_screenshot_capture():
                    logger.error("无法启动屏幕截图捕获")
                    return False
                
                # 截图捕获已经启动，等待足够的截图生成
                logger.info("屏幕截图捕获已启动，录制准备就绪")
                return True
            else:
                # 在其他平台上，直接使用ffmpeg进行录制
                # 创建包含日期时间的水印
                watermark_filter = f"drawtext=fontfile='{self.font_file}':text='%{{localtime}}':fontcolor=white:fontsize=36:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2"
                
                # 使用ffmpeg录制屏幕
                cmd = [
                    "ffmpeg",
                    "-hide_banner",
                    "-f", "avfoundation",
                    "-framerate", "30",
                    "-i", "1:0",
                    "-vf", watermark_filter,
                    "-c:v", "libx264",
                    "-preset", "ultrafast",
                    "-crf", "28",
                    "-y",
                    self.output_file
                ]
                
                logger.info(f"启动ffmpeg录制: {' '.join(cmd)}")
                self.process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                
                # 等待一段时间，确保录制已经开始
                time.sleep(2)
                
                if self.process.poll() is not None:
                    logger.error("ffmpeg进程已退出，录制可能失败")
                    return False
                
                logger.info("屏幕录制已启动")
                return True
        except Exception as e:
            logger.error(f"启动录制时发生错误: {e}")
            return False
    
    def _create_video_from_screenshots(self):
        """从截图创建视频"""
        try:
            # 获取所有截图文件
            screenshots = sorted([f for f in os.listdir(self.screenshots_dir) if f.endswith('.jpg')])
            if not screenshots:
                logger.error("没有找到任何截图文件")
                return False
            
            # 创建输入文件列表
            input_file = os.path.join(self.temp_dir, "input.txt")
            with open(input_file, 'w') as f:
                for screenshot in screenshots:
                    f.write(f"file '{os.path.join(self.screenshots_dir, screenshot)}'\n")
                    f.write(f"duration 0.1\n")  # 每张图片显示0.1秒
            
            # 使用ffmpeg从截图创建视频
            cmd = [
                "ffmpeg",
                "-hide_banner",
                "-f", "concat",
                "-safe", "0",
                "-i", input_file,
                "-vf", f"drawtext=fontfile='{self.font_file}':text='%{{localtime}}':fontcolor=white:fontsize=36:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2",
                "-c:v", "libx264",
                "-preset", "ultrafast",
                "-crf", "28",
                "-y",
                self.output_file
            ]
            
            logger.info(f"从截图创建视频: {' '.join(cmd)}")
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
            
            # 检查输出文件
            if os.path.exists(self.output_file) and os.path.getsize(self.output_file) > 0:
                logger.info(f"成功创建视频: {self.output_file}")
                return True
            else:
                logger.error(f"视频文件不存在或为空: {self.output_file}")
                return False
        except Exception as e:
            logger.error(f"创建视频时发生错误: {e}")
            return False
    
    def _cleanup(self):
        """清理临时文件和进程"""
        # 停止截图进程
        if self.screenshot_process and self.screenshot_process.poll() is None:
            try:
                logger.info("停止截图进程")
                self.screenshot_process.terminate()
                try:
                    self.screenshot_process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    logger.warning("截图进程未响应，强制终止")
                    self.screenshot_process.kill()
                    self.screenshot_process.wait()
            except Exception as e:
                logger.error(f"停止截图进程时出错: {e}")
        
        # 停止ffmpeg进程
        if self.process and self.process.poll() is None:
            try:
                logger.info("停止ffmpeg进程")
                if sys.platform == 'darwin':
                    os.system(f"kill -INT {self.process.pid}")
                else:
                    self.process.send_signal(signal.SIGINT)
                
                try:
                    self.process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    logger.warning("ffmpeg进程未响应，强制终止")
                    self.process.kill()
                    self.process.wait()
            except Exception as e:
                logger.error(f"停止ffmpeg进程时出错: {e}")
        
        # 不要立即删除临时目录，因为我们可能还需要用它来创建视频
    
    def stop_recording(self):
        """停止录制并保存视频"""
        try:
            # 停止所有进程
            self._cleanup()
            
            # 如果在macOS上使用截图方式录制，需要将截图合成为视频
            if sys.platform == 'darwin' and self.screenshot_process:
                logger.info("从截图创建视频...")
                success = self._create_video_from_screenshots()
                if success:
                    duration = datetime.now() - self.start_time if self.start_time else datetime.timedelta(0)
                    logger.info(f"录制完成，时长: {duration.total_seconds():.1f}秒，文件: {self.output_file}")
                    return True
                else:
                    logger.error("从截图创建视频失败")
                    return False
            else:
                # 如果直接使用ffmpeg录制，检查输出文件是否存在
                if os.path.exists(self.output_file) and os.path.getsize(self.output_file) > 0:
                    duration = datetime.now() - self.start_time if self.start_time else datetime.timedelta(0)
                    logger.info(f"录制完成，时长: {duration.total_seconds():.1f}秒，文件: {self.output_file}")
                    return True
                else:
                    logger.error(f"录制保存失败，输出文件不存在或为空: {self.output_file}")
                    return False
        except Exception as e:
            logger.error(f"停止录制时发生错误: {e}")
            return False
        finally:
            # 重置状态
            self.process = None
            self.screenshot_process = None
            self.start_time = None

def record_script(app_type, script_path, report_dir):
    """录制脚本执行过程
    
    Args:
        app_type: 应用类型，'duole'或'baowang'
        script_path: 要执行的脚本路径
        report_dir: 报告目录路径
    """
    recorder = ScreenRecorder(app_type, report_dir)
    
    try:
        # 开始录制
        if not recorder.start_recording():
            logger.error("无法启动录制")
            return False
        
        # 执行脚本
        try:
            result = subprocess.run(
                ["python", script_path],
                check=True
            )
            script_success = result.returncode == 0
        except subprocess.CalledProcessError as e:
            logger.error(f"脚本执行失败: {e}")
            script_success = False
        
        # 停止录制
        if not recorder.stop_recording():
            logger.error("录制保存失败")
            return False
        
        return script_success
    except Exception as e:
        logger.error(f"录制过程中发生错误: {e}")
        return False
    finally:
        # 清理临时文件
        if hasattr(recorder, 'temp_dir') and os.path.exists(recorder.temp_dir):
            try:
                shutil.rmtree(recorder.temp_dir)
            except Exception as e:
                logger.error(f"清理临时文件时出错: {e}")

def main():
    """主函数"""
    if len(sys.argv) != 4:
        print("Usage: python screen_recorder.py <app_type> <script_path> <report_dir>")
        sys.exit(1)
    
    app_type = sys.argv[1]
    script_path = sys.argv[2]
    report_dir = sys.argv[3]
    
    success = record_script(app_type, script_path, report_dir)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 