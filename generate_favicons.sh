#!/bin/bash

# Create favicon sizes from logo
convert assets/images/abbotsford-croquet-logo.png -resize 16x16 assets/images/favicon-16x16.png
convert assets/images/abbotsford-croquet-logo.png -resize 32x32 assets/images/favicon-32x32.png
convert assets/images/abbotsford-croquet-logo.png -resize 180x180 assets/images/apple-touch-icon.png
convert assets/images/abbotsford-croquet-logo.png -resize 192x192 assets/images/android-chrome-192x192.png
convert assets/images/abbotsford-croquet-logo.png -resize 512x512 assets/images/android-chrome-512x512.png

# Create .ico file
convert assets/images/favicon-16x16.png assets/images/favicon-32x32.png assets/images/favicon.ico 