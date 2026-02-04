from PIL import Image

r_source = Image.open('red_channel.jpg').convert('L') 
g_source = Image.open('green_channel.jpg').convert('L')
b_source = Image.open('blue_channel.jpg').convert('L')

width, height = r_source.size

r_shifted = r_source.crop((50, 0, width, height))
r_center = r_source.crop((25, 0, width - 25, height))
r_final = Image.blend(r_shifted, r_center, 0.5)

b_shifted = b_source.crop((0, 0, width - 50, height))
b_center  = b_source.crop((25, 0, width - 25, height))
b_final = Image.blend(b_shifted, b_center, 0.5)

g_final = g_source.crop((25, 0, width - 25, height))

result_005 = Image.merge("RGB", (r_final, g_final, b_final))
result_005.save("result_005.jpg")

image = Image.open("result_005.jpg")
image.thumbnail((80, 70))
image.save('result_thumb.jpg')

