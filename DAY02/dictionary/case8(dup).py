# 중첩된 딕셔너리 생성
students = {
    "student1": {
        "name": "Alice",
        "age": 21
    },
    "student2": {
        "name": "Bob",
        "age": 22
    }
}

# 중첩된 딕셔너리 접근
print("학생 1의 이름:", students["student1"]["name"])  # Alice
print("학생 2의 나이:", students["student2"]["age"])   # 22
