from PIL import Image, ImageDraw, ImageFont

width, height = 400, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

draw.polygon([(50, 50), (200, 50), (125, 10)], fill="red")

draw.rectangle([(50, 50), (200, 250)], fill="blue")

draw.rectangle([(20, 250), (230, 260)], fill="brown")

font = ImageFont.load_default()
text = "HOUSE"
text_width, text_height = draw.textsize(text, font)
text_position = ((width - text_width) // 2, height - text_height - 10)

text_image = Image.new("RGB", (text_width, text_height), "white")
text_draw = ImageDraw.Draw(text_image)
text_draw.text((0, 0), text, fill="black", font=font)

rotated_text = text_image.rotate(180, expand=True)

image.paste(rotated_text, text_position)

image.save("house.png")

image.show()
