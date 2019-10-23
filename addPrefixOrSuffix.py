f = open("/home/ub/Yolo2/darknet/VOCdevkit/VOC2012/ImageSets/Main/val.txt")
lines = f.readlines()
f.close()
new_lines = [ "/home/ub/Yolo2/darknet/VOCdevkit/VOC2012/JPEGImages/"+ x.strip() + '\n' for x in lines] 

with open('/home/ub/Yolo2/darknet/VOCdevkit/VOC2012/ImageSets/Main/valnew.txt', 'w') as f:
    f.writelines(new_lines)
