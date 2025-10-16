import openai
import base64
import time

def encode_image(image_path):
    """将本地图片转换为Base64编码"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# 准备图片
image1_path = "./resource/3/1.jpeg"
image2_path = "./resource/3/2.jpeg"
image3_path = "./resource/3/3.jpeg"
image4_path = "./resource/3/4.jpeg"
image5_path = "./resource/3/5.jpeg"
image6_path = "./resource/3/6.jpeg"
image7_path = "./resource/3/7.jpeg"
image8_path = "./resource/3/8.jpeg"
image9_path = "./resource/3/9.jpeg"

# 转换为Base64编码
base64_image1 = encode_image(image1_path)
base64_image2 = encode_image(image2_path)
base64_image3 = encode_image(image3_path)
base64_image4 = encode_image(image4_path)
base64_image5 = encode_image(image5_path)
base64_image6 = encode_image(image6_path)
base64_image7 = encode_image(image7_path)
base64_image8 = encode_image(image8_path)
base64_image9 = encode_image(image9_path)


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
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image2}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image3}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image4}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image5}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image6}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image7}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image8}"}},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image9}"}}
            ]}
            ]
        )
        print(response)
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

# 问题
question = "Act as an image classifier by providing predictions for each image."

# 记录本地发送请求的时间（用于参考）
local_send_time = time.time()
# 获取打印并回答
answer = query_gpt4(question)
# 记录本地接收响应的时间
local_receive_time = time.time()
total_inference_time = round(local_receive_time - local_send_time, 10)
print(answer)
print(f"总耗时：{total_inference_time}秒")
