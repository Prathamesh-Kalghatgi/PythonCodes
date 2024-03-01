camera = {"Sony":600,"Nikon":650,"Canon":700}
print(camera)
print(camera.keys())
print(camera.values())
copycamera =camera.copy()
print(copycamera)
del copycamera["Sony"]
print(copycamera)
copycamera.clear()
print(copycamera)