import os
import argparse
from pprint import pprint
import io
import multiprocessing as mp
import urllib
from urllib.request import Request, urlopen
from pyresparser import ResumeParser

def get_remote_data():
    try:
        remote_file = 'https://www.omkarpathak.in/downloads/OmkarResume.pdf'
        print('Extracting data from: {}'.format(remote_file))
        req = Request(remote_file, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        _file = io.BytesIO(webpage)
        _file.name = remote_file.split('/')[-1]
        resume_parser = ResumeParser(_file)
        return [resume_parser.get_extracted_data()]
    except urllib.error.HTTPError:
        return 'File not found. Please provide correct URL for resume file.'

def get_local_data():
    data = ResumeParser('OmkarResume.pdf').get_extracted_data()
    return data

def test_remote_name():
    data = get_remote_data()
    assert 'Omkar Pathak' == data[0]['name']

def test_remote_phone_number():
    data = get_remote_data()
    assert '8087996634' == data[0]['mobile_number']

def test_local_skills():
    data = get_local_data()
    assert 'C++' in data['skills']

def test_local_phone_number():
    data = get_local_data()
    assert '8087996634' == data['mobile_number']

def test_extract_string():

    string = (f"Joe Bloggs email: joe.bloggs@test.com \n"
              f"Professional Experience \n"
              f"Microsoft \n Jan 2017 - Mar 2020 \n"
              f"Analyst \n"
              f"Created monthly Excel and Powerpoint reports highlighting KPIs in a clear and simple format. \n"
              f"Used predictive modelling to detect patterns in customer behaviour using Python. \n"
              f"Education \n"
              f"University of Oxford \n"
              f"BSc in Computer Science \n")

    data = ResumeParser(string).get_extracted_data()
    assert 'Excel' in data['skills']
