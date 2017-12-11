# 识别图片，返回预测结果
import json
import numpy as np

from app.controller.ImageToDigital import recognize
from app.controller.tools import ConvertELogStrToValue


def predictionImage(picturePath):
    print("start prediction...")
    try:
        result = recognize(picturePath)
        print(result)
        temp = [10]
        i = 0
        length = len(str(result[9]))
        for item in result:
            float_data = np.float16(item)
            if (float_data) < 0.0001:
                temp[i] = 0
            else:
                temp[i] = '{:.5f}'.format(np.float16(item))
            ++i
        print (temp)
        prediction = json.dumps(temp, ensure_ascii=False, encoding='UTF-8')

        return prediction
    except Exception as ex:
        print(ex)
        return ex
