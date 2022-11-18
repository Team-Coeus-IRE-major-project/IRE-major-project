# Abstractive Summarization

The data was fine-tuned on Bart-base and T5-small models.

## Fine-tuning Bart and T5

```
pip install -r requirements.txt
bash finetune.sh <basefolder> <modelname>
```

* basefolder: Location to store results and checkpoints. Should include the train, validation and test csv files containing `plot_synopsis` and `tagline` as the columns to fine-tune the data on.

* modelname: Should be a valid supported architecture (tested on `t5-small` and bart variants) available on huggingface's modelhub.

Test results will be generated at `<basefolder>/results.csv` and checkpoints will be found at `<basefolder>/checkpoints`.



## Fine-tuning GPT-2

GPT-2 is a general-purpose learner and requires a slightly different method of fine-tuning which is demonstrated in `gpt_finetuning.ipynb`. Note that running inference requires a session restart.

Checkpoints and results are found at [OneDrive](https://iiitaphyd-my.sharepoint.com/:f:/g/personal/abhishekh_sivakumar_students_iiit_ac_in/EgBXjzX3qKxOpsBSJb4WO3gBB1N2B_W9VPyXO-OSLVIlCw?e=uxFarx)

Results can be found at - [gdrive](https://drive.google.com/file/d/1pZO9mbsvkw6jacowyjsosPDCZbWkW6QP/view?usp=sharing)

