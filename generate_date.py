import os
import random
import unittest

last_name = ('김', '이', '박', '최', '정', '강', '조', '윤', '장', '임' '한', '오' '신', '서', '권', '황', '안', '송', '전', '백',
'허', '고', '문', '김', '남', '심', '류', '김', '원', '문', '주', '석', '손', '민', '유' '조', '남', '노' '백', '봉',
'정', '곽', '채', '홍', '신', '강', '노' '연', '공', '문'
)
first_name = []

#directory = ".\phone_num\\"
file_name = "korean_top_name.txt"

file_path = os.path.join(file_name)

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        name = line.strip()
        first_name.append(name)

def generate_name():
    full_name = "{}{}".format(random.choice(last_name), random.choice(first_name))
    return full_name

def generate_phone_number():
    if random.choice([True,False]):
        phone_number = '10'
        for _ in range(8):
            phone_number += str(random.randint(0,9))
    else:
        phone_number = '11'
        for _ in range(7):
            phone_number += str(random.randint(0,9))

    return phone_number

class TestGeneratePhoneNumber(unittest.TestCase):
    def test_generate_phone_number(self):
        for _ in range(100):
            phone_number = generate_phone_number()
            self.assertTrue(len(phone_number)) in [9,10]
            self.assertTrue(phone_number.startswith('10') or phone_number.startswith('11'))

if __name__ == "main":
    print(generate_name())

    print(generate_phone_number())

    unittest.main()