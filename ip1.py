import numpy as np
np.seterr(over='ignore')
from PIL import Image
import matplotlib.pyplot as plt
import time
from functools import reduce
from collections import Counter

def createExample():
	numberArrayExample = open('numArrEx.txt', 'a')
	numbersWeHave = range(0, 10)
	versionWeHave = range(1, 10)

	for eachNum in numbersWeHave:
		for eachVer in versionWeHave:
			#print(str(eachNum)+'.'+str(eachVer))
			imageFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
			ei = Image.open(imageFilePath)
			eiar = np.array(ei)
			eiar1 = str(eiar.tolist())

			lineToWrite = str(eachNum)+'::'+eiar1+'\n'
			numberArrayExample.write(lineToWrite)


def threshold(imageArray):
	blanceAr = []
	newAr = imageArray

	for eachRow in imageArray:
		for eachPix in eachRow:
			avgNum = reduce(lambda x,y: x+y, eachPix[:3])/len(eachPix[:3])
			blanceAr.append(avgNum)

	balance = reduce(lambda x,y: x+y, blanceAr[:3])/len(blanceAr[:3])

	for eachRow in newAr:
		for eachPix in eachRow:
			if reduce(lambda x,y: x+y, eachPix[:3])/len(eachPix[:3]) >= balance:
				eachPix[0] = 255
				eachPix[1] = 255
				eachPix[2] = 255
				eachPix[3] = 255
			else:
				eachPix[0] = 0
				eachPix[1] = 0
				eachPix[2] = 0
				eachPix[3] = 255
			#print(eachPix)
			#time.sleep(0.1)

	return newAr

def whatNumberIsThis(filepath):
	matchedAr = []
	loadExams = open('numArrEx.txt', 'r').read()
	loadExams = loadExams.split('\n')

	i = Image.open(filepath)
	iar = np.array(i)
	iarl = iar.tolist()

	inQuestion = str(iarl)

	#print(inQuestion)

	for eachExams in loadExams:
		if len(eachExams) > 3:
			splitEx = eachExams.split('::')
			currentNum = splitEx[0]
			currentAr = splitEx[1]

			eachPixEx = currentAr.split('],')
			#eachPixQ = str(inQuestion.split('\n'))
			#eachPixQ = eachPixQ.split('],')
			eachPixQ = inQuestion.split('],')

			#print(eachPixEx)
			#print('\n')
			#print(eachPixQ)

			x=0
			while x < len(eachPixEx):
				if eachPixEx[x] == eachPixQ[x]:
					matchedAr.append(int(currentNum))

				x += 1

	print(matchedAr)
	x = Counter(matchedAr)
	print(x)

	graphX = []
	graphY = []

	for eachThing in x:
		print(eachThing)
		graphX.append(eachThing)
		print(x[eachThing])
		graphY.append(x[eachThing])

	fig = plt.figure()
	ax1 = plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
	ax2 = plt.subplot2grid((4,4), (1,0), rowspan=3, colspan=4)

	ax1.imshow(iar)
	ax2.bar(graphX, graphY, align='center')
	plt.ylim(400)

	xloc = plt.MaxNLocator(12)

	ax2.xaxis.set_major_locator(xloc)

	plt.show()

#createExample()
whatNumberIsThis('images/numbers/9.6.png')

'''i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 =Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

threshold(iar3)
threshold(iar2)
threshold(iar4)
#print(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()'''