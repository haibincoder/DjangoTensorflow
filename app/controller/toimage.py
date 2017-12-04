import base64

from PIL import Image


def base64toimg(strg):
    # base64
    missing_padding = 4 - len(strg) % 4
    if missing_padding:
        strg += '==' * missing_padding
        print('missing_padding:', missing_padding)

    result = base64.decodestring(strg.encode())
    print("end decode")
    print("start save image:")

    # 保存图片
    path = "app/images/djangotest.png"
    fs = open( path, "wb")
    fs.write(result)
    fs.close()
    print("save successful.")

    # 压缩图片
    im = Image.open(path)
    im = im.resize((28, 28), Image.ANTIALIAS)
    newPath = "app/images/djangotest_new.png"
    im.save(newPath, quality=30)

