people = []
for i in range(0,10):
	i = int(input('請輸入數字:'))
	people.append(i)
print(people)
print(end='\n')

for question in range(0,5):
	a = int(input('頭在哪裡:'))
	b = int(input('尾在哪裡:'))
	print('總合為:', sum(people[a:b]))
	print(end='\n')	