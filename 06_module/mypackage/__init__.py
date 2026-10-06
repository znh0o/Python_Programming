#__init__.py(패키지 초기화 파일)
#1. 패키지를 import할 때 실행되어야 하는 초기화 코드
print("__init__")

#패키지 메타데이터 설정
version = "1.0.0"

#2. 패키지 내 모듈을 re-export
from mypackage.mymath import add, PI #절대 임포트
from .mymath import add, PI #상대 임포트