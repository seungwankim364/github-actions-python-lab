import os
secret_value = os.getenv("SECRET_MESSAGE")
secret_value2 = os.getenv("SECRET_MESSAGE2")

if secret_value:
    print("SECRET_MESSAGE 값")
else:
    print("SECRET_MESSAGE 값 없음")


if secret_value2:
    print("SECRET_MESSAGE2 값")
else:
    print("SECRET_MESSAGE2 값 없음")