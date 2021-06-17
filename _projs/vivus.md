---
title: "vivus"
date: 2021-05-15
excerpt: "venous intra-vascular ultra-sound image processing through CNN<br/><img src='https://github.com/tuguldurs/vivus/blob/main/media/pullback.gif?raw=true' width='350'>"
collection: projs
permalink: /projs/2021/05/vivus/
---

<p align='center'>
<img src="https://raw.githubusercontent.com/tuguldurs/vivus/main/media/logo.png" alt="logo" width="250"/>
</p>

This is a freelance work I did for Dr. Breuer's lab at the Nationwide Children's Hospital in Columbus, OH. The overarching focus of their study is to develop artificial grafts that would eventually treat children who were born with various congenital defects. They explore grafts made from various materials (different types of polymers) and test them out in large animal models (e.g. sheep, monkey) to study their deformation and durability with time.

One of their primary tools for assessing the graft structure is intra-vascular ultrasound (IVUS). As the name implies, an ultrasound probe is literally inserted into the blood vessel to map out the interior structure. Like most places around the world they have been using commercial software to manually label the contours (mapping the interior wall(s) of the vessel), which introduces substantial amount of ambiguity and errors. Manual contours on the same exact image can significantly vary depending on the surgeon's experience, and the labels drawn even by the same person on the same image can differ quite a bit. Furthermore, manual contour annotation is very slow - it can take up to 10min just to process a single image. As a result, the ultrasound measurements were never fully utilized, and it was not possible to meaningfully compare its results to alternative approaches such as, MRI and Angiography.

<br/><img src='https://github.com/tuguldurs/vivus/blob/main/media/pullback.gif?raw=true' width='350'><br>

These problems are entirely solved by <code>vivus</code> ([GitHub](https://github.com/tuguldurs/vivus)) - a python code developed specifically to process venous IVUS images. It performs all the necessary image processing, and draws the contours based on models trained on convolutional neural networks (CNN), and a decision tree classifier. Preliminary performance results suggest a mean absolute error of <7% when compared to the areas of manual contours, and the accuracy of the classifier is 99% (with 100% precision). On cuda enabled devices a single image is processed in just a couple of seconds, which makes it possible to process 100-1000s of images in a short time and even build 3D volumetric models. The code is deployed at the Nationwide Children's Hospital and in collaboration with researchers at Dr. Beuer's lab we are preparing an article in a medical journal.
