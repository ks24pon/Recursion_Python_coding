# 解雇される従業員を除いた新しい従業員リストを返す
def fireEmployees(employees,unemployed):
    # 解雇リストをセットに変換
    fireList = set(unemployed)

    # 残る従業員を格納するリスト
    remainingEmployees = []

    # 元の従業員リストを1人ずつ確認
    for employee in employees:
        # 解雇リストに含まれていない場合のみ残留リストに追加
        if employee not in fireList:
            remainingEmployees.append(employee)


    return remainingEmployees