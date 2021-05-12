import requests
res = requests.get("http://google.com")
print("응답코드 :", res.status_code) # 200 이면 정상
res.raise_for_status() # 정상이면 스크래핑 하고, 아니면 멈추는

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("오류 발생",res.status_code)

print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf-8") as d:
    d.write(res.text)