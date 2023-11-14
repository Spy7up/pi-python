import qrcode
from PIL import Image


def getQRcode(data, file_name):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    # 添加数据
    qr.add_data(data)
    # 填充数据
    qr.make(fit=True)
    # 生成图片
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    img = Image.open("myQrCode.png").convert('RGBA')

    # 添加logo，打开logo照片
    icon = Image.open("logo.jpg")
    icon = icon.convert('RGBA')
    # 获取图片的宽高
    img_w, img_h = img.size
    # 参数设置logo的大小
    factor = 5.5
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    # 得到画图的x，y坐标，居中显示
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    # 黏贴logo照
    img.paste(icon, (w, h), mask=None)
    # 保存img
    img.save(file_name)
    return img


if __name__ == '__main__':
    getQRcode("https://h5iov.venucia.com/common/msg/msginfo.html?id=77989&appCode=nissan&projectType=nissan&jumpData=mweZ&type=1&jumpType=2&version=3.0.0", 'myQrCode.png')
