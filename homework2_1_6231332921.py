import cv2
import numpy as np
import matplotlib.pyplot as plt  

path = "kitty55.png"

img = cv2.imread(path,0)
plt.imshow(img, cmap = 'gray');
plt.title('Original'), plt.xticks([]), plt.yticks([]);plt.show()

# gau = cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT) 
# plt.imshow(gau, cmap = 'gray'), plt.xticks([]), plt.yticks([]);
# plt.title('Gaussian');plt.show()

c = 29 # cutoff freq.
n = 15 # order

nx, ny = img.shape
x = np.linspace(-nx/2, nx/2-1, nx)
y = np.linspace(-ny/2, ny/2-1, ny)
gau = np.zeros((nx,ny),dtype=np.float32)
for i in x.astype(np.int32):
  for j in y.astype(np.int32):
    gau[i+int(nx/2),j+int(ny/2)] = np.exp(-(i**2+j**2)/(2*pow(c,2.0)))
#--------------------------------------
f1 = np.fft.fft2(img)
fshift1 = np.fft.fftshift(f1)
magnitude_spectrum_original = np.log(1+np.abs(fshift1))
#--------------------------------------
img_ft_filter = fshift1 * gau
magnitude_spectrum_gauss = np.log(1+np.abs(img_ft_filter))
plt.imshow(magnitude_spectrum_gauss.astype(np.uint8), cmap = 'gray')
plt.xticks([]), plt.yticks([]);
plt.title('Gaussian');plt.show()

#--------------------------------------
# f2 = np.fft.fft2(img_ft_filter)
# fshift2 = np.fft.fftshift(f2)
# magnitude_spectrum_gauss = np.log(1+np.abs(fshift2))
fi = np.fft.ifftshift(img_ft_filter)
img_back = np.fft.ifft2(fi)
img_back = np.abs(img_back)

plt.imshow(magnitude_spectrum_original, cmap = 'gray'), plt.xticks([]), plt.yticks([]);
plt.title('magnitude_spectrum_original');plt.show()

plt.imshow(magnitude_spectrum_gauss, cmap = 'gray'), plt.xticks([]), plt.yticks([]);
plt.title('magnitude_spectrum_gauss');plt.show()

plt.imshow(img_back, cmap = 'gray'), plt.xticks([]), plt.yticks([]);
plt.title('image b');plt.show()

power_original = np.sum(np.abs(f1)**2)
power_gauss = np.sum(np.abs(img_ft_filter)**2)
ratio = (power_gauss/power_original)*100
print("ratio = ",ratio)

