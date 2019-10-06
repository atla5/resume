# Aidan Sawyer

### Description ###

##### short #####
store and export information about my education, work experience, projects, and goals.

##### long #####
This repository is meant to act as both:
 - a convenient reference for visitors to my page to better understand my background 
 - a central hub to store the data objects about my personal and professional career in one location.
 - a repeatable and automated way to generate updated PDFs (allowing me to only update the json and run a command)
 - a simplified way to host/serve resume info and pdf download on [my site](http://aidan-sawyer.com).

### Content ###

As a "resume", the repository is meant to store information relevant to my work
  and career. Following the traditional divisions as well as those I found most
  desirable to my site, the information is stored as follows:

|file|description|
|:---|:---------------|
|ROADMAP.md|textual description of stated goals, plans, and objectives over time.|
|experience.json|data describing some of my professional experience and what i've learned from it|
|education.json|data describing my formal schooling|
|projects.json|data describing my [personal](https://github.com/atla5)/[organizational](https://github.com/lib-re) projects|
|additional.json|listing of languages, skills, interests, and links that didn't fit elsewhere|

### Interface ###

If you're just here to view the information stored in these `.json` files, a  much more pleasant way of 
  doing so is available on my website at [aidan-sawyer.com/about](http://aidan-sawyer.com/about).

### How to Use ###

#### Getting Started

Clone the repository or download the zip from the master branch
```
$ cd ~/your/projects/folder
$ git clone https://github.com/atla5/resume.git
```

This project runs on python 2.6 - 3.5 and requires `pdflatex`, included in the `basictex` 
  [brew cask](https://brew.sh/).  
``` 
$ brew cask install basictex
```

#### Running the Builder

The main script for this repository, responsible for reading the json, 
  populating the new `.tex` file, and outputing the actual `.pdf` at the end 
  is in `src/build_resume.pdf`:

```bash
$ python src/build_resume.py
```

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
