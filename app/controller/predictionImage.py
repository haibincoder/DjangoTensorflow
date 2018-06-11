# 识别图片，返回预测结果
import json
import numpy as np

from app.controller.ImageToDigital import recognize
from app.controller.tools import ConvertELogStrToValue


def predictionImage(picturePath):
    print("start prediction...")
    try:
        result = recognize(picturePath)
        print("predict result:", result)
        temp = [None]*10
        i = 0
        for item in result:
            result_num=float(item)
            temp[i]=round(result_num,3)*100
            i = i + 1
        prediction = json.dumps(temp)
        print(prediction)
        return prediction
    except Exception as ex:
        print(ex)
        return ex