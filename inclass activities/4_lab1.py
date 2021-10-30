"""convert positive integer to base 2"""
def binarify(num):
    if num<=0: return '0'
    digits=[]
    while num>0:
      digits.insert(0,num%2)
      num=num//2
    return ''.join(str(e) for e in digits)

"""convert positive integer to a string in any base"""
def int_to_base(num, base):
    if num<=0:  return '0'
    digits = []
    while num>0:
        digits.insert(0,num%base)
        num=num//base
    return ''.join(str(e) for e in digits)

'''
"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
    if string=="0" or base <= 0 : return 0
    result = 0
    return result



def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  result = int_to_base(tmp, base1)
  return result

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result = int_to_base(tmp, base1)
  return result

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result
'''
