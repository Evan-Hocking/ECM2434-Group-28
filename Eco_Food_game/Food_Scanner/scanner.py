# Importing library
import cv2
from pyzbar.pyzbar import decode

###### Might have to fiddle around with this to get it working ######

# Make one method to decode the barcode
def barcodeReader(image) -> dict:
	
	# read the image in numpy array using cv2
	img = cv2.imread(image)
	
	# Decode the barcode image
	detectedBarcodes = decode(img)

	isBarcode = True
	barcodeNum = 1
	# If not detected then print the message
	if not detectedBarcodes:
		isBarcode = False
	else:
	
		# Traverse through all the detected barcodes in image
		for barcode in detectedBarcodes:
		
			# Locate the barcode position in image
			(x, y, w, h) = barcode.rect
			
			# Put the rectangle in image using
			# cv2 to highlight the barcode
			cv2.rectangle(img, (x-10, y-10),
						(x + w+10, y + h+10),
						(255, 0, 0), 2)
			
			if barcode.data!="":
				barcodeNum = barcode.data
				barcodeType = barcode.type
			else:
				isBarcode = False
	

	lib = {
		'isBarcode': isBarcode,
		'barcodeNum': barcodeNum,
	}

	return lib

	"""			
	#Display the image
	cv2.imshow("Image", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == "__main__":
# Take the image from user
	image="Img.jpg"
	BarcodeReader(image)
  """
