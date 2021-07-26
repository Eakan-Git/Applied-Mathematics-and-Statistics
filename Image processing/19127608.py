import numpy as np
from PIL import Image

def adjust_brightness():
	input_file = "meo.jpg"
	image = Image.open(input_file)
	image = np.array(image)
	print("Adjusting brightness on " + input_file)
	value = input("Enter number to adjust brightness: ")
	value = np.clip(float(value), -255, 255)
	result =  np.uint8(np.clip(image + np.array([value], dtype = np.int16), 0, 255))
	output_file = "brightness_" + str(int(value)) + ".jpg"
	Image.fromarray(result).save(output_file)
	print("Output result to " + output_file)

def adjust_contrast():
	input_file = "meo.jpg"
	image = Image.open(input_file)
	image = np.array(image)
	print("Adjusting contrast on " + input_file)
	value = input("Enter number to adjust contrast: ")
	value = np.clip(float(value), -255, 255)
	factor = (259 * (value + 255)) / (255 * (259 - value))
	result =  np.uint8(np.clip(128 + factor * (image.astype(float) - 128), 0, 255))
	output_file = "contrast_" + str(int(value)) + ".jpg"
	Image.fromarray(result).save(output_file)
	print("Output result to " + output_file)

def change_to_grayscale():
	input_file = "meo.jpg"
	image = Image.open(input_file)
	image = np.array(image)
	print("Changing " + input_file + " to grayscale.")
	weight = [0.299, 0.587, 0.114] #CCIR 601 luma format
	result =  np.uint8(np.dot(image[..., :3], weight))
	output_file = "grayscaled.jpg"
	Image.fromarray(result).save(output_file)
	print("Output result to " + output_file)

def flip():
	input_file = "meo.jpg"
	image = Image.open(input_file)
	image = np.array(image)
	print("Flip on " + input_file)
	left_right = image[:, ::-1, :] #reverse rows
	up_down = image[::-1] #reverse columns
	output_file = "flipped_left_right.jpg"
	Image.fromarray(left_right).save(output_file)
	print("Output result to " + output_file)
	output_file = "flipped_up_down.jpg"
	Image.fromarray(up_down).save(output_file)
	print("Output result to " + output_file)

def blend_images(): #only grayscaled images
	input_file = "to_blend_1.jpg"
	image_1 = Image.open(input_file)
	image_1 = np.array(image_1.resize((200, 200))) #resize to the same

	input_file = "to_blend_2.jpg"
	image_2 = Image.open(input_file)	
	image_2 = np.array(image_2.resize((200, 200))) #resize to the same
	print("Blending images")
	alpha = 0.5
	result = (image_1 * (1.0 - alpha) + image_2 * alpha).astype('uint8')
	output_file = "blended_image_" + str(alpha) + ".jpg"
	Image.fromarray(result).save(output_file)
	print("Output result to " + output_file)


def gauss(x, sigma):
	return np.array(1 / (np.sqrt(2 * np.pi) * sigma) * (np.exp(-np.power(x / sigma, 2) / 2)))\

def guass_kernel(size, sigma):
	dimension_1d = np.linspace(-(size // 2), size // 2, num = size)
	dimension_1d = gauss(dimension_1d, sigma)
	dimension_2d = np.outer(dimension_1d.T, dimension_1d.T)
	dimension_2d *= 1.0 / np.sum(dimension_2d)
	return dimension_2d

def convole_layer(layer, kernel):
	view = kernel.shape + tuple(np.subtract(layer.shape, kernel.shape) + 1)
	submatrices = np.lib.stride_tricks.as_strided(layer, shape = view, strides = layer.strides * 2)
	return np.einsum('ij,ijkl->kl', kernel, submatrices)

def convolution(image, kernel):
	return np.dstack((convole_layer(image[:, :, 0], kernel), convole_layer(image[:, :, 1], kernel), convole_layer(image[:, :, 2], kernel)))

def blur():
	value = 33
	input_file = "meo.jpg"
	image = Image.open(input_file)
	image = np.array(image)
	print("Blur on " + input_file + " please wait...")
	kernel = guass_kernel(value, sigma = (value - 1) / 6)
	result = np.uint8(convolution(image, kernel))
	output_file = "blurred_image_" + str(value) + ".jpg"
	Image.fromarray(result).save(output_file)
	print("Output result to " + output_file)

#main
adjust_brightness()
print()
adjust_contrast()
print()
change_to_grayscale()
print()
flip()
print()
blend_images()
print()
blur()