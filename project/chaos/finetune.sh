export CUDA_VISIBLE_DEVICES=1

python -m cli.train \
  -cp conf/finetune \
  run_name=example_run \
  model=moirai_1.1_R_small \
  data=etth1 \
  val_data=etth1