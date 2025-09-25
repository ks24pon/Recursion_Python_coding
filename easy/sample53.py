# 配列idsを右にn回ローテーションする関数
def rotateByTimes(ids,n):
    # 配列の長さを取得
    length = len(ids)

    # nを配列の長さで割った余りにする
    # nが配列より大きくても正しく処理できる
    n = n % length

    # nが0の場合は回転せず、そのまま返却
    if n == 0:
        return ids

    # スライス使って回転 *重要
    return ids[-n:] + ids[:-n]