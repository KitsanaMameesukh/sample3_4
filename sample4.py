def fact(num):
  if num ==1:
    return 1
  else:
    return num*fact(num-1)
  
if __name__ == '__main__':
  countNum = 0
  number = int(input("Please enter a number "))
  result  = str(fact(number))
  for i  in range(len(str(result)),0,-1):
    if result[i-1] == "0" :
      countNum+=1
    else:
      break
       
  print(str(number)+"! = "+str(result)+" มีเลข 0 ต่อท้าย "+str(countNum)+" ตัว")

    