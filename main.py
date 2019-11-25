class Country:
    """Super Class"""

    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')


class Korea(Country):
    """Sub Class"""

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print('국가 이름은 : ', self.name)


class CustomClass:

    # instance method
    def add_instance_method(self, a,b):
        return a + b

    # classmethod
    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    # staticmethod
    @staticmethod
    def add_static_method(a, b):
        return a + b



class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = "한국어"



class AbstractCountry(metaclass=ABCMeta):
    name = '국가명'
    population = '인구'
    capital = '수도'

    def show(self):
        print('국가 클래스의 메소드입니다.')

class Korea(AbstractCountry):

    def __init__(self, name,population, capital):
        self.name = name
        self.population = population
        self.capital = capital

    def show_name(self):
        print('국가 이름은 : ', self.name)


class Parrot:
    def fly(self):
        print("Parrot flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

def lift_off(entity):
    entity.fly()

parrot = Parrot()
airplane = Airplane()
whale = Whale()

lift_off(parrot) # prints `Parrot flying`
lift_off(airplane) # prints `Airplane flying`
lift_off(whale) # Throws the error `'Whale' object has no attribute 'fly'`

class OpenClose:

    def open(self):
        print("작업을 시작합니다.")

    def do_something(self):
        print("작업을 진행합니다...")
        print("작업을 진행합니다...")
        print("작업을 진행합니다...")

    def close(self):
        print("작업을 종료합니다.")


def doOpenClose():
    d = OpenClose()
    d.open()
    d.do_something()
    d.close()


import unittest
import os


def custom_function(file_name):
    with open(file_name, 'rt') as f:
        return sum(1 for _ in f)


# TestCase를 작성
class CustomTests(unittest.TestCase):

    def setUp(self):
        """테스트 시작되기 전 파일 작성"""
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""
            파이썬에는 정말 단위테스트 모듈이 기본으로 포함되어 있나요? 진짜?
            멋지군요!
            단위테스트를 잘 수행해보고 싶습니다!
            """.strip())

    def tearDown(self):
        """테스트 종료 후 파일 삭제 """
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""

        custom_function(self.file_name)

    def test_line_count(self):
        self.assertEqual(custom_function(self.file_name), 3)


# unittest를 실행
if __name__ == '__main__':
    unittest.main()


def convert(s):
    """int로 변환"""
    try:
        a = int(s)
        print('성공')
    except ValueError:
        print('실패 : ValueError')
        a = -1
    except TypeError:
        print('실패 : TypeError')
        a = -1
    return a


class Rectangle:
    count = 0  # 클래스 변수

    # 초기자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수
        self.width = width
        self.height = height
        Rectangle.count += 1

    # 메서드
    def calcArea(self):
        area = self.width * self.height
        return area


import math

n = math.sqrt(9.0)

print(n)  # 3.0 출력