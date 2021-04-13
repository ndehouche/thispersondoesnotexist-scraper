from PIL import Image
import tpdne
import base64



for k in range(5):
	imagedata = base64.b64decode(tpdne.tpdne_base64())
	filename = str(k)+".jpg"   
	with open(filename, 'wb') as f:
    		f.write(imagedata)
