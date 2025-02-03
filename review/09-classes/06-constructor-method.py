# 생성자 메서드

class Person:
    # 생성자 메서드
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        self.name = name
        print('인스턴스가 생성되었습니다.')
    
    # 인스턴스 메서드
    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다. => 단축형 표현 (객체지향방식)
Person.greeting(person1)  # 얘도 가능하긴하다.

