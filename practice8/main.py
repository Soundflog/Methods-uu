from PIL import Image, ImageEnhance

im = Image.open("img.png")

constrast = ImageEnhance.Contrast(im)

alpha = 0.5
im_output = constrast.enhance(alpha)
im_output.save('less-contrast-image.png')

alpha = 1.5
im_output = constrast.enhance(alpha)
im_output.save('more-contrast-image.png')