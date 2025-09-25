# URLのリストをページネーションする関数
def websitePagination(urls,pageSize,page):
    # 開始位置を計算(0始まりに直す)
    startIndex = (page - 1) * pageSize
    # startIndexから+pageSize分を切り出す
    return urls[startIndex:startIndex + pageSize]
