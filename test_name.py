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

def test_local_name():
    data = get_local_data()
    assert 'Omkar Pathak' == data['name']

def test_local_phone_number():
    data = get_local_data()
    assert '8087996634' == data['mobile_number']
