import imageio
import os

now= os.getcwd()
path="frames"
frames_path= os.path.join(now,path)


reader= imageio.get_reader("ornek.mp4")
count=4
for i,frame in enumerate(reader):
    if count==4:
        imageio.imwrite(path+"/frame%d.jpg" % i, frame)
        count=0
    count+=1






