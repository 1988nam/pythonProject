import re

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe | caffe(x)
# ^ (^de) : 문자열의 시작 > desk, destination | fade(x)
# $ (se$) : 문자열의 끝 > case, dice

def print_match(m):

    if m:
        print("group:", m.group())
        print("string:", m.string)
        print("start:", m.start())
        print("end:", m.end())
        print("span:",m.span())
    else:
        print("매칭 실패")
#
# m = p.match("case")
# print_match(m)

# m = p.search("careless") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("care cafe") # 일치하는 모든 것을 리스트 형태로 반환
print(lst)