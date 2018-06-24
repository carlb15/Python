numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

integerToRoman(13) = "XIII"

def integerToRoman(value):
  # error when out of range
  if value < 0 or value > 1000:
    return -1

  def search(value):
    idx = 0
    for idx in range(len(digits)):
      if numerals[idx] <= value:
        break
    return idx

  result = ""
  while value > 0:
    idx = search(value)
    value -= digits[idx]
    result += numerals[idx]

  return result