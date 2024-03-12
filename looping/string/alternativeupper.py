s  =  "PythonDjango" 
result  =  " " 
upr  =  True 
for  i  in  s  : 
 if  upr  : 
  result  +=  i  .  upper  () 
 else  : 
  result  +=  i  .  lower  () 
 upr  =  not  upr 
print  (  result  ) 