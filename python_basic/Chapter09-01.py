# 파일 읽기 및 쓰기
# 읽기 r / 쓰기 w / 추가 append / 텍스트 t / 바이너리 b
# 상대 경로 ../, ./ 절대 경로 c:\Django\example..

# 파일 읽기(read)
# 예제1
#f = open('C:\Users\남정현\PycharmProjects\pythonProject\python_basic\resource\it_new.txt')
f = open('./resource/it_news.txt','r',encoding='UTF-8')
# 속성확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
print(f.name)
print(f.mode)

cts = f.read()
print(cts)
f.close()

# 예제2
with open('./resource/it_news.txt','r',encoding='UTF-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제3
# read() : 전체 읽기, read(10) : 10 Byte

with open('./resource/it_news.txt','r',encoding='UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20)
    print(c)
    f.seek(0,0)
    c = f.read(20)
    print(c)

print()
print()

# 예제4
# readline : 한 줄 씩 읽기
with open('./resource/it_news.txt','r',encoding='UTF-8') as f:
    c = f.readline()
    print(c)

print()
print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장

with open('./resource/it_news.txt','r',encoding='UTF-8') as f:
    cts = f.readlines()
    print(cts)
    print()

    for c in cts:
        print(c, end='')

print()

# 파일 쓰기(write)

# 예제1
with open('./resource/contents1.txt', 'w') as f:
    f.write('I love python\n')

# 예제2
with open('./resource/contents1.txt', 'a') as f:
    f.write('I love python2\n')

# 예제3
# writelines : 리스트 -> 파일
with open('./resource/contents2.txt', 'w') as f:
    list = ['orange\n', 'Apple\n', 'banana\n', 'Melon\n']
    f.writelines(list)

# 예제4
with open('./resource/contents3.txt', 'w') as f:
    print('Test Text Write', file=f)
    print('Test Text Write', file=f)
    print('Test Text Write', file=f)