# 讀取一個string, 實現currency conversion相關的需求
# 例子: USD:AUD:1.4,CAD:USD:0.8,USD:JPY:110
# Part 1: 給定一組currency code, 如果input string裏有直接記錄conversion rate的話, 返回該conversion rate
# Part 2: 如果conversion rate可經由一次轉換計算岀來(如CAD:AUD), 也需返回
# Part 3: 計算Part 2中的conversion rate時, 需用"best conversion calculation available"
# Part 4: 應能返回所有可從input string計算岀的conversion rate pairs
from collections import  defaultdict, deque
class CurrencyConverter:
    def coversion_rate(self,raw):
        res = defaultdict(dict)
        items = raw.split(",")
        for each in items:
            A, B, rate = each.split(":")
            rate = float(rate)
            res[A][B] = float(rate)
            res[B][A] = 1/float(rate)
        return res

    def get_indirect_rate(self, rates, src, dest):
        if src==dest:
            return 1.0
        queue = deque([src,1.0])
        visited=set(src)
        while queue:
            cur, cur_rate = queue.popleft()
            for neighbor, rate in rates[cur].items():
                if neighbor not in visited:
                    acc_rate = cur_rate * rate
                    if neighbor==dest:
                        return acc_rate
                    visited.add(neighbor)
                    queue.append((neighbor,acc_rate))
        return None

    def get_all_indirect_rate(self,rates):
        indirect_rates = {}
        currencies = list(rates.keys())
        for i in range(len(currencies)):
            for j in range(len(currencies)):
                src = currencies[i]
                dest = currencies[j]
                rate = self.get_indirect_rate(rates, src, dest)
                if rate:
                    indirect_rates[(src, dest)] = rate
                    indirect_rates[(dest, src)] = 1 / rate
            return indirect_rates

    def bfs_find_rate(rates, src, dest):
        queue = deque([(src, 1.0)])
        visited = set([src])

        while queue:
            current, current_rate = queue.popleft()
            for neighbor, rate in rates[current].items():
                if neighbor == dest:
                    return current_rate * rate
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_rate * rate))
        return None
if __name__ == "__main__":
    print(conversion_rate2("USD:AUD:1.4,CAD:USD:0.8,USD:JPY:110"))
