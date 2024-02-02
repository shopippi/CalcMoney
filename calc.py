import re

def format_large_number(number):
    if number < 1000:
        return f"{number}円"
    elif number < 10000:
        return f"{number / 1000:.2f}千円"
    elif number < 100000000:
        return f"{number / 10000:.2f}万円"
    else:
        return f"{number / 100000000:.2f}億円"

def parse_amount(text):
    # カンマを取り除く
    text = text.replace(",", "")

    # 正規表現を使用して数値を抽出
    match = re.search(r'\d+', text)
    if match:
        amount = int(match.group())
        return amount
    else:
        return None

# 例: "1000千円"を数値に変換
input_text = input()
parsed_amount = parse_amount(input_text)

if parsed_amount is not None:
    formatted_amount = format_large_number(parsed_amount)
    print(formatted_amount)
else:
    print("無効な入力です")
