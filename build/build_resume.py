# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: build custom resume from LaTeX template and json

import json, time, os
from shutil import copyfile
from update_values_helpers import *


def sanitize_latex_syntax(line):
    return line.replace("#", "\#")


def update_values(dict_values):

    # header and objective
    about = json.load(open('../about.json'))
    generate_about(dict_values, about)

    # education
    educations = json.load(open('../education.json'))
    generate_school_info(dict_values, educations[0])

    # work experience
    experiences = json.load(open('../experience.json'))
    for i, work_experience in enumerate(experiences[:3], start=1):
        generate_work_experience(dict_values, work_experience, i)

    # projects
    projects = json.load(open('../projects.json'))
    for i, project in enumerate(projects[:3], start=1):
        generate_project(dict_values, project, i)

    # languages
    additional = json.load(open('../additional.json'))
    languages = additional['languages']
    generate_languages(dict_values, languages)


if __name__ == "__main__":

    # create and update value dictionary from json files
    dict_values = {
        "DATE~CREATED": time.strftime("%Y-%m-%d"),
    }
    update_values(dict_values)

    # manage/generate filenames and paths
    build_dir = os.getcwd()
    tex_template_filepath = os.path.join(build_dir, "resume.tex")

    last_name = dict_values['FULL~NAME'].split()[-1]
    filename = "Resume{}".format("_"+last_name if last_name else "")
    tex_new_filepath = os.path.join(build_dir, filename+".tex")

    # copy .tex template into a new (temporary) file 'filename.tex'
    copyfile(tex_template_filepath, tex_new_filepath)

    # use `dict_values` to replace placeholders in template with real values in the new one
    resume_template = open(tex_template_filepath, 'r')
    output_resume = open(tex_new_filepath, 'w')
    for line in resume_template:
        for key in dict_values:
            line = line.replace(key, dict_values[key])
        if not line.isspace():
            print(sanitize_latex_syntax(line), file=output_resume)

    # export filename.tex into a pdf
    # os.chdir(build_dir)
    # os.system("pdflatex -interaction=nonstopmode {}".format(tex_new_filepath))

    # delete temporary filename.tex file
    # os.remove(tex_new_filepath)
    # os.system("rm *.log")
    # os.system("rm *.aux")