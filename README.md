# pyresparser

```
A simple resume parser used for extracting information from resumes
```

Built with ❤︎ and :coffee: by  [Omkar Pathak](https://github.com/OmkarPathak)

---

[![GitHub stars](https://img.shields.io/github/stars/OmkarPathak/pyresparser.svg)](https://github.com/OmkarPathak/pyresparser/stargazers)
[![Downloads](https://pepy.tech/badge/pyresparser)](https://pepy.tech/project/pyresparser)
![Python](https://img.shields.io/badge/Python-3.7-brightgreen.svg)
[![GitHub](https://img.shields.io/github/license/omkarpathak/pyresparser.svg)](https://github.com/OmkarPathak/pyresparser/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg) [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-:D-1EAEDB.svg)](https://saythanks.io/to/OmkarPathak)

# Features

- Extract name
- Extract email
- Extract mobile numbers
- Extract skills
- Extract total experience
- Extract college name
- Extract degree
- Extract designation
- Extract company names

# Installation

- You can install this package using

```bash
pip install pyresparser
```

- For NLP operations we use spacy and nltk. Install them using below commands:

```bash
# spaCy
python -m spacy download en_core_web_sm

# nltk
python -m nltk.downloader words
```

# Supported File Formats

- PDF and DOCx files are supported on all Operating Systems
- If you want to extract DOC files you can install [textract](https://textract.readthedocs.io/en/stable/installation.html) for your OS (Linux, MacOS)
- Note: You just have to install textract (and nothing else) and doc files will get parsed easily

# Usage

- Import it in your Python project

```python
from pyresparser import ResumeParser
data = ResumeParser('/path/to/resume/file').get_extracted_data()
```

# CLI

For running the resume extractor you can also use the `cli` provided

```bash
usage: pyresparser [-h] [-f FILE] [-d DIRECTORY] [-r REMOTEFILE]
                   [-sf SKILLSFILE]

optional arguments:
  -h, --help                                show this help message and exit
  -f FILE, --file FILE                      resume file to be extracted
  -d DIRECTORY, --directory DIRECTORY       directory containing all the resumes to be extracted
  -r REMOTEFILE, --remotefile REMOTEFILE    remote path for resume file to be extracted
  -sf SKILLSFILE, --skillsfile SKILLSFILE   custom skills CSV file against which skills are searched for
```

For extracting data from a single resume file, use

```bash
pyresparser -f <resume_file_path>
```

For extracting data from several resumes, place them in a directory and then execute

```bash
pyresparser -d <resume_directory_path>
```

For extracting data from remote resumes, execute

```bash
pyresparser -r <path_to_remote_resume_file>
```

For extracting data against your specified skills, create a CSV file with no headers. Sample file can be found [here](pyresparser/skills.csv)

```bash
pyresparser -sf <path_to_custom_skills_file>
```

# Notes:

- If you are running the app on windows, then you can only extract .docs and .pdf files

# Result

The module would return a list of dictionary objects with result as follows:

```
[
  {
    'college_name': ['Marathwada Mitra Mandal’s College of Engineering'],
    'company_names': None,
    'degree': ['B.E. IN COMPUTER ENGINEERING'],
    'designation': ['Manager',
                    'TECHNICAL CONTENT WRITER',
                    'DATA ENGINEER'],
    'email': 'omkarpathak27@gmail.com',
    'mobile_number': '8087996634',
    'name': 'Omkar Pathak',
    'no_of_pages': 3,
    'skills': ['Operating systems',
              'Linux',
              'Github',
              'Testing',
              'Content',
              'Automation',
              'Python',
              'Css',
              'Website',
              'Django',
              'Opencv',
              'Programming',
              'C',
              ...],
    'total_experience': 1.83
  }
]
```

# References that helped me get here

- [https://www.kaggle.com/nirant/hitchhiker-s-guide-to-nlp-in-spacy](https://www.kaggle.com/nirant/hitchhiker-s-guide-to-nlp-in-spacy)

- [https://www.analyticsvidhya.com/blog/2017/04/natural-language-processing-made-easy-using-spacy-%E2%80%8Bin-python/](https://www.analyticsvidhya.com/blog/2017/04/natural-language-processing-made-easy-using-spacy-%E2%80%8Bin-python/)

- [https://medium.com/@divalicious.priya/information-extraction-from-cv-acec216c3f48](https://medium.com/@divalicious.priya/information-extraction-from-cv-acec216c3f48)

- **Special thanks** to dataturks for their [annotated dataset](https://dataturks.com/blog/named-entity-recognition-in-resumes.php)

# Donation

If you have found my softwares to be of any use to you, do consider helping me pay my internet bills. This would encourage me to create many such softwares :smile:

| PayPal | <a href="https://paypal.me/omkarpathak27" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg" alt="Donate via PayPal!" title="Donate via PayPal!" /></a> |
|:-------------------------------------------:|:-------------------------------------------------------------:|
| ₹ (INR)  | <a href="https://www.instamojo.com/@omkarpathak/" target="_blank"><img src="https://www.soldermall.com/images/pic-online-payment.jpg" alt="Donate via Instamojo" title="Donate via instamojo" /></a> |
