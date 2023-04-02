for i in page_*.tif; do echo $i; tesseract -l grc+eng $i $(basename $i .tif) txt; done
