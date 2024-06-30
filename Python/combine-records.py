#https://www.1point3acres.com/bbs/thread-1066917-1-1.html
#Part 1
# Input:
# merchant A, 2024-01-01, Visa, 100
# merchant A, 2024-01-01, Visa, 200
# merchant B, 2024-01-01, Visa, 500
# merchant B, 2024-01-01, MasterCard, 100
# Output：
# merchant A, 2024-01-01, Visa, 300
# merchant B, 2024-01-01, Visa, 500
# merchant B, 2024-01-01, MasterCard, 100

# contract1, merchant A, 2024-01-01, Visa, 300
#
# https://www.1point3acres.com/bbs/thread-1065342-1-1.html
# 1) check valid card numer
# 2) 加visa, amex, mastercard 等信用卡号规则
# 3) 用checksum 检查卡号是否合格
# 4) 地里没问到的,就是当input不是句子的时候,不能简单用空格split,没做完就讲了下用rege=x的思路做match/replace
from collections import OrderedDict, defaultdict


class CombineRecords:
    def combinerecords(self, stringlist):
        records = defaultdict(int)
        for each in stringlist:
            word_list = each.split(", ")
            contract = ""
            if len(word_list) == 5:
                contract, merchant, date, card, amount = word_list

            else:
                merchant, date, card, amount = word_list
            key = (merchant, date, card)
            amount = int(amount)
            if contract:
                if key in records:
                    records[key] -= amount
                    if records[key] == 0:
                        del records[key]
                else:
                    records[key] = -amount
                records[(contract, date, card)] = (records[(contract, date, card)] or 0) + amount
            else:
                if key in records:
                    records[key] += amount
                else:
                    records[key] = amount
        res = []
        sorted_records = sorted(records.items(), key=lambda x: (x[0][0], x[0][1], x[0][2]))
        # for key in records.keys():
        #     res.append(f"{key[0]}, {key[1]}, {key[2]}, {records[key]}")
        for key, amount in sorted_records:
            res.append(f"{key[0]}, {key[1]}, {key[2]}, {amount}")
        return res


if __name__ == "__main__":
    inputs = []
    sol = CombineRecords()
    while True:
        try:
            input_string = input("Enter record, done to finish")
            if input_string.lower() == 'done':
                break
            else:
                inputs.append(input_string)
        except:
            break
    print(sol.combinerecords(inputs))
