from pyresparser.resume_parser import ResumeParser
from datetime import datetime
import sys
import csv
import os

result = []
fields = ['filename', 'name', 'email', 'mobile_number', 'skills', 'total_experience', 'experience']

for root, directories, filenames in os.walk(sys.argv[1]):
    for filename in filenames:
        file_name = os.path.join(root, filename)
        parser = ResumeParser(file_name)
        data = parser.get_extracted_data()
        name = data.get('name')
        email = data.get('email')
        mobile_number = data.get('mobile_number')
        skills = ', '.join(data.get('skills')) if data.get('skills') else []
        total_experience = str(data.get('total_experience'))
        experience = ' '.join(data.get('experience')) if data.get('experience') else []
        
        result.append(
            [
                file_name,
                name,
                email,
                mobile_number,
                skills, 
                total_experience,
                experience
            ]
        )

# writing to csv file
with open(datetime.today().strftime('%d-%B-%y.csv'), 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(result)
