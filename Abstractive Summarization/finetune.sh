base_folder=$1
train_file="$base_folder/train.csv"
val_file="$base_folder/val.csv"
test_file="$base_folder/test.csv"
dest_file="$base_folder/results.csv"
results_dir="$base_folder/results"
checkpoints_dir="$base_folder/checkpoints"

model=$2

prefix=""

if [[ "$model" == *"t5"* ]]; then
    echo "Attempting to fine-tune T5 variant"
    prefix="summarize: "
fi

python run_summarization.py \
    --model_name_or_path "$model" \
    --do_train \
    --train_file "$train_file" \
    --do_eval \
    --validation_file "$val_file" \
    --text_column plot_synopsis \
    --summary_column tagline \
    --source_prefix "$prefix" \
    --output_dir "$checkpoints_dir" \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --overwrite_output_dir \
    --predict_with_generate \
    --do_predict \
    --test_file "$test_file" \
    --output_dir "$results_dir"

python merge.py \
    --out_preds "$results_dir/generated_predictions.txt" \
    --test_file "$test_file" \
    --dest_file "$dest_file"

echo "results generated at $dest_file"

