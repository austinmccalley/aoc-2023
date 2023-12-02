import re

# Part 1

f = open("day1/input.txt")
contents = f.read()
lines = contents.split('\n')

nums = []
for l in lines:
  tmp = re.findall(r'\d', l)
  res = list(map(str, tmp))
  res = ''.join(res)
  res = [x for x in res]
  res = [res[0], res[-1]]

  d_s = ''.join(res)
  d = int(d_s)

  assert d < 100


  nums.append(d)

print(sum(nums))
f.close()


# Part 2
word_lookup = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

pattern = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))(?=(one|two|three|four|five|six|seven|eight|nine|\d))')

def handleWordOrDigit(x: str) -> str:
  return x if x.isdigit() else str(word_lookup[x])


f = open("day1/input.txt")
contents = f.read()
lines = contents.split('\n')

nums = []
for l in lines:
  tmp = re.findall(pattern, l)
  tmp = [x[0] for x in tmp]
  res = list(map(str, tmp))

  digits = [handleWordOrDigit(x) for x in res]

  res = [digits[0], digits[-1]]

  d_s = ''.join(res)
  d = int(d_s)

  assert d < 100
  nums.append(d)

print(sum(nums))
f.close()


