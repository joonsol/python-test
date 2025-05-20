# 최소한의 UI 구성 예시
import streamlit as st
import datetime

st.title("테스트 앱입니다")
st.write("이 문장이 보여야 정상입니다.")
# 📅 만나이 계산기

def calculate_age(year, month, day):
    try:
        birth = datetime.date(year, month, day)
        today = datetime.date.today()
        age = today.year - birth.year

        # 생일이 안 지났으면 한 살 빼기
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1

        return age

    except ValueError:
        return None


# 🔽 사용자 입력
print("출생 정보를 입력하세요.")
try:
    y = int(input("출생 연도 (예: 1990): "))
    m = int(input("출생 월 (1~12): "))
    d = int(input("출생 일 (1~31): "))
    age = calculate_age(y, m, d)

    if age is not None:
        print(f"\n📌 오늘 기준 만나이는 {age}세입니다.")
        # 생일이 오늘이라면 축하 메시지 출력
        today = datetime.date.today()
        if (today.month, today.day) == (m, d):
            print("🎉 생일 축하합니다!")
    else:
        print("\n❗ 날짜를 잘못 입력했습니다.")

except ValueError:
    print("\n❗ 숫자만 입력해 주세요.")
