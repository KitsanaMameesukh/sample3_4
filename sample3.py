def find_MaxIndex(num):
  maxValue = 0
  index = 0
  for i in num:
    if i>maxValue:
      maxValue = i
      index+=1
  print("ลำดับที่มีค่ามากที่สุด คือ index = "+str(index))
  
if __name__ == '__main__':
  result = find_MaxIndex([1,2,1,3,5,6,4])