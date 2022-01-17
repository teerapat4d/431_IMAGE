def arith(img1,img2) :
    img_div = cv2.divide(img1,img2)
    img_mul = cv2.multiply(img1,img2)
    img_add = cv2.add(img1,img2)
    img_sub = cv2.subtract(img1,img2)

    for i in [ img_add,img_sub,img_mul,img_div ] :
        s = cv2.split(i)
        colors = ("b", "g", "r")
        for (c, color) in zip(s, colors):
            hist = cv2.calcHist([c], [0], None, [256], [0, 256])
            plt.plot(hist, color=color)
            plt.xlim([0, 256])
        plt.show()