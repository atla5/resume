# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: build custom resume from LaTeX template and json

import json, time
from shutil import copyfile
from build.update_values_helpers import *


def generate_filename(last_name=""):
    date = time.strftime("%Y-%m-%d")
    filename = "Resume_{name}{date}".format(
        name=last_name+"_" if last_name else "",
        date=str(date)
    )
    return filename


def sanitize_latex_syntax(line):
    return line.replace("#","\#")


def update_values(dict_values):
    # add header
    generate_header_info(dict_values)

    # add objective
    dict_values.update({
        "OBJECTIVE":"I'm looking for meaningful work involved with the organization, preservation, and expansion of knowledge, with particular regard to library resources and scientific research. By improving the engines which power human understanding, I seek to expedite human progress long-term."
    })

    # add education
    educations = json.load(open('education.json'))
    generate_school_info(dict_values, educations[0])

    # add work experience
    experiences = json.load(open('experience.json'))
    for i, work_experience in enumerate(experiences[:3], start=1):
        generate_work_experience(dict_values, work_experience, i)

    # add projects
    projects = json.load(open('projects.json'))
    for i, project in enumerate(projects[:3], start=1):
        generate_project(dict_values, project, i)

    # add languages
    additional = json.load(open('additional.json'))
    languages = additional['languages']
    generate_languages(dict_values, languages)


if __name__ == "__main__":

    # create and update value dictionary from json files
    dict_values = {}
    update_values(dict_values)

    # manage/generate filenames and paths
    filename = generate_filename(dict_values['FULL~NAME'].split()[-1])
    tex_template_filepath = "./build/resume.tex"
    tex_new_filepath = "./build/"+filename+".tex"

    # copy .tex template into a new (temporary) file 'filename.tex'
    copyfile(tex_template_filepath, tex_new_filepath)

    # use `dict_values` to replace placeholders with real values in filename.tex
    resume_template = open(tex_template_filepath, 'r')
    output_resume = open(tex_new_filepath, 'w')
    for line in resume_template:
        for key in dict_values:
            line = line.replace(key, dict_values[key])
        print(sanitize_latex_syntax(line), file=output_resume)

    # export filename.tex into a pdf
    # TODO

    # delete temporary filename.tex file
    # TODO
