import re

# Part 1

def cleanUpCubeStr(s: str) -> int:
  if len(s) > 0:
    n = re.findall(r"\d+", s[0])

    return int(n[0])
  return 0


f = open("day2/input.txt")
contents = f.read()
lines = contents.split('\n')

game_start_re = r"Game \d:"
red_re = r"\d+ red"
green_re = r"\d+ green"
blue_re = r"\d+ blue"

red_max = 12
green_max = 13
blue_max = 14

game_ids = []

i = 1 
for l in lines:
  r = re.sub(game_start_re, "", l, 0, re.MULTILINE)
  sets = r.split(';')
  abort = False

  for s in sets:
    # Red test
    r = re.findall(red_re, s)
    if r:
      reds = cleanUpCubeStr(r)
      if reds > red_max:
        abort = True
    g = re.findall(green_re, s)
    if g:
      greens = cleanUpCubeStr(g)
      if greens > green_max:
        abort = True
    b = re.findall(blue_re, s)
    if b:
      blues = cleanUpCubeStr(b)
      if blues > blue_max:
        abort = True

    if abort:
      break

  if not abort: 
    game_ids.append(i)

  i += 1

print(sum(game_ids))


# Part 2

f = open("day2/input.txt")
contents = f.read()
lines = contents.split('\n')

game_start_re = r"Game \d:"
red_re = r"\d+ red"
green_re = r"\d+ green"
blue_re = r"\d+ blue"

game_powers = []

i = 1 
for l in lines:
  r = re.sub(game_start_re, "", l, 0, re.MULTILINE)
  sets = r.split(';')
  abort = False

  max_reds = -1
  max_greens = -1
  max_blues = -1

  for s in sets:
    # Red test
    r = re.findall(red_re, s)
    if r:
      reds = cleanUpCubeStr(r)
      if reds > max_reds:
        max_reds = reds
    g = re.findall(green_re, s)
    if g:
      greens = cleanUpCubeStr(g)
      if greens > max_greens:
        max_greens =greens 
    b = re.findall(blue_re, s)
    if b:
      blues = cleanUpCubeStr(b)
      if blues > max_blues:
        max_blues = blues 

  maxs = [max_reds, max_greens, max_blues]
  power = max_reds * max_greens * max_blues

  game_powers.append(power)

  i += 1

print(sum(game_powers))



