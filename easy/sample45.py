class BankAccount:
    def __init__(self, bankName, ownerName, savings):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings

    # 貯金額を増やし金額をint型で返す
    def depositMoney(self, depositAmount):
        # $20,000 以下の場合、手数料 $100
        if self.savings <= 20000:
            self.savings += depositAmount - 100
        else:
            self.savings += depositAmount
        return int(self.savings)

    # 貯金額を減らし、残りの貯金額を正数として返す（最大20%まで引出可）
    def withdrawMoney(self, withdrawAmount):
        maxWithdrawal = self.savings * 0.2
        if withdrawAmount > maxWithdrawal:
            withdrawAmount = maxWithdrawal
        self.savings -= withdrawAmount
        return int(self.savings)

    # 口座に毎日0.25ドル振り込まれていくとき、貯金金額をfloatで返す
    def pastime(self, day):
        return self.savings + (day * 0.25)


# ★ アンパックを使う形
args = ("Chase", "Claire Simmmons", 30000)
user1 = BankAccount(*args)
print(user1.withdrawMoney(2000))
print(user1.depositMoney(10000))
print(user1.pastime(93))

user2 = BankAccount("Bank Of America", "Remy Clay", 10000)
print(user2.withdrawMoney(5000))
print(user2.depositMoney(12000))
print(user2.pastime(505))
