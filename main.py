import numpy as np

def numberEqualTo( data, n ) :
  nnn = 0
  for d in data : 
    if d==n : nnn = nnn + 1 
  return nnn
  
def negationEqualTo( data, n ) :
  # Your code goes here
  
def numberLessThan( data, n ) :
  nnn = 0
  for d in data : 
    if d<n : nnn = nnn + 1 
  return nnn
  
def negationLessThan( data, n ) :
  # Your code goes here
  
def numberGreaterThan( data, n ) :
  nnn = 0
  for d in data : 
    if d>n : nnn = nnn + 1 
  return nnn
  
def negationGreaterThan( data, n ) :
  # Your code goes here
  
# These lines of code allow you to check your code is working
data = np.loadtxt("mydata.dat")
print(negationEqualTo(data,5), "should equal", len(data) - numberEqualTo(data,5))
print(negationLessThan(data,4), "should equal", len(data) - numberLessThan(data,4))
print(negationGreaterThan(data,7), "should equal", len(data) - numberGreaterThan(data,5))
