import requests
import json
from typing import Optional

class RobotMessage:
    def __init__(self, base_url: str = "https://trobot.ymtio.com/robot/1517306:b217dcb9a4dc4fea845d9e62e87b5fae/sendmessage_v2"):
        self.base_url = base_url

    def send_message(self, target_name: str, text: str, chat_type: str = "2", model: str = "1") -> dict:
        """
        发送消息到指定群组
        
        Args:
            target_name: 群ID
            text: 消息内容
            chat_type: 聊天类型，默认为"2"
            model: 模型类型，默认为"1"
            
        Returns:
            dict: API响应结果
        """
        headers = {
            'Content-Type': 'application/json'
        }
        
        payload = {
            "targetname": target_name,
            "text": text,
            "chatType": chat_type,
            "model": model
        }
        print(self.base_url)
        print(payload)
        
        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                data=json.dumps(payload)
            )
            return response.json()
        except Exception as e:
            return {
                "code": 500,
                "msg": f"请求失败: {str(e)}",
                "data": None
            }

# 使用示例
if __name__ == "__main__":
    robot = RobotMessage()
    result = robot.send_message(
        target_name="1002973958",
        text="这是一条测试消息"
    )
    print(result) 