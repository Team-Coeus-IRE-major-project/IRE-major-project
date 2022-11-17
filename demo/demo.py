import sys
import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import (
    AutoConfig,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    DataCollatorForSeq2Seq,
    HfArgumentParser,
    MBart50Tokenizer,
    MBart50TokenizerFast,
    MBartTokenizer,
    MBartTokenizerFast,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    set_seed,
)
from transformers.trainer_utils import get_last_checkpoint
check_point_path = "checkpoint"



def get_summary(summary):
    tokenizer = AutoTokenizer.from_pretrained(check_point_path+"/")
    model = AutoModelForSeq2SeqLM.from_pretrained(check_point_path)
    input_ids = tokenizer(f"summarize: {summary}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    tagline = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return tagline


def load_summary(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines[0]

if __name__ == '__main__':

    # Gradio interface
    
    demo = gr.Interface(
    fn=get_summary,
    inputs=["text"],
    outputs=["text"],
    )
    demo.launch()

    # Terminal Interface
    # if len(sys.argv) == 2:

    #     context = load_summary(sys.argv[1])
    #     tagline = get_summary(context)
    #     print("Tagline for the given summary is as follows:\n")
    #     print(tagline)
    # else:
    #     print("Please provide text file path containing summary as an argument")
