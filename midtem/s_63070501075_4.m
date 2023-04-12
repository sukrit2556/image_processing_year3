close all;
clear;
img = imread('lifting_gray.bmp');

%result1
%Negative Transformation
Image_Result1=256-1-img;
Result1=figure();
imshow(Image_Result1);
title("result1")

%result2
result2 = imadjust(lift,[0.45 0.7],[0.1 1]);
figure
imshow(result2);
title("result1")

%result3
%Logarithmic
r = double(img);
c = 255/log(1+255);
s = c * log(r+1);
result3 = uint8(s);
figure
imshow(result3);
title("result1")
