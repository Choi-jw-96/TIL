class person:

    def greeting(self):
        return "hi"

iu = person()
jimin = person()

print(type(iu))     # person

print(iu.greeting)  # hi

print(iu.name)  # 속성값 없음

#속성부여
iu.name = "아이유"
jimin.name = "지민"
print(iu.name)
print(jimin.name)


a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)   #True(동일한 항목이 있으니까) False(주소값이 다른 별개의 객체니까)

b = a
print(a is b)   # True (주소 자체가 저장됨)



class person:
    # 생성자 메서드
     def __init__(self, name):
        self.name = name
     def greeting(self):     # 호출 시 self가 먼저 출력
         return f'안녕 난{self.name}'
p1 = person('아이유')   # init메서드 호출
print(p1.greeting())    # 직접 greeting을 호출
# == print(person.greeting(p1))
    #  def __del__(self): self 소멸




# 소개팅
class person:
    def __init__(self, name, age, mbti):
        self.name = name
        self.age = age
        self.mbti = mbti
    def greeting(self):
        return f'{self.name}입니다. {self.mbti}이구요.'
    
    def __gt__(self, other):    # 나이가 많은사람이 더 커
        # ge == (p1 > p2)    
        if self.age > other.age:
            return self
        else:
            return other
    def __str__(self):
        return f'{self.name}({self.age})'


p1 = person('재용', 30, 'istp')
p2 = person('유영', 28, 'enfj')
print(p1.name)
print(p1.greeting)
print(p1 > p2)  # 재용(30)
print(p1)   # 데이터 조각이 나옴
print(p1)   # 재용(30)
print(len(p1))  # 30