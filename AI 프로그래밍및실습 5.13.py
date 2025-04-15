#5.13

pi = 3.14

def get_volume(shape, a=0, b=0, c=0):
    if shape == "정육면체":
        return a * a * a
    elif shape == "직육면체":
        return a * b * c
    elif shape == "원뿔":
        return (1/3) * pi * a * a * b
    elif shape == "구":
        return (4/3) * pi * a * a * a
    elif shape == "원기둥":
        return pi * a * a * b

print("(1)", get_volume("정육면체", a=12))
print("(2)", get_volume("정육면체", a=20))
print("(3)", get_volume("직육면체", a=3, b=5, c=6))
print("(4)", get_volume("원뿔", a=20, b=10))
print("(5)", get_volume("구", a=15))
print("(6)", get_volume("원기둥", a=20, b=10))
