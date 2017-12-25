# -*- coding: utf-8 -*-


start_a, start_b = 618, 814
af, bf = 16807, 48271
mod = 2147483647
a = start_a
b = start_b
same = 0

for _ in xrange(40 * 10 **6):
  if (a & 0xffff) == (b & 0xffff):
    same += 1
  a = (a * af) % mod
  b = (b * bf) % mod
print same

a = start_a
b = start_b
generated_as = []
generated_bs = []
while True:
  a = (a * af) % mod
  if (a & 3) == 0: # accidentally had a 4 here the first time, so had to eat a minute penalty :(
    generated_as.append(a)
  b = (b * bf) % mod
  if (b & 7) == 0:
    generated_bs.append(b)
  if min(len(generated_as), len(generated_bs)) > (5 * 10**6):
    break

print len(filter(lambda (a,b): (a & 0xffff) == (b & 0xffff), zip(generated_as, generated_bs)[:5*10**6]))



