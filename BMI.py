'''
classBMI:
属性:
    -身長
    -体重
    -BMI

ルール:BMI範囲
    -10<=BMI<=40
    -表示するときは、小数点第2位まで
        -ex:23.678 => 23.67
できること:
    -???
'''


# クラス名はUpperCamelCaseが一般的
# ex -SpartaCampDay2
class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height ** 2)
        if not (10 <= self.value <= 40):
            raise ValueError('BMI が正常値範囲を超えています')

    def __str__(self):
        return f'{self.value:.2f}'




# BMIのクラスのインスタンス化
hibiki_bmi = BMI(height=1.80, weight=67.0)
print(hibiki_bmi)


wataru_bmi = BMI(height=1.68, weight=62.1)
print(wataru_bmi)
