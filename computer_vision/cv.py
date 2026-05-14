import cv2
import matplotlib.pyplot as plt

img = cv2.imshow("color.jpg")

# Check if image loaded
if img is None:
    print("Error: Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img, (25,25),8)
    edges = cv2.Canny(img, 100, 200)

    # Convert BGR → RGB (important!)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    blur_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)


    # Display images
    plt.figure(figsize=(10,8))

    plt.subplot(2,2,1)
    plt.imshow(img_rgb)
    plt.title("Original")

    plt.subplot(2,2,2)
    plt.imshow(gray, cmap='gray')
    plt.title("Gray")

    plt.subplot(2,2,3)
    plt.imshow(blur_rgb)
    plt.title("Blur")

    plt.subplot(2,2,4)
    plt.imshow(edges, cmap='gray')
    plt.title("Edges")

    plt.show()
