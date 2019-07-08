mkdir -p data
cd data
wget http://www.robots.ox.ac.uk/~vgg/data/text/mjsynth.tar.gz
cd ..
mkdir -p data/images
# strip leading mnt/ramdisk/max/90kDICT32px/
tar xzvf data/mjsynth.tar.gz --strip=4 -C data/images
cd tools
# use python 2
python create_lmdb_dataset_mjsynth.py