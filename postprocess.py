from PIL import Image

def read_image(file):
    img = Image.open(file)
    return img


def generate_linear_gradient(start, end, steps):
    # gradient will include start and end colors
    # length of gradient will be steps+1

    gradient = []
    diff = tuple(end[i] - start[i] for i in range(0, len(start)))
    for i in range(0, steps+1):
        gradient.append(tuple(int(start[j] + int(diff[j] * i/steps)) for j in range(0, len(start))))
    
    return gradient


im = read_image("generated/42a.png")
print(im.format, im.size, im.mode)

start_color = (0, 0, 0)
end_color = (0, 255, 0)


source = im.split()
R, G, B = 0, 1, 2
mask = source[G].point(lambda i: i > 0 and 255)
black = source[R].point(lambda i: i)
grad = source[G].point(lambda i: i)
source[R].paste(grad, None, mask)
source[G].paste(black, None, mask)
source[B].paste(grad, None, mask)

out = Image.merge(im.mode, source)
out.save("generated/42b.png")