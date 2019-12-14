# CLI

`pyresparser` comes with a **cli** option which you can use right away in your terminal

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

## Parsing single resume

For extracting data from a **single resume** file, use

```bash
pyresparser -f /path/to/resume/file
```

## Parsing mutliple resumes

For extracting data from several resumes, place them in a **directory** and then execute

```bash
pyresparser -d /path/to/resume/directory/
```

## Parsing hosted resumes

For extracting data from **remote resumes**, execute

```bash
pyresparser -r https://www.example.com/path/to/resume/file
```

## Specifying skills explicitly

Pyresparser comes with built-in skills file that defaults to many technical skills. You can find the default skills file [here](https://github.com/OmkarPathak/pyresparser/blob/master/pyresparser/skills.csv).

For extracting data against your specified skills, create a CSV file with no headers and execute

```bash
pyresparser -sf /path/to/resume/file.csv -f /path/to/resume/file
```

## Specifying export format

For specifying the export format you can use the following option:

```bash
pyresparser -e json -f /path/to/resume/file
```

Note: Currently only JSON export is supported

## Custom regex for parsing phone numbers

While pyresparser parses most of the phone numbers correctly, there is a possibility of new patterns being added in near future. Hence, we can explicitly provide the regex required to parse the desired phone numbers. This can be done using

```bash
pyresparser -re '<pattern>' -f /path/to/resume/file
```