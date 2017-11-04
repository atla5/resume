# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: build custom resume from LaTeX template and json

import json, time
from os import path, getcwd, system
from shutil import copyfile
from sys import stderr
from update_values_helpers import *

# set absolute paths for 'build/' and 'data/' directories
build_dir = path.abspath(getcwd())
data_dir = path.abspath(path.join(getcwd(), "../data"))


def get_json_from_data_file(filename):
    json_to_return = {}
    try:
        data_file = path.join(data_dir, filename)
        json_to_return = json.load(open(data_file))
    except FileNotFoundError:
        stderr.write("Error loading file: {}".format(filename), exc_info=True)
    finally:
        return json_to_return


def sanitize_latex_syntax(line):
    return line.replace("#", "\#")


def update_shared_values(dict_values):
    # about me
    about = get_json_from_data_file('about.json')
    generate_about(dict_values, about)

    # date created
    dict_values.update({
        "DATE~CREATED": time.strftime("%Y-%m-%d")
    })

def update_resume_values(dict_values):
    # education
    educations = get_json_from_data_file('education.json')
    generate_school_info(dict_values, educations[0])

    # work experience
    experiences = get_json_from_data_file('experience.json')
    for i, work_experience in enumerate(experiences[:3], start=1):
        generate_work_experience(dict_values, work_experience, i)

    # projects
    projects = get_json_from_data_file('projects.json')
    for i, project in enumerate(projects[:3], start=1):
        generate_project(dict_values, project, i)

    # languages
    additional = get_json_from_data_file('additional.json')
    languages = additional['languages']
    generate_languages(dict_values, languages)


def update_references_values(dict_values):
    references = get_json_from_data_file('references.json')
    for i, project in enumerate(references[:3], start=1):
        generate_reference(dict_values, project, i)


def generate_new_tex_file_with_values(values, input_template, output_filename):
    # copy .tex template into a new 'output_filename.tex'
    copyfile(input_template, output_filename)

    # use `dict_values` to replace placeholders in template with real values in the new one
    resume_template = open(input_template, 'r')
    output_tex = open(output_filename, 'w')
    for line in resume_template:
        for key in values:
            line = line.replace(key, values[key])
        output_tex.write(sanitize_latex_syntax(line))

    # close files
    resume_template.close()
    output_tex.close()


def generate_pdf_from_tex_template(output_tex_filename):
    # export filename.tex into a pdf
    system("pdflatex -interaction=nonstopmode {}".format(output_tex_filename))

    # delete temporary filename.tex file
    system("rm *.log")
    system("rm *.aux")
    system("rm -rf __pycache__")


def build_resume():

    # create and update value dictionary from json files
    dict_values = {}
    update_shared_values(dict_values)
    update_resume_values(dict_values)

    # manage/generate filenames and paths
    tex_template_filepath = path.join(build_dir, "resume.tex")
    last_name = dict_values['FULL~NAME'].split()[-1]
    filename = "Resume{}".format("_"+last_name if last_name else "")
    tex_new_filepath = path.join(build_dir, filename + ".tex")

    # use values to generate a pdf
    generate_new_tex_file_with_values(dict_values, tex_template_filepath, tex_new_filepath)
    generate_pdf_from_tex_template(tex_new_filepath)


def build_references():

    # create and update value dictionary from json files
    dict_values = {}
    update_shared_values(dict_values)
    update_references_values(dict_values)

    # manage/generate filenames and paths
    tex_template_filepath = path.join(build_dir, "references.tex")
    last_name = dict_values['FULL~NAME'].split()[-1]
    filename = "References{}".format("_" + last_name if last_name else "")
    tex_new_filepath = path.join(build_dir, filename + ".tex")

    # use values to generate a pdf
    generate_new_tex_file_with_values(dict_values, tex_template_filepath, tex_new_filepath)
    generate_pdf_from_tex_template(tex_new_filepath)

if __name__ == "__main__":
    build_resume()
    build_references()
