#!/usr/local/bin/python3
    
def fibonacci(NumTerms = 10):
    '''Returns NumTerms terms of the Fibonacci Sequence '''

    terms = [0,1]

    i = 2

    while i < NumTerms:
        terms.append(terms[i-2]+terms[i-1])
        i += 1
    
    return terms


def erast(uBound):
    '''Returns a list of prime numbers <= uBound '''
    candidates = [2, 3, 5, 7, 11]
    
    if uBound <= candidates[-1]:
        return [i  for i in range(uBound + 1) if i in candidates]
    
    candidates += [i  for i in range(13, uBound + 1) if i % 2 and i % 3 and i % 5 and i % 7 and i % 11]
    
    for i in candidates[5:]:
        j = i * 2
        while j <= uBound:
            if j in candidates:
                candidates.remove(j)
            j += i
    
    return candidates
    

def primeFact(num):
    '''Prime Factorization of num'''
    
    primeList = erast(num)
    factList = []
    tempNum = num
    
    if num == primeList[-1]:
        return [num]
    
    while tempNum > 1:
        for i in primeList:
                
            while i <= tempNum and tempNum % i == 0:
                #print "Testing ", i
                factList.append(i)
                tempNum /= i
                
        
    return factList
    
def printPrimeFacts(factLen, uBound):
  '''Prints a list of numbers/prime factorization where there are factLen prime factors'''
  
  xFactors = []
  
  for i in range(4, uBound + 1):
    facts = primeFact(i)
    
    if len(facts) == factLen:
      xFactors.append([i, facts])
    
  for i in xFactors:
    print(i[0],":\t",i[1])
      

printPrimeFacts(3, 50)
