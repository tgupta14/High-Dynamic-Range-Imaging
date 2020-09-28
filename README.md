# High-Dynamic-Range-Imaging-
 Implementation of the basic algorithm for high dynamic range imaging by combining a stack of frames at different exposure settings.
 
 Each file is for an exposure taken with the exposure length set at
 t<sub>k</sub> = (1/2048)*2<sup>k−1</sup> where k varies from 1 to 16

The final High Dynamic Range frame is calculated using the following formula:

![Capture](https://user-images.githubusercontent.com/63022731/94486289-0e33de80-0194-11eb-935d-cda60f7eaea3.JPG)


To display the image, the tonemapping I = I<sub>HDR</sub>/(1 + I<sub>HDR</sub>) is used, and the image is saved as “HDR_phototonemap.png”
