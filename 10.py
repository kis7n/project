a = float(input())  # ввод угла поворота часовой стрелки
oboroty = int(a // 360)
ugol = a % 360

hours = oboroty * 12 + int(ugol//30)
minutes= int(ugol * 2) - hours*60
seconds= int(ugol * 2 * 60) - minutes*60 - hours*3600

print(hours, minutes, seconds, sep=', ')
