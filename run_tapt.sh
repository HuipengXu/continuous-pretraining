export CUDA_VISIBLE_DEVICES=0
python -m scripts.run_language_modeling \
  --train_data_file ./multi-task-data/train_input.txt \
  --line_by_line \
  --output_dir bert-base-dapt \
  --model_type bert \
  --tokenizer_name ./multi-task-data/bert-base-chinese \
  --config_name ./multi-task-data/bert-base-chinese/config.json \
  --mlm \
  --per_gpu_train_batch_size 8 \
  --gradient_accumulation_steps 16 \
  --model_name_or_path ./multi-task-data/bert-base-chinese \
  --eval_data_file ./multi-task-data/dev_input.txt \
  --do_eval \
  --evaluate_during_training \
  --do_train \
  --num_train_epochs 2 \
  --learning_rate 0.0005 \
  --logging_steps 100 \
  --overwrite_output_dir


#python -m scripts.run_language_modeling \
#  --train_data_file ./multi-task-data/debug_train_input.txt \
#  --line_by_line \
#  --output_dir bert-base-tapt \
#  --model_type bert \
#  --tokenizer_name ./multi-task-data/bert-base-chinese \
#  --config_name ./multi-task-data/bert-base-chinese/config.json \
#  --mlm \
#  --per_gpu_train_batch_size 8 \
#  --gradient_accumulation_steps 1 \
#  --model_name_or_path ./multi-task-data/bert-base-chinese \
#  --eval_data_file ./multi-task-data/debug_dev_input.txt \
#  --do_eval \
#  --evaluate_during_training \
#  --do_train \
#  --num_train_epochs 5 \
#  --learning_rate 0.0001 \
#  --logging_steps 20 \
#  --overwrite_output_dir