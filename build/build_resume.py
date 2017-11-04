# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: build custom resume from LaTeX template and json

import json, time
from os import path, getcwd, system
from shutil import copyfile
from update_values_helpers import *

# set absolute paths for 'build/' and 'data/' directories
build_dir = path.abspath(getcwd())
data_dir = path.abspath(path.join(getcwd(), "../data"))


def sanitize_latex_syntax(line):
    return line.replace("#", "\#")


def update_values(dict_values):

    # header and objective
    about_file = path.join(data_dir, 'about.json')
    about = json.load(open(about_file))
    generate_about(dict_values, about)

    # education
    education_file = path.join(data_dir, 'education.json')
    educations = json.load(open(education_file))
    generate_school_info(dict_values, educations[0])

    # work experience
    experiences_file = path.join(data_dir, 'experience.json')
    experiences = json.load(open(experiences_file))
    for i, work_experience in enumerate(experiences[:3], start=1):
        generate_work_experience(dict_values, work_experience, i)

    # projects
    projects_file = path.join(data_dir, 'projects.json')
    projects = json.load(open(projects_file))
    for i, project in enumerate(projects[:3], start=1):
        generate_project(dict_values, project, i)

    # languages
    additional_file = path.join(data_dir, 'additional.json')
    additional = json.load(open(additional_file))
    languages = additional['languages']
    generate_languages(dict_values, languages)


def build_resume():

    # create and update value dictionary from json files
    dict_values = {
        "DATE~CREATED": time.strftime("%Y-%m-%d"),
    }
    update_values(dict_values)

    # manage/generate filenames and paths
    tex_template_filepath = path.join(build_dir, "resume.tex")

    last_name = dict_values['FULL~NAME'].split()[-1]
    filename = "Resume{}".format("_"+last_name if last_name else "")
    tex_new_filepath = path.join(build_dir, filename + ".tex")

    # copy .tex template into a new (temporary) file 'filename.tex'
    copyfile(tex_template_filepath, tex_new_filepath)

    # use `dict_values` to replace placeholders in template with real values in the new one
    resume_template = open(tex_template_filepath, 'r')
    output_resume = open(tex_new_filepath, 'w')
    for line in resume_template:
        for key in dict_values:
            line = line.replace(key, dict_values[key])
        output_resume.write(sanitize_latex_syntax(line))

    # close files
    resume_template.close()
    output_resume.close()

    # export filename.tex into a pdf
    system("pdflatex -interaction=nonstopmode {}".format(tex_new_filepath))

    # delete temporary filename.tex file
    system("rm *.log")
    system("rm *.aux")
    system("rm -rf __pycache__")


def build_references():
    pass

if __name__ == "__main__":
    build_resume()
