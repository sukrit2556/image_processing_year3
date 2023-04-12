close all;
clear all;
clc;

image8 = imread("lifting_gray.bmp");
imshow(image8);
title("8-bits image");

[r,c] = size(image8);

for i = 1:r
    for j=1:c
        f = image8(i,j);
        if f <= 32
            image8(i,j) = 32;
        elseif f <= 64
            image8(i,j) = 64;
        elseif f <= 96
            image8(i,j) = 96;
        elseif f <= 128
            image8(i,j) = 128;
        elseif f <= 160
            image8(i,j) = 160;
        elseif f <= 192
            image8(i,j) = 192;
        elseif f <= 224
            image8(i,j) = 224;
        elseif f <= 256
            image8(i,j) = 256;
        end
    end
end
figure,imshow(image8);
title("after")