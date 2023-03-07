import csv
# load a csv file
with open('../list.csv', 'r',encoding='utf-8') as csvfile:
  with open('./list.csv', 'w', newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['名称','作者','摆放位置','建筑总数','电量','物品','需求建筑'])

    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
      res = []
      # print(row[0]) # 名称 -> res[0]
      res.append(row[0])
      # print(row[1]) # 作者 -> res[1]
      res.append(row[1])
      # print(row[2]) # 摆放位置 -> res[2]
      res.append(row[2])
      # print(row[3]) # 建筑总数 -> res[3]
      res.append(row[3])
      # print(row[4]) # 用电量 

      # print(row[5]) # 发电量

      # 发电量 - 用电量 = 电量 -> res[4]
      # print(int(row[5])-int(row[4]))
      res.append(str(int(row[5])-int(row[4])))

      itemStatus = {}
      # print(row[6]) # 产物
      for re in row[6].split(';'):
        name,num = re.split(':')
        if itemStatus.get(name) == None:
          itemStatus[name] = 0
        itemStatus[name] += int(num)
      # print(itemStatus)
      # print(row[7]) # 原料
      for re in row[7].split(';'):
        name,num = re.split(':')
        if itemStatus.get(name) == None:
          itemStatus[name] = 0
        itemStatus[name] -= int(num)
      
      for rub in itemStatus:
        if itemStatus[rub] == 0:
          del itemStatus[rub]
      
      rt = ""
      for rees in itemStatus:
        rt += rees+':'+str(itemStatus[rees])+';'
      # 产物 - 原料 = 物品 -> res[5]
      rt = rt.strip(';')
      res.append(rt)

      # print(row[8]) # 需求建筑 ->res[6]
      res.append(row[8])

      # print(res)

      writer = csv.writer(f)
      writer.writerow(res)

# write to csv

    
    
