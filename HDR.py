import cv2
import numpy as np
import rawpy

##### Converting the Raw exposure files to Processed Exposure files ######
for i in range(1,17):
    path = 'Input Images/'+'exposure'+str(i)+'.nef'
    name = 'processed_exposure'+str(i)+'.tiff'
    with rawpy.imread(path) as raw:
        rgb = raw.postprocess(gamma = (1,1),no_auto_bright = True, output_bps=16)
        bgr = cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
        cv2.imwrite('Processed Images/'+name,bgr)
################################################################
############ Computation for HDR image #########################
img = cv2.imread('Processed Images/processed_exposure1.tiff',-1) ## -1 for Reading the 16 bit image
size = img.shape 
w = np.zeros(size) ## Weight Matrix
n1 = np.zeros(size) ## Intermediate numerator matrix
n = np.zeros(size) ## numerator matrix
d = np.zeros(size) + 10**(-8) ## Denominator matrix adding a small value to avoid divison by zero

for i in range(1,17):
    name = 'Processed Images/processed_exposure'+str(i)+'.tiff'
    img = np.float32(cv2.imread(name,-1))/65535 ## Normalizing the image
    img[img>0.8] = 0 ## Valid Pixels
    img[img<0.05] = 0 ## Valid Pixels
    w = (np.exp(-4*((img-0.5)**2)/(0.5**2))) ## Weights
    w[w==np.exp(-4)] = 0 ## Weights for just valid pixels else = 0
    n1 = (w*img/(2**(i-12))) ## Img*weights
    n = n + n1 ## Weighted Sum
    d = d + w ## Sum of weights
    
i_hdr = (n/d) ## HDR image with out tone map

## Photo tone map with different fraction of additions in denominator
for i in range(1,11):
    i_tm = np.uint16(i_hdr*65535/((i*0.1)+i_hdr))
    cv2.imwrite('Output Images/HDR_phototonemap'+str(i)+'.png',i_tm)

###############################################################################
############# Inbuilt OpenCV tone mapping #####################################
## Drago Tonemap ##
tonemapDrago = cv2.createTonemapDrago(1.0,0.7) ## Setting gamma and saturation
ldrDrago = tonemapDrago.process(np.float32(i_hdr))
ldrDrago = 3*ldrDrago ## factor of 3 is by trail and error
cv2.imwrite('Output Images/HDR_Drago.png',ldrDrago*255)
## Reinhard Tonemap ##
## parameters - Gamma,intensity,light adapt,color adapt
tonemapReinhard = cv2.createTonemapReinhard(1.2,0.5,0,0) 
ldrReinhard = tonemapReinhard.process(np.float32(i_hdr))
cv2.imwrite("Output Images/HDR_Reinhard1.png", ldrReinhard*255)