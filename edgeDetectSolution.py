from PIL import Image

threshold = 50


try:
	img = Image.open("kitchen.jpeg")
	pix = img.load(); #loads pixel 2D array
	img2 = Image.new("RGB", img.size, "white")
	pix2 = img2.load();
except:
	print "Image doesn't exist"



def colorDist(pix1, pix2):
	return ((pix1[0] - pix2[0]) ** 2 + (pix1[1] - pix2[1]) ** 2 + (pix1[2] - pix2[2]) ** 2) ** (0.5) 


width, height = img.size

for i in range(0, width - 1):
	for j in range(0, height - 1):
		pix1 = pix[i, j]
		pixRight = pix[i + 1, j]
		pixBottom = pix[i, j + 1]

		if(colorDist(pix1, pixRight) > threshold):
			pix2[i, j] = (0, 0, 0)
		if(colorDist(pix1, pixBottom) > threshold):
			pix2[i, j] = (0, 0, 0)

img2.show();

