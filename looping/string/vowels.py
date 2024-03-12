input_string  =  "Anandakrishnan" 
input_string  =  input_string  .  lower  () 
vowels  =  "aeiou" 
count  =  0 
for  i  in  input_string  : 
  if  i  in  vowels  : 
    count  +=  1 
print  (  "Number of vowels:"  ,  count )