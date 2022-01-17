from math import log10, sqrt
import cv2
import numpy as np
def PSNR(original, compressed):
  mse = np.mean((original - compressed) **2) 
  if(mse == 0): # MSE is zero means no noise is present in the signal .
# Therefore PSNR have no importance.
    return 100
  max_pixel = 255.0
  psnr = 20 * log10(max_pixel / sqrt(mse))
  return psnr


#----------------------
import cv2
import numpy as np
import matplotlib.pyplot as plt  

path = "noisy_kitty55.png"

img = cv2.imread(path,0)
#----------------
F = np.fft.fft2(img)
FShift = np.fft.fftshift(F)
magnitude_spectrum = np.log(1+np.abs(FShift))

plt.imshow(img,cmap='gray')
plt.show()
#----------------
# nx, ny = img.shape
# y = np.linspace(-nx/2,nx/2,nx)
# x = np.linspace(-ny/2,ny/2,ny)
# xv, yv = np.meshgrid(x,y) 
# radiusCoor = np.sqrt(xv**2 + yv**2)
# r1 = radiusCoor < 50
# r2 = radiusCoor >= 65
# mask1 = np.ones([nx,ny])
# bandReject = cv2.bitwise_or(r1.astype(np.uint8),r2.astype(np.uint8),mask=mask1.astype(np.uint8))
# plt.imshow(bandReject,cmap='gray')
# plt.show()
# img_bandReject = bandReject * FShift
# img_ft_filter_hp_spectrum = np.log(1+np.abs(img_bandReject))
# plt.imshow(img_ft_filter_hp_spectrum)
# plt.show()
# f_ishift_br = np.fft.ifftshift(img_bandReject)
# img_restored = np.fft.ifft2(f_ishift_br)
# img_restored = np.abs(img_restored)

# plt.imshow(img_restored,cmap='gray')
# plt.show()
# 
#----------------
print("-----------------------------------------------")
im_notchFilter = FShift.copy()
im_notchFilter[100:130,:]= 0 #top left
im_notchFilter[:,100:120]= 0 #top left,105:115]= 0 #top left
im_notchFilter[370:400,:]= 0 #bottom right
im_notchFilter[:,370:400]= 0 #bottom right

img_ft_filter_nf_spectrum = np.log(1+np.abs(im_notchFilter))
f_ishift_nf = np.fft.ifftshift(im_notchFilter)
img_restored = np.fft.ifft2(f_ishift_nf)
img_restored = np.abs(img_restored)

plt.imshow(img_ft_filter_nf_spectrum)
plt.show()


plt.imshow(img_restored,cmap='gray')
plt.show()

kt55 = cv2.imread("kitty55.png",0)

print(PSNR(kt55,img))
print(PSNR(kt55,img_restored))