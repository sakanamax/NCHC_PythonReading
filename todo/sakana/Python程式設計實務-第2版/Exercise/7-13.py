# -*- coding: utf-8 -*-
# 程式 7-13 (Python 3 version )
import os
class_101 = dict() #記錄學生座號及姓名
chi_score = dict() #記錄國文成績
eng_score = dict() #記錄英文成績
mat_score = dict() #記錄數學成績
subjects = ["國文", "英文", "數學"]
scores  = [chi_score, eng_score, mat_score]

def disp_menu():
    os.system("clear")
    print("Class 101班級成績管理系統")
    print("-------------------------")
    print("1. 輸入學生姓名")
    print("2. 輸入國文成績")
    print("3. 輸入英文成績")
    print("4. 輸入數學成績")
    print("5. 顯示成績單")
    print("0. 結束程式")
    print("-------------------------")

def enter_std_data():
    while True:
        no = int(input("座號（0==>停止輸入）："))
        if no <=0 or no >100: break
        name = input("姓名：")
        class_101[no] = name
    print(class_101)

def enter_score(subject_no):
    for no, name in class_101.items():
        print("subject_no is {}".format(subject_no)) #觀察 subject_no
        scores[subject_no][no] = \
          int(input("{},{}的{}成績:". \
            format(no, name, subjects[subject_no])))
    print(scores[subject_no])
    x = input("按Enter返回主選單")

def disp_score_table():
    for no in class_101.keys():
        # 這邊為了對齊美觀使用 {:<5} , 靠左對齊, 預設寬度5, 如果名字不足五個資源會補到5個字元寬度
        print("{:<5}:".format(class_101[no]), end="")
        total = 0
        for subject_no in range(0,3):
            #print(scores, end="*")
            total = total + scores[subject_no][no] #計算總分使用
            #列印出科目還有分數
            print("{}:{:>3} ".format(subjects[subject_no], \
              scores[subject_no][no]), end="") 
        # 這邊 {:.2f} 為浮點數, 小數點取到小數點兩位
        print("總分:{:>3}, 平均:{:.2f}".format(total, \
          float(total)/len(scores))) # 總分 / 科目 來計算平均數
    x = input("按Enter返回主選單")


### 主程式從這裡開始

while True:
    disp_menu()
    user_choice = int(input("請輸入您的選擇："))
    if user_choice==1:
        enter_std_data()
    elif user_choice>=2 and user_choice<=4:
        #這邊 user_choice - 2 是要對應 scores  = [chi_score, eng_score, mat_score]
        #輸入2 2.輸入國文成績, 2 - 2 =0, 對應到 scores[0] 的國文成績
        enter_score(user_choice - 2) 
    elif user_choice==5:
        disp_score_table()
    else:
        break
print("謝謝您的使用，再見！")
