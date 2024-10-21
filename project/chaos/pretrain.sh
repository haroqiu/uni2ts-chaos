#!/bin/bash

export CUDA_VISIBLE_DEVICES=0

python -m cli.train \
  -cp conf/pretrain \
  run_name=first_run \
  model=moirai_small \
  data=lotsa-chaost_unweighted