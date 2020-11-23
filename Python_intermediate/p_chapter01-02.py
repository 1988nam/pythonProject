# 개발 가상환경 설정 테스트 코드

import pendulum
from datetime import datetime

pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')

print(type(pst))

print(datetime.now(pst))
print(datetime.now(ist))

# 타입 확인

print(type(ist))

