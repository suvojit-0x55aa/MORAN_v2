GPU=0
CUDA_VISIBLE_DEVICES=${GPU} \
python main.py \
	--train_nips '/home/ubuntu/MORAN_v2/data/train' \
	--train_cvpr 'path_to_dataset' \
	--valroot '/home/ubuntu/MORAN_v2/data/val' \
	--workers 2 \
	--batchSize 64 \
	--niter 10 \
	--lr 1 \
	--cuda \
	--experiment output/ \
	--displayInterval 100 \
	--valInterval 1000 \
	--saveInterval 40000 \
	--adadelta \
	--BidirDecoder