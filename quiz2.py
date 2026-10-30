consumption_records=[]

def input_str_must(msg) -> str:
    """文字必填欄位輸入"""
    while True:
        answer = input(msg)
        if answer != "":
            break
        else:
            print("欄位不可為空")
    return answer

def input_number(msg) :
    """請輸入大於 0 的數字，可包含小數點。"""
    while True:
        text = input(msg).strip()
        check_text=text.replace(".","",1)

        if check_text.isdigit() and check_text.isascii() :
            amount = float(text)
            if amount>0 :
                return amount
            else :
                print("請輸入大於 0 的有效金額。")
            
        else:
            print("請輸入大於 0 的數字，可包含小數點。")

while True:
    print("""--- 消費紀錄統計系統 ---
1. 新增消費
2. 顯示消費明細
3. 顯示統計
4. 退出系統
-----------------------""")
    select_function=input("請選擇功能")
    if select_function=="1":
        items=input_str_must("請輸入消費項目:")
        amount=input_number("請輸入金額:")
    elif select_function=="2":
        print("")
    elif select_function=="3":
        print("")
    elif select_function=="4":
        print("系統已退出。")
        break
    else:
        print("選項錯誤，請重新選擇。")