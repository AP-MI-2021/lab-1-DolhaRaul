'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n <= 1:
    return False
  if n == 2:
    return True
  div = 2
  while div * div <= n:
    if n % div == 0:
      return False
    div = div + 1
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  prod = 1
  for i in lst:
    prod = prod * i
  return prod



  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  print("hello world")
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  print("SOFRAAAN")
  
  
def main():
  print("hello world")

if __name__ == '__main__':
  main()
  lst = [1,2 ,3 ,4]
  print(get_product(lst))
