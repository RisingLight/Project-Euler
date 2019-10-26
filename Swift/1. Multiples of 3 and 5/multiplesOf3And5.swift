var sum = 0
(3..<1000).forEach { ($0 % 3 == 0 || $0 % 5 == 0) ? (sum += $0) : (sum += 0) }
print(sum)
