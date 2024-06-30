# /*
# Your previous Plain Text content is preserved below:
# For the purposes of this interview, imagine that we own a store. This
# store doesn't always have customers shopping: there might be some long
# stretches of time where no customers enter the store. We've asked our
# employees to write simple notes to keep track of when customers are
# shopping and when they aren't by simply writing a single letter every
# hour: 'Y' if there were customers during that hour, 'N' if the store
# was empty during that hour.
# For example, our employee might have written "Y Y N Y", which means
# the store was open for four hours that day, and it had customers
# shopping during every hour but its third one.
#   hour: | 1 | 2 | 3 | 4 |
#   log:  | Y | Y | N | Y |
#                   ^
#                   |
#             No customers during hour 3
# We suspect that we're keeping the store open too long, so we'd like to
# understand when we *should have* closed the store. For simplicity's
# sake, we'll talk about when to close the store by talking about how
# many hours it was open: if our closing time is `2`, that means the
# store would have been open for two hours and then closed.
#   hour:         | 1 | 2 | 3 | 4 |
#   log:          | Y | Y | N | Y |
#   closing_time: 0   1   2   3   4
#                 ^               ^
#                 |               |
#          before hour #1    after hour #4
# (A closing time of 0 means we simply wouldn't have opened the store at
# all that day.)
# First, let's define a "penalty": what we want to know is "how bad
# would it be if we had closed the store at a given hour?" For a given
# log and a given closing time, we compute our penalty like this:
#   +1 penalty for every hour that we're *open* with no customers
#   +1 penalty for every hour that we're *closed* when customers would have shopped
# For example:
#   hour:    | 1 | 2 | 3 | 4 |   penalty = 3:
#   log:     | Y | Y | N | Y |     (three hours with customers after closing)
# 广告
# PauseUnmute
# Loaded: 0%
# Fullscreen
#   penalty: | * | * |   | * |
#            ^
#            |
#          closing_time = 0
#   hour:    | 1 | 2 | 3 | 4 |   penalty = 2:
#   log:     | N | Y | N | Y |      (one hour without customers while open +
#   penalty: | * |   |   | * |       one hour with customers after closing)
#                    ^
#                    |
#                  closing_time = 2
#   hour:    | 1 | 2 | 3 | 4 |   penalty = 1
#   log:     | Y | Y | N | Y |      (one hour without customers while open)
#   penalty: |   |   | * |   |
#  closing_time = 4
# Note that if we have a log from `n` open hours, the `closing_time`
# variable can range from 0, meaning "never even opened", to n, meaning
# "open the entire time".
# 1a)
# Write a function `compute_penalty` that computes the total penalty, given
# a store log (as a space separated string) AND
# a closing time (as an integer)
# In addition to writing this function, you should use tests to
# demonstrate that it's correct. Do some simple testing, and then quickly
# describe a few other tests you would write given more time.
# ## Examples
# compute_penalty("Y Y N Y", 0) should return 3
# compute_penalty("N Y N Y", 2) should return 2
# compute_penalty("Y Y N Y", 4) should return 1
# 1b)
# Write another function named `find_best_closing_time` that returns
# the best closing time in terms of `compute_penalty` given just a
# store log. You should use your answer from 1a to solve this problem.
# Again, you should use tests to demonstrate that it's correct. Do
# some simple testing, and then quickly describe a few other tests
# you would write given more time.
# ## Example
# find_best_closing_time("Y Y N N") should return 2
# 2a)
# We've asked our employees to write their store logs all together in the
# same text file, marking the beginning of each day with `BEGIN` and the
# end of each day as `END`, sometimes spanning multiple lines. We hoped
# that the file might look like
# "BEGIN Y Y END \nBEGIN N N END"
# which would represent two days, where the store was open two hours
# each day. Unfortunately, our employees are often too busy to remember
# to finish the logs, which means this text file is littered with
# unfinished days and extra information scattered throughout. Luckily,
# we know that an unbroken sequence of BEGIN, zero or more Y's or N's,
# and END is going to be a valid log, so we can search the aggregate log
# for those.
# For example, given the aggregate log
# "BEGIN BEGIN BEGIN N N BEGIN Y Y END N N END"
# We can extract only one valid sequence, "BEGIN Y Y END". For our
# purposes, we should ignore any invalid sequences. *These logs cannot
# be nested.*
# Write a function `get_best_closing_times` that takes an aggregate log
# as a string and returns an array of best closing times for every valid
# log we can find, in the order that we find them.
# Again, you should use tests to demonstrate that it's correct. Do
# some simple testing, and then quickly describe a few other tests
# you would write given more time.
# ## Examples
# get_best_closing_times("BEGIN Y Y END \nBEGIN N N END")
# should return an array: [2, 0]
# get_best_closing_times("BEGIN BEGIN \nBEGIN N N BEGIN Y Y\n END N N END")
# should return an array: [2]
# */
#
# https://www.1point3acres.com/bbs/thread-1061730-1-1.html
class Solution:
    def penalty(self, storelog, closing_time):
        log = storelog.split(" ")
        # "Y"
        # "Y N" ->0, 1, 2
        penalty = 0
        for index, log in enumerate(log):
            if index < closing_time and log == 'N':
                penalty += 1
            elif index >= closing_time and log == 'Y':
                penalty += 1
            else:
                continue
        return penalty

    def bestClosingTime(self, customers: str) -> int:
        # for each hour, we just need to calculate what changes since last hour and then have the min recorded
        # kind of like dynamic programming, but may be not necessary for dp list(o(n)) to store them
        #calculate penalty at zero
        penalty = 0
        customers = customers.split(" ")
        for each in customers:
            if each == 'Y':
                penalty += 1
        res = penalty
        hour = 0
        for i in range(1, len(customers) + 1):
            if customers[i - 1] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < res:
                hour = i
                res = penalty
        return hour

    def bestClosingTime2(self, customers: str) -> int:
        best_time = 0
        best_penalty = float('inf')
        for i in range(0, len(customers) + 1):
            cur = self.penalty(customers, i)
            if cur < best_penalty:
                best_time = i
                best_penalty = cur
        return best_time

    def get_best_closing_times(self, lines):
            items = lines.split()
            res = []
            record = []
            inside_log = False

            for item in items:
                if item == 'BEGIN':
                    if inside_log:
                        # Reset if another BEGIN is found without a closing END
                        record = []
                    inside_log = True
                elif item == 'END':
                    if inside_log:
                        # Process the valid log and reset
                        res.append(self.bestClosingTime2(' '.join(record)))
                        record = []
                        inside_log = False
                else:
                    if inside_log:
                        record.append(item)

            return res

    def get_best_closing_times__v2(self, filename):
        res = []
        record = []
        inside_log = False

        with open(filename, 'r') as file:
            for line in file:
                items = line.split()
                for item in items:
                    if item == 'BEGIN':
                        if inside_log:
                            # Reset if another BEGIN is found without a closing END
                            record = []
                        inside_log = True
                    elif item == 'END':
                        if inside_log:
                            # Process the valid log and reset
                            res.append(self.bestClosingTime2(' '.join(record)))
                            record = []
                            inside_log = False
                    else:
                        if inside_log:
                            record.append(item)

        return res


if __name__ == "__main__":
    sol = Solution()
    # print(sol.penalty('Y Y N Y', 0))
    # print(sol.penalty("", 0))
    print(sol.penalty("N N Y N", 0))
    print(sol.bestClosingTime("N N Y N"))
    print(sol.bestClosingTime2("N N Y N"))
    print(sol.get_best_closing_times("BEGIN BEGIN BEGIN N N BEGIN Y Y END N N END"))
