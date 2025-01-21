from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

@app.route('/api/ip.jpg')
def generate_image():
    # 获取客户端IP
    client_ip = request.remote_addr

    # 创建一个白色背景的图片
    img = Image.new('RGB', (280, 80), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # 设置字体和大小
    font = ImageFont.truetype("fonts/simsun.ttc", 48)
    
    # 在图片上绘制IP地址
    d.text((10, 10), client_ip, font=font, fill=(0,0,0))

    # 将图片保存到内存中
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    # 返回图片
    return send_file(io.BytesIO(img_byte_arr), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)


# http://localhost:5000/api/ip.jpg
