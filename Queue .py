# Queue is a data structure
# Queue works as First In First Out(FIFO)

from collections import deque

bank = deque(["Athika", "Priya", "Rittika"])
print(bank)
bank.popleft()
print(bank)

bank.popleft()
bank.popleft()
print(bank)

if not bank:
    print("No person left")