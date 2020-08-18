# CSMU Crawer
設計來抓取中山醫學大學各網站資料的 python package    

## Information

- csmuCrawer
  - News
    - get()
  - ILms
    - CheckAccount()

---

## (Class) News

### 建構函式    

> `__init__(date)`    
> date format is "YY/MM/DD" or "today" or "yesterday"

```python
from csmuCrawer import News

news = News("today") #取得今日公告
news = News("yesterday") #取得昨日公告
news = News("%Y/%m/%d") #取得特定日期公告
```
### `get()`

> 取得資料 
> Return JSON format string

```python
from csmuCrawer import News

news = News("today") #取得今日公告
news.get()
```

### Return Format

```json
{
    "status": True/False,
    "date": "Date of NEWS",
    "data":[
        {
            "name": "NEWS NAME",
            "Category": "NEWS CATEGOTY",
            "Apartment": "NEWS APARTMENT",
            "Url": "URL of NEWS"
        }
    ]
}
```

---

## (Class) ILms

### CheckAccount(user, password)
> 檢查帳號密碼是否正確   
> 參數: `user` = "帳號"; `password` = "密碼"      
    
     
### Return Format
`bool` (成功為 True / 失敗為 False)

---

### GetSession()
> 取得帳戶登入後的PHP session

### Return format
`str` (26碼 PHP SESSION)
