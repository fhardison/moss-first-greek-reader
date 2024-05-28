convert -density 300 $1 -type Grayscale -compress lzw -background white +matte -depth 8 page_%05d.tif
