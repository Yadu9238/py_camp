string = "manipal prolearn"
x=""
maps = {
    'a':'2',
    'e':'4',
    'i':'6',
    'o':'8',
    'u':'10'
}
newst = []
for i in list(string):
    try:
        newst.append(maps[i.lower()])
    except KeyError:
        newst.append(i)

half=len(newst)//2      
newst = ''.join([newst[i].upper() if i >= half else newst[i]
         for i in range(len(newst)) ])

print(newst)