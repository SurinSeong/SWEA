# 절차 지향 사고
# 절차 지향 프로그래밍 : 프로그램을 함수와 로직(절차) 중심으로 작성. 데이터를 함수에 전달하며 순차적으로 처리
# 예: 변수와 함수를 별개로 다룸
name = 'Alice'
age = 25


def introduce(name, age):
    print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')


introduce(name, age)

'''
<특징>
- 입력을 받고, 처리하고, 결과를 내는 과정이 위에서 아래로 순차적으로 흐르는 형태
- 순차적인 명령어 실행
- 데이터와 함수(절차)의 분리
- 함수 호출의 흐름이 중요
==> 데이터를 다시 재사용하거나 하기보다는 처음부터 끝까지 실행되는 결과물이 중요

<한계>
1. 복잡성 증가
    - 프로그램 규모가 커질수록 데이터와 함수의 관리가 어려움
    - 전역 변수의 증가로 인한 관리의 어려움
2. 유지보수 문제
    - 코드 수정 시 영향 범위 파악이 어려움
'''

# 객체 지향 사고
# 객체 지향 프로그래밍 : 데이터와 함수를 하나의 단위(객체)로 묶어서 관리. 객체들을 조합하고 재활용하는 방식으로 프로그램 구성.
# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')


alice = Person('Alice', 25)
alice.introduce()  # 객체가 자신의 정보를 출력

'''
<특징>
- 프로그램을 데이터(변수)와 그 데이터를 처리하는 함수(메서드)를 하나의 단위(객체)로 묶어서 조직적으로 관리
- 데이터와 메서드의 결합
- 코드의 구조화와 재사용성을 높이는 동시에, 실제 세계의 모델링 방식과 더 유사한 프로그래밍을 가능하게 함.
'''
