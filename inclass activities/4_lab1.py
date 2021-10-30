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
