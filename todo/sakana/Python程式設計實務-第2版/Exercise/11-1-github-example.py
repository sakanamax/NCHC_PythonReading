from firebase import firebase
# 這個是從 github 上面的範例抓來練習的 https://github.com/ozgur/python-firebase

# 後面的 None 代表不驗證
firebase = firebase.FirebaseApplication('https://sakanatestfirebase.firebaseio.com', None)

# 這邊要注意的是 之前課本的範例 上傳到 /user , 所以 get 就要針對 /user 而不是 github 上面的 /users
# 如果沒有指定 get 的第二個 argument 是 snapshot 名稱, 如果沒有指定的話(None), 就會列出所有的
# 也等同於存取 https://sakanatestfirebase.firebaseio.com/user.json
result = firebase.get('/user', None)

# 這樣會列出所有的資料, 包含 snaphot 與 他裡面的 Key: value
print( "all data:", result )


# 課本上的案例拿來用, 利用 for 的方式列出人名
print("")
print("=====")
for key in result:
    print(result[key]['name'])


# 這邊我指定某一個 snapshot 的名稱
result2 = firebase.get('/user', '-M1L1eK7OcF_O5dnM-i1')

# 提醒自己, 如果有兩種不同型別, 要放一起, 記得使用 , 逗號
print("")
print("=====")
print( "result2 :", result2 )