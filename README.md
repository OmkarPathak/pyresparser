# pyresparser
A simple resume parser used for extracting information from resumes

# Features

- Extract name
- Extract email
- Extract mobile numbers
- Extract skills
- Extract total experience
- Extract education (not very accurate as of now)
- Extract experience (not very accurate as of now)

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

- For extracting other supporting dependencies, execute:

```bash
# If you want to parse .docx and .pdf files (all OS supported)
pip install -r resume_parser/requirements.txt

# If you want to parse .docx, .doc and .pdf files (Ubuntu and OSX supported)
pip install -r resume_parser/requirements_with_textract.txt
```

- Run `pyresparser -f <resume_file_path>`

# CLI

For running the resume extractor you can also use the `cli` provided

```bash
usage: pyresparser [-h] [-f FILE] [-d DIRECTORY]

optional arguments:
  -h, --help                              show this help message and exit
  -f FILE, --file FILE                    resume file to be extracted
  -d DIRECTORY, --directory DIRECTORY     directory containing all the resumes to be extracted
  -r REMOTEFILE, --remotefile REMOTEFILE  remote path for resume file to be extracted
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

# Notes:

- If you are running the app on windows, then you can only extract .docs and .pdf files

# Result

The module would return a list of dictionary objects with result as follows:

```
[{'education': [('BE', '2014')],
  'email': 'omkarpathak27@gmail.com',
  'experience': [' Schlumberger DATA ENGINEER Pune'],
  'mobile_number': '8087996634',
  'name': 'Omkar Pathak',
  'no_of_pages': 3,
  'skills': ['Python',
             'C',
             'Technical',
             'Linux',
             'Machine learning',
             'System',
             'Html',
             'C++',
             'Security',
             'Testing',
             'Content',
             'Apis',
             'Engineering',
             'Payments',
             'Django',
             'Excel',
             'Admissions',
             'Mysql',
             'Windows',
             'Automation',
             'Opencv',
             'Website',
             'Css',
             'Js',
             'Algorithms',
             'Flask',
             'Programming',
             'Writing',
             'Training',
             'Php',
             'Reports',
             'Photography',
             'Open source',
             'Github',
             'Analytics',
             'Api'],
  'total_experience': 0.58}]
```

# References that helped me get here

- [https://www.kaggle.com/nirant/hitchhiker-s-guide-to-nlp-in-spacy](https://www.kaggle.com/nirant/hitchhiker-s-guide-to-nlp-in-spacy)

- [https://www.analyticsvidhya.com/blog/2017/04/natural-language-processing-made-easy-using-spacy-%E2%80%8Bin-python/](https://www.analyticsvidhya.com/blog/2017/04/natural-language-processing-made-easy-using-spacy-%E2%80%8Bin-python/)

- [https://medium.com/@divalicious.priya/information-extraction-from-cv-acec216c3f48](https://medium.com/@divalicious.priya/information-extraction-from-cv-acec216c3f48)

### Built with ♥ and :coffee: by [`Omkar Pathak`](http://www.omkarpathak.in/)

# Donation

If you have found my softwares to be of any use to you, do consider helping me pay my internet bills. This would encourage me to create many such softwares :)

| PayPal | <a href="https://paypal.me/omkarpathak27" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg" alt="Donate via PayPal!" title="Donate via PayPal!" /></a> |
|:-------------------------------------------:|:-------------------------------------------------------------:|
| ₹ (INR)  | <a href="https://www.instamojo.com/@omkarpathak/" target="_blank"><img src="https://www.soldermall.com/images/pic-online-payment.jpg" alt="Donate via Instamojo" title="Donate via instamojo" /></a> |
