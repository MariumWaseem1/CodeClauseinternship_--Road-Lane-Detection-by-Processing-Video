# Lane Detection System

This project detects lane lines in road videos using basic computer vision techniques. It processes each video frame to identify and overlay detected lane markings.

## Features

\- Converts frames to grayscale and applies Gaussian blur  
\- Detects edges using the Canny edge detector  
\- Applies a mask to focus on the region of interest  
\- Uses Hough Line Transform to detect lane lines  
\- Overlays lane lines on the original video frame  
\- Displays processed video in real-time  

## How It Works

1. Convert the video frame to grayscale  
2. Apply Gaussian blur to reduce noise  
3. Detect edges using the Canny edge detector  
4. Define a triangular region of interest to isolate lane lines  
5. Apply Hough Line Transform to find line segments  
6. Draw the lines on a blank canvas and blend with the original frame  

## Requirements

\- Python 3  
\- OpenCV  
\- NumPy  



