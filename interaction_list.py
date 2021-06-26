list_1 = ['Sex',"Pclass","Fare","Age","SibSp","SibSp>0","Parch>0","Embarked=C","Embarked=None","Embarked=Q","Embarked=S", "CabinType=A","CabinType=B","CabinType=C","CabinType=D","CabinType=E","CabinType=F","CabinType=G","CabinType=None","CabinType=T"]

list_2 = ['Sex',"Pclass","Fare","Age","SibSp","SibSp>0","Parch>0","Embarked=C","Embarked=None","Embarked=Q","Embarked=S", "CabinType=A","CabinType=B","CabinType=C","CabinType=D","CabinType=E","CabinType=F","CabinType=G","CabinType=None","CabinType=T"]

my_list = []

for value_1 in list_1:
  for value_2 in list_2:
    added_foward = value_1 + " * " + value_2
    added_backward = value_2 + " * " + value_1
    if "CabinType" in value_1 and "CabinType" in value_2:
      continue
    if "Embarked" in value_1 and "Embarked" in value_2:
      continue
    if "SibSp" in value_1 and "SibSP" in value_2:
      continue
    if "Parch" in value_1 and "Parch" in value_2:
      continue
    if added_foward not in my_list and added_backward not in my_list and value_1 != value_2:
        my_list.append(added_foward)
print(my_list)

