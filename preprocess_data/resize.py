import os
import cv2

def main(base_dir="./", img_path="imgs"):
    imgs_dir = os.path.join(base_dir, img_path)
    imgs_path = [os.path.join(imgs_dir, img) for img in sorted(os.listdir(imgs_dir)) if ".jpg" in img or ".png" in img] 
    for n_order, img_path in enumerate(imgs_path):
        img = cv2.imread(img_path)
        H, W, _ = img.shape
        img = cv2.resize(img, tuple([2000, 2000]))
        cv2.imwrite(f"{imgs_dir}/{n_order}.png", img)
        print("Resized: ", img_path, "==>", f"{n_order}.png")
    pass

if __name__ == "__main__":
    main()