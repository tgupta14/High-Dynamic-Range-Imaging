# High-Dynamic-Range-Imaging
Implementation of the basic algorithm for high dynamic range imaging by combining a stack of frames at different exposure settings.
 
Each file is for an exposure taken with the exposure length set at t<sub>k</sub> = (1/2048)*2<sup>k−1</sup> where k varies from 1 to 16.

Folder named "Input Images" contain the 16 low dynamic range raw images in the .nef file format. The code first processes these raw image files to do color balancing, and all ISP operations except gamma compression and auto-brightness. These processed images are saved in the folder "Processed Images"

The final High Dynamic Range image is calculated using the following formula:

![tempsnip](https://user-images.githubusercontent.com/63022731/94486869-e1cc9200-0194-11eb-92cc-d8ad3abf32dc.jpg)


To display the image, the tonemapping I = I<sub>HDR</sub>/(1 + I<sub>HDR</sub>) is used, and the image is saved as “HDR_phototonemap.png”. Built-in Drago and Reinhard tonemapping is also done. The final HDR files are stored in "Output Images"

Sample Low Dynamic Range images (They have been converted to JPG from NEF to upload here):

![exposure9](https://user-images.githubusercontent.com/63022731/94489400-3a059300-0199-11eb-8918-5e35debe5b74.jpg)
![exposure15](https://user-images.githubusercontent.com/63022731/94489398-383bcf80-0199-11eb-878f-0aba79a285b8.jpg)


The final HDR Image will look like this:

![HDR_Reinhard](https://user-images.githubusercontent.com/63022731/94488864-489f7a80-0198-11eb-85f5-b863ee5f06e3.jpg)
