import cv2
import numpy as np


def accumulator(img,edges):
    acc= np.zeros((img.shape[0]+img.shape[1]+1,180))
    edgeimg=np.nonzero(edges)
    for i in range(0,len(edgeimg[0])):
        x=edgeimg[0][i]
        y=edgeimg[1][i]
        for theta in range(0,180):
            rho = round(x * np.cos(theta) + y * np.sin(theta))
            acc[rho,theta]+=1
    return acc


def find_local_maxima(img, edges, threshold, neighborhood_size):
    maxima = []
    acc= accumulator(img, edges)
    height, width = acc.shape

    for i in range(height):
        for j in range(width):
            if acc[i, j] >= threshold:
                is_local_max = True

                # Sprawdź wartości sąsiadujące
                for di in range(-neighborhood_size, neighborhood_size + 1):
                    for dj in range(-neighborhood_size, neighborhood_size + 1):
                        ni, nj = i + di, j + dj
                        if (ni != i or nj != j) and ni >= 0 and ni < height and nj >= 0 and nj < width:
                            if acc[i, j] < acc[ni, nj]:
                                is_local_max = False
                                break

                    if not is_local_max:
                        break

                if is_local_max:
                    maxima.append((i, j))

    return acc,maxima


def find_lines(img,edges, threshold=150,neighborhood_size= 100):
    acc,maxima = find_local_maxima(img,edges,threshold,neighborhood_size)
    lines=[]
    for peak in maxima:
        x1=peak[0]
        x2=peak[1]
        a=np.cos(peak[1])
        b=np.sin(peak[1])
        if b>0:
            m=-a/b
            c=peak[0]/b
            # Wygeneruj punkty na linii
            x1 = 0
            y1 = int(m * x1 + c)
            x2 = img.shape[0]
            y2 = int(m * x2 + c)
        else:
            # Linia prawie pionowa, x = rho
            x = int(peak[0])
            y1 = 0
            y2 = img.shape[1]

        lines.append(((x1,y1),(x2,y2)))
    return lines

def printlines(img,lines):
    image_with_lines = np.copy(img)
    for line in lines:
        pt1, pt2 = line
        cv2.line(image_with_lines, pt1, pt2, (0, 0, 255), 2)  # Rysowanie linii na obrazie
    cv2.imshow('Lines', image_with_lines)
    cv2.waitKey(0)
    cv2.destroyAllWindows()