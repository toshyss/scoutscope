import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

class putMoji:
    def __init__(self):
        pass

    @classmethod
    def putText(cls, cv_image, text, point, font_path, font_size, color=(0,0,0)):
        font = ImageFont.truetype(font_path, font_size)

        cv_rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_rgb_image)

        draw = ImageDraw.Draw(pil_image)
        draw.text(point, text, fill=color, font=font)

        cv_rgb_result_image = np.asarray(pil_image)
        cv_bgr_result_image = cv2.cvtColor(cv_rgb_result_image, cv2.COLOR_RGB2BGR)

        return cv_bgr_result_image


if __name__ == '__main__':
    cv_image = cv2.imread("./images/sample.png")

    # font_path = '/System/Library/Fonts/Courier.dfont'
    font_path = '/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc'

    image = putMoji.putText(cv_image, u"今日も頑張ります。", (30, 30), font_path, 60, (0,0,0))

    cv2.imshow("sample", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
