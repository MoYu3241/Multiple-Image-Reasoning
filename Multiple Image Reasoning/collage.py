import openai
import base64
import time
import requests

def encode_image(image_path):
    """将本地图片转换为Base64编码"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 准备图片
image1_path = "./resource/3/a (5).jpeg"  # 本地图片1

# 转换为Base64编码
base64_image1 = encode_image(image1_path)

def query_gpt4(question):
    openai.api_key = "sk-vb0cABDvuMoCWvtfB000F1DdA8734861806467713aA4697d"
    openai.base_url = 'https://api.shubiaobiao.cn/v1/'

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                #  {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": [
                # 文本提示
                {"type": "text", "text": question},
                # 第一张图片（本地图片的Base64编码）
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image1}"}},
                # 第二张图片（网络图片的Base64编码）
                #  {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image2}"}}
                # 可继续添加更多图片...
            ]}
            ]
        )

        print(response)
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

# 问题
question = "Act as an image classifier by providing predictions for each 3x3 grid collage, following left-to-right, top-to-bottom order."

# 记录本地发送请求的时间（用于参考）
local_send_time = time.time()
# 获取打印并回答
answer = query_gpt4(question)
# 记录本地接收响应的时间
local_receive_time = time.time()
total_inference_time = round(local_receive_time - local_send_time, 10)
print(answer)
print(f"总耗时：{total_inference_time}秒")
