import os
from dotenv import load_dotenv

"""
load_dotenv()
.env 파일의 key-value를 프로그램 환경 변수에 등록
"""
load_dotenv()

print(os.getenv('SECRET_KEY'))