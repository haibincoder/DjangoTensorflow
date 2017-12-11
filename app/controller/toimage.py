import base64
import uuid

from PIL import Image


def base64toimg(strg, tag):
    try:
        # base64
        print("start decode:")
        missing_padding = 4 - len(strg) % 4
        if missing_padding:
            strg += '==' * missing_padding
            print('missing_padding:', missing_padding)

        result = base64.decodestring(strg.encode())
        print("end decode")
        print("start save image:")

        # 保存图片
        train_image_path="app/training-images/" + tag + "/"
        test_image_path="app/test-images/" + tag + "/"

        filename = str(uuid.uuid1()) + ".png"

        print (train_image_path + filename)

        path = "app/images/" + filename
        fs = open( path, "wb")
        fs.write(result)
        fs.close()

        print("save image successful")

        # 压缩图片
        im = Image.open(path)
        im = im.resize((28, 28), Image.ANTIALIAS)

        # Get the alpha band
        alpha = im.split()[-1]

        im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

        # Set all pixel values below 128 to 255,
        # and the rest to 0
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)

        # Paste the color of index 255 and use alpha as a mask
        im.paste(255, mask)


        im.save(train_image_path + filename, quality=50)
        im.save(test_image_path + filename, quality=50)

        print("save successful.")
        return "保存成功"
    except Exception as ex:
        print (ex)
        return ex


def checkimg(strg):
    try:
        # base64
        print("start decode:")
        missing_padding = 4 - len(strg) % 4
        if missing_padding:
            strg += '==' * missing_padding
            print('missing_padding:', missing_padding)

        result = base64.decodestring(strg.encode())
        print("end decode")
        print("start save image:")

        filename = str(uuid.uuid1()) + ".png"

        path = "app/images/" + filename
        fs = open( path, "wb")
        fs.write(result)
        fs.close()

        print("save image successful")

        # 压缩图片
        im = Image.open(path)
        im = im.resize((28, 28), Image.ANTIALIAS)

        # Get the alpha band
        alpha = im.split()[-1]

        im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

        # Set all pixel values below 128 to 255,
        # and the rest to 0
        mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)

        # Paste the color of index 255 and use alpha as a mask
        im.paste(255, mask)

        im.save(path, quality=50)

        print("save successful.")
        return path
    except Exception as ex:
        print (ex)
        return ex

