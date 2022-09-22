# Aidan Sawyer

### Description ###

##### short #####
store and export information about my education, work experience, projects, and goals.

##### long #####
This repository is meant to act as both:
 - a central hub to store the data objects about my personal and professional career in one location.
 - a repeatable and simple way to generate PDF resumes without dealing with formatting hassles (allowing me to only update the json and run a command)
 - a simplified way to host/serve resume info and pdf download on [my site](http://aidan-sawyer.com).

### Content ###

As a "resume", the repository is meant to store information relevant to my work
  and career. Following the traditional divisions as well as those I found most
  desirable to my site, the information is stored as follows:

|file|description|
|:---|:---------------|
|experience.json|various jobs i've had over my career in a number of fields|
|education.json|formal schooling and certifications i've recieved|
|projects.json|various softare projects i've worked on over the years|
|additional.json|listing of languages, skills, interests, and links that didn't fit elsewhere|

### Interface ###

If you're just here to view the information stored in these `.json` files, a much more 
  pleasant way of doing so is available on my website at 
  [aidan-sawyer.com/](http://aidan-sawyer.com/).

### How to Use ###

#### Getting Started

Clone the repository or download the zip from the master branch
```
$ cd ~/your/projects/folder
$ git clone https://github.com/atla5/resume.git
```

This project runs on `python` 2.6 - 3.5 and requires `pdflatex` as a helper library.

I use/prefer macs, so the commands are in/for that. I'm sure you could get it running
  on PC or linux, and if you do, please send in a ticket or Pull Request explaining 
  how you did.

For mac, make sure you have homebrew package manager installed:
```bash
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

And use it to install the `basictex` [brew cask](https://brew.sh/).  
  
```bash
$ brew install basictex --cask
```

#### Running the Builder

The main script for this repository, responsible for reading the json, 
  populating the new `.tex` file, and outputing the actual `.pdf` at the end 
  is in `src/build_resume.pdf`:

```bash
$ python src/build_resume.py
```

Once you run it, look in the `./build` folder to find the following main outputs:
  -  `Resume_NAME.pdf` 
  -  `CoverLetter_NAME` 
  -  `References_NAME.pdf`

#### Rolling Your Own

You probably don't just want to build _my_ resume, so if you'd like to create one 
  that looks like it but contains your own information, simply edit the `.json` files 
  in the `data/` directory.

If you don't like how I laid out my `json` schemas and want to fiddle with how the information 
  is stored, look into editing the `src/update_values_helpers.py` methods. 

More extensive edits can be made to the _content_ of the resume by editing `build/resume.tex` 
  directly. The `.tex` is similar to most other markup once you get the hang of it, and 
  doesn't take you long to learn.

If you'd like to make changes to the _styling_ of the resume, you're looking at changing 
  the `build/resume.cls` file, and more power to you. I've yet to wrestle that beast, and 
  will not be able to provide you much assistance (at least yet).
