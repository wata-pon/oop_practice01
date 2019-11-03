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
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)


# BMIのクラスのインスタンス化
hibiki_bmi = BMI(height=1.80, weight=67.0)
wataru_bmi = BMI(height=1.68, weight=62.1)

print(hibiki_bmi.height, hibiki_bmi.weight)
print(hibiki_bmi.calculate_bmi())
