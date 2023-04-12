close all;
clear;

img = imread("twocats_gray.bmp");
figure
imshow(img);
title("original")
%create blank array filled with 1
blank = ones(5)/25;
%mean filttering
outmean = imfilter(img,blank,'conv');
%median filtering
outmedian = medfilt2(img,[3 3]);

figure
imshow(outmean)
title("mean filter")

figure
imshow(outmedian)
title("median filter")

%gaussian filtering
gaussian = fspecial('gaussian', [5 5], 0.1);
outgaussian = imfilter(img, gaussian);

figure
imshow(outgaussian);
title("gaussian filter")