import os
try:
    os.remove('filename')
except FileNotFoundError:
    print('無法刪除檔案: 找不到檔案')
except PermissionError:
    print('無法刪除檔案: 檔案權限或種類錯誤')
except:
    print('無法刪除檔案: 未知錯誤')