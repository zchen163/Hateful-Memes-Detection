#!/bin/bash
export OC_DISABLE_DOT_ACCESS_WARNING=1

mmf_run config="projects/visual_bert/configs/hateful_memes/from_coco.yaml" \
        model="visual_bert" \
        dataset=hateful_memes \
        run_type=train_val \
        checkpoint.max_to_keep=1 \
        checkpoint.resume_zoo=visual_bert.pretrained.cc.full \
        training.tensorboard=True \
        training.checkpoint_interval=500 \
        training.evaluation_interval=500 \
        training.max_updates=8500 \
        training.log_interval=500 \
        dataset_config.hateful_memes.annotations.train[0]=hateful_memes/defaults/annotations/train.jsonl \
        dataset_config.hateful_memes.annotations.val[0]=hateful_memes/defaults/annotations/dev_unseen.jsonl \
        dataset_config.hateful_memes.annotations.test[0]=hateful_memes/defaults/annotations/test_unseen.jsonl \
        dataset_config.hateful_memes.features.train[0]=$3 \
        dataset_config.hateful_memes.features.val[0]=$3 \
        dataset_config.hateful_memes.features.test[0]=$3 \
        optimizer.params.lr=$4 \
      	training.batch_size=$2 \
        env.tensorboard_logdir=logs/fit/$1 \
        env.save_dir=./$1 \
