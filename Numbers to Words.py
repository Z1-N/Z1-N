def numToEng(n: int) -> str:
  number = n
  ones = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
  ons2 = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
  tens = ["ten","twenty","thirty", "forty", "fifty", "sixty","seventy","eighty","ninety"]
  if (number) <= 10 :         # Numbers less than 10
    return ones[number]
  elif number % 10 == 0 and 100 > number > 10: # factors of 10
    digit = number // 10**1 % 10
    return tens[digit-1]
  elif number > 10 and number <= 20:   # Numbers from 10 to 20
    number = number - 10
    return ons2[number]
  elif number > 20 and number <= 30:  # Numbers from 20 to 30
    while number > 10 :
      number = number - 10
    return "twenty" + "-" + ones[number] 
  elif number >= 30 and number <= 99: # Numbers from 30 to 99
    digit = number // 10**1 % 10
    while number >= 10 :
      number = number - 10
    return tens[digit-1] + "-" + ones[number]
  elif number % 100 == 0 : # Hundreds
    dig = number // 100 
    return ones[dig] + " " +"hundred"
  elif number > 100 : # Numbers from 100 to 999
    hund = number // 100 
    ten = number // 10
    while ten >= 10 :
      ten = ten - 10
    one = number - (hund * 100) - (ten * 10)
  er_num = ten * 10 + one 
  if 19 >= er_num >= 11 :
    return ones[hund] + " hundred " + ons2[one]
  elif one == 0 :
     return ones[hund] +  " hundred "+ tens[ten-1] 
  elif ten == 0 :
     return ones[hund] + " hundred "  + ones[one] 
  else:
      return ones[hund] + " hundred " + tens[ten-1] + "-"  + ones[one] 
