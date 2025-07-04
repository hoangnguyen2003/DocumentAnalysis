# DocumentAnalysis

### Table of contents
* [Introduction](#star2-introduction)
* [Installation](#wrench-installation)
* [How to run](#zap-how-to-run) 
* [Contact](#raising_hand-questions)

## :star2: Introduction

* <p align="justify">Developed a Python tool to extract, summarize, and generate Q&A from a PDF document.</p>
* <p align="justify">Implemented PDF text extraction with PyMuPDF and text processing with NLTK.</p>
* <p align="justify">Utilized Hugging Face transformers (T5, RoBERTa) for summarization and question-answering.</p>
* <p align="justify">Applied passage splitting and duplicate question handling to improve output quality.</p>

![summary](/images/summary.PNG)
![qa](/images/qa.PNG)

Figure: *An example of a WHO document studying SARS-CoV-2*

## :wrench: Installation

<p align="justify">Step-by-step instructions to get you running DocumentAnalysis:</p>

### 1) Clone this repository to your local machine:

```bash
git clone https://github.com/hoangnguyen2003/DocumentAnalysis.git
```

A folder called `DocumentAnalysis` should appear.

### 2) Install the required packages:

Make sure that you have Anaconda installed. If not - follow this [miniconda installation](https://www.anaconda.com/docs/getting-started/miniconda/install).

<p align="justify">You can re-create our conda enviroment from `environment.yml` file:</p>

```bash
cd DocumentAnalysis
conda env create --file environment.yml
```

<p align="justify">Your conda should start downloading and extracting packages.</p>

### 3) Activate the environment:

Your environment should be called `DocumentAnalysis`, and you can activate it now to run the scripts:

```bash
conda activate DocumentAnalysis
```

## :zap: How to run 
<p align="justify">To summarize the document and generate Q&A:</p>

```bash
python main.py
```

You can choose a different document or model in `config/config.yaml`.

## :raising_hand: Questions
If you have any questions about the code, please contact Hoang Van Nguyen (hoangvnguyen2003@gmail.com) or open an issue.