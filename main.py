dicti = {}

# print(type(dicti))

for i in range(5):
	j = "cust00" + str(i)
	name = "Iam" + str(i)
	ttid = i
	ccid = str(i)+str(i)

	dicti[j]= {"name" : name}
	dicti[j].update({"tid":ttid})
	dicti[j].update({"cid":ccid})


# print(dicti)
for i in dicti:
	print(i, ":")
	for j in dicti[i]:
		print("		",j, ":",dicti[i][j])