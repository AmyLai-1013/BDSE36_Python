# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 使用者猜對要回傳「恭喜中獎」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」

secrect_num = 50

while True:
    input = int(input("請輸入1~100:"))
    if input > 100 or input < 1:
        print("超出範圍請重新輸入")
    elif input == secrect_num:
        print("恭喜中獎")
        break
    elif input < secrect_num:
        print("請輸入更大的數字")
    else :
        print("請輸入更小的數字")
    

    





     








