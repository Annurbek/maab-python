##Task 1
import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])
vectorized_celsius = np.vectorize(fahrenheit_to_celsius)
temps_c = vectorized_celsius(temps_f)

##Task 2
def power_func(base, exp):
    return base ** exp

bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
vectorized_power = np.vectorize(power_func)
powers = vectorized_power(bases, exponents)

##Task 3
A1 = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])
b1 = np.array([7, 4, 5])
solution1 = np.linalg.solve(A1, b1)

##Task 4
A2 = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
b2 = np.array([12, -5, 15])
solution2 = np.linalg.solve(A2, b2)

##Task 5
from PIL import Image
import numpy as np

def load_image(path):
    return np.array(Image.open(path))

def save_image(array, path):
    Image.fromarray(array.astype(np.uint8)).save(path)

def flip_image(img):
    flipped_h = np.fliplr(img)
    flipped_v = np.flipud(img)
    return flipped_h, flipped_v

def add_noise(img):
    noise = np.random.randint(0, 50, img.shape, dtype='uint8')
    noisy_img = np.clip(img + noise, 0, 255)
    return noisy_img

def brighten_channels(img, value=40):
    brightened = np.clip(img + value, 0, 255)
    return brightened

def apply_mask(img):
    h, w = img.shape[:2]
    masked = img.copy()
    cx, cy = w // 2, h // 2
    masked[cy-50:cy+50, cx-50:cx+50] = [0, 0, 0]
    return masked

# === Main ===
img_path = 'images/birds.jpg'
img = load_image(img_path)

flipped_h, flipped_v = flip_image(img)
save_image(flipped_h, 'flipped_horizontal.jpg')
save_image(flipped_v, 'flipped_vertical.jpg')

noisy = add_noise(img)
save_image(noisy, 'noisy.jpg')

bright = brighten_channels(img, 40)
save_image(bright, 'brightened.jpg')

masked = apply_mask(img)
save_image(masked, 'masked.jpg')
