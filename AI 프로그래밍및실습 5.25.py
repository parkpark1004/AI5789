#5.25

names = ['Kang Young Min',
         'Kang Young-Min',
         'Park Dong Min',
         'Park Dong-Yun']

s_vars = [f's{i+1}="{name}"' for i, name in enumerate(names)]
for var in s_vars:
    print(var)

print()

for name in names:
    수정된 = name.replace(' ', '').replace('-', '').upper()
    print(f"{name}(은)는 {수정된}(으)로 수정됨")

for name in names:
    수정된 = name.replace(' ', '').replace('-', '').upper()
    n_개수 = 수정된.count('N')
    print(f"{수정된} : {n_개수}개의 N이 나타남")
