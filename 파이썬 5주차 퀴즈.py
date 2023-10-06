def print_gugudan(dan):
    print(f"------[ {dan} 단 ] ------")
    for i in range(1, dan + 1):
        result = dan * i
        print(f"{dan} X {i} = {result}")

def main():
    try:
        max_dan = int(input("몇 단까지 출력할까요? "))
        for dan in range(1, max_dan + 1):
            print_gugudan(dan)
    except ValueError:
        print("올바른 숫자를 입력하세요.")

if __name__ == "__main__":
    main()
