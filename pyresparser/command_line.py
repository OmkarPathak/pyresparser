# Author: Omkar Pathak

import os
import argparse
from pprint import pprint
import io
import csv
import multiprocessing as mp
from urllib.request import Request, urlopen
from pyresparser import ResumeParser
from itertools import product

def print_cyan(text):
    print("\033[96m {}\033[00m" .format(text))

class ResumeParserCli(object):
    def __init__(self):     
        self.__parser = argparse.ArgumentParser()
        self.__parser.add_argument('-f', '--file', help="resume file to be extracted")
        self.__parser.add_argument('-d', '--directory', help="directory containing all the resumes to be extracted")
        self.__parser.add_argument('-r', '--remotefile', help="remote path for resume file to be extracted")
        self.__parser.add_argument('-sf', '--skillsfile', help="custom skills CSV file against which skills are searched for")

    def extract_resume_data(self):
        args = self.__parser.parse_args()

        if args.remotefile:
            return self.__extract_from_remote_file(args.remotefile)
        if args.file and not args.directory:
            if args.skillsfile:
                return self.__extract_from_file(args.file, args.skillsfile)
            else:
                return self.__extract_from_file(args.file)
        elif args.directory and not args.file:
            if args.skillsfile:
                return self.__extract_from_directory(args.directory, args.skillsfile)
            else:
                return self.__extract_from_directory(args.directory)
        else:
            self.__parser.print_help()

    def __extract_from_file(self, file, skills_file=None):
        if os.path.exists(file):
            print_cyan('Extracting data from: {}'.format(file))
            if skills_file:
                resume_parser = ResumeParser(file, skills_file)
            else:
                resume_parser = ResumeParser(file)
            return [resume_parser.get_extracted_data()]
        else:
            return 'File not found. Please provide a valid file name.'

    def __extract_from_directory(self, directory, skills_file=None):
        if os.path.exists(directory):
            pool = mp.Pool(mp.cpu_count())

            resumes = []
            for root, _, filenames in os.walk(directory):
                for filename in filenames:
                    file = os.path.join(root, filename)
                    if skills_file:
                        resumes.append([file, skills_file])
                    else:
                        resumes.append(file)
            results = pool.map(resume_result_wrapper, resumes)
            pool.close()
            pool.join()

            return results
        else:
            return 'Directory not found. Please provide a valid directory.'

    def __extract_from_remote_file(self, remote_file):
        print_cyan('Extracting data from: {}'.format(remote_file))
        req = Request(remote_file, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        _file = io.BytesIO(webpage)
        _file.name = remote_file.split('/')[-1]
        resume_parser = ResumeParser(_file)
        return [resume_parser.get_extracted_data()]

def resume_result_wrapper(args):
    if len(args) == 2:
        print_cyan('Extracting data from: {}'.format(args[0]))
        parser = ResumeParser(args[0], args[1])
    else:
        print_cyan('Extracting data from: {}'.format(args))
        parser = ResumeParser(args)
    return parser.get_extracted_data()

def main():
    cli_obj = ResumeParserCli()
    pprint(cli_obj.extract_resume_data())
