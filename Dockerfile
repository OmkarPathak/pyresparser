FROM ubuntu:latest

RUN apt-get update 

RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip

WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY resumes resumes

# FROM 

# # Update aptitude with new repo


# #Labels as key value pair


# # Any working directory can be chosen as per choice like '/' or '/home' etc
# # i have chosen /usr/app/src
# WORKDIR /app


# # Now the structure looks like this '/usr/app/src/test.py'

# #to COPY the remote file at working directory in container
# # COPY . .

# #CMD instruction should be used to run the software
# #contained by your image, along with any arguments.

# # CMD [ "python", "./test.py"]