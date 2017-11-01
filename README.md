# Aidan Sawyer

### Description ###

##### short #####
hold information about my education, work experience, projects, and goals.

##### long #####
This repository is meant to act as both:
 - a convenient reference for visitors to my page to better understand my background and
 - a central hub to store the data objects about my personal and professional
   career in one location.

### Content ###

As a "resume", the repository is meant to store information relevant to my work
  and career. Following the traditional divisions as well as those I found most
  desirable to my site, the information is stored as follows:

|file|description|
|:---|:---------------|
|ROADMAP.md|textual description of stated goals, plans, and objectives over time.|
|experience.json|data describing some of my professional experience and what i've learned from it|
|education.json|data describing my formal schooling (college and high school)|
|projects.json|data describing my [personal](https://github.com/atla5)/[organizational](https://github.com/lib-re) projects|
|additional.json|listing of languages, skills, interests, and links that didn't fit elsewhere|

### Interface ###

If you're just here to view the information stored in these `.json` files, a  much more pleasant way of 
  doing so ~is~ should be available on my website at [aidan-sawyer.com/about](https://aidan-sawyer.com/about).

### How to Use ###

#### Dependencies

- python (tested on `2.6` through `3.5`)
- pdflatex (?)

#### Cloning the Repository 

```
$ cd ~/your/projects/folder
$ git clone https://github.com/atla5/resume.git
```

#### Running the Builder

The main script for this repository, responsible for reading the json, populating the new `.tex` file, 
and outputing the actual `.pdf` at the end is `build/build_resume.pdf`:

```bash
$ cd resume/build/
$ python build_resume.py
```

You have to install some extra software to get the actual `pdflatex` command to work inside of `build_resume`.

```bash
$ sudo apt-get update
$ sudo apt-get install --no-install-recommends texlive-fonts-recommended texlive-latex-extra texlive-fonts-extra texlive-latex-recommended dvipng 
```

_note: you can probably get it running without _all_ of these, i was just making room for growth (and hate debugging LaTeX)_ 

#### Roll Your Own

If you'd like to create a resume that looks like this but contains your own information, simply edit the `.json` 
  files in the main directory, making sure to [lint your json](https://jsonlint.com/) to save time debugging.

If you don't like how I laid out my `json` schemas and want to fiddle with how the information is stored, look 
  into editing the `update_values_helpers` methods. 

More extensive edits can be made to the _content_ of the resume by editing `build/resume.tex` directly. The `.tex` is 
  similar to most other markup once you get the hang of it, and doesn't take you long.

If you'd like to make changes to the _styling_ of the resume, you're looking at changing the `build/resume.cls` file,
  and more power to you. I've yet to wrestle that beast, and will not be able to provide you much assistance (at least yet).
