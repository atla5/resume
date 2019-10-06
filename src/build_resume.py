# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: build custom resume from LaTeX template and json

import json, time, logging
from os import path, getcwd, system, chdir
from sys import stdout
from shutil import copyfile

from subprocess import check_call, STDOUT, DEVNULL
from update_values_helpers import *

logging.basicConfig(stream=stdout, level=logging.INFO)
logger = logging.getLogger("build_resume")

# set absolute paths for 'build/' and 'data/' directories
src_dir = path.abspath(path.dirname(__file__))
build_dir = path.abspath(path.join(src_dir, "../build"))
data_dir = path.abspath(path.join(src_dir, "../data"))

# variables used in the 
LAST_NAME = "Sawyer"

def get_json_from_data_file(filename):
    json_to_return = {}
    try:
        data_file = path.join(data_dir, filename)
        json_to_return = json.load(open(data_file))
    except FileNotFoundError:
        logger.error("Error loading file: {}".format(filename), exc_info=True)
    finally:
        return json_to_return


def sanitize_latex_syntax(line):
    return line.replace("#", "\#")


def update_shared_values(dict_values):
    logger.debug("adding header, date data to 'dict_values'")

    # about me
    about = get_json_from_data_file('about.json')
    generate_about(dict_values, about)

    # date created
    dict_values.update({
        "DATE~CREATED": time.strftime("%Y-%m-%d")
    })


def update_resume_values(dict_values):
    logger.debug("adding resume values data to 'dict_values'")

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
    logger.debug("adding references data to 'dict_values'")
    references = get_json_from_data_file('references.json')
    for i, project in enumerate(references[:3], start=1):
        generate_reference(dict_values, project, i)


def generate_new_tex_file_with_values(values, input_template, output_filename):
    logger.debug("generating new tex file '{}' using input template '{}'".format(output_filename, input_template))

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
    logger.debug("generating pdf from tex file '{}'".format(output_tex_filename))

    chdir(build_dir)

    # export filename.tex into a pdf
    check_call(['pdflatex', '-interaction=nonstopmode', output_tex_filename], stdout=DEVNULL, stderr=STDOUT)
    logger.info("pdf created at {}".format(output_tex_filename.replace('.tex','.pdf')))


def build_resume():
    logger.info("\n\nbuilding resume...")

    # create and update value dictionary from json files
    dict_values = {}
    update_shared_values(dict_values)
    update_resume_values(dict_values)

    # manage/generate filenames and paths
    tex_template_filepath = path.join(build_dir, "resume.tex")
    last_name = get_last_name(dict_values)
    filename = "{}Resume".format(last_name+"_" if last_name else "")
    tex_new_filepath = path.join(build_dir, filename + ".tex")

    # use values to generate a pdf
    generate_new_tex_file_with_values(dict_values, tex_template_filepath, tex_new_filepath)
    generate_pdf_from_tex_template(tex_new_filepath)


def build_references():
    logger.info("\n\nbuilding references...")

    # create and update value dictionary from json files
    dict_values = {}
    update_shared_values(dict_values)
    update_references_values(dict_values)

    # manage/generate filenames and paths
    tex_template_filepath = path.join(build_dir, "references.tex")
    last_name = get_last_name(dict_values)
    filename = "{}References".format(last_name+"_" if last_name else "")
    tex_new_filepath = path.join(build_dir, filename + ".tex")

    # use values to generate a pdf
    generate_new_tex_file_with_values(dict_values, tex_template_filepath, tex_new_filepath)
    generate_pdf_from_tex_template(tex_new_filepath)


def build_coverletter():
    logger.info("\n\nbuilding cover letter...")
    dict_values = {}
    update_shared_values(dict_values)
    with open(path.join(data_dir, "coverletter.txt"),'r') as cover_letter_text:
        cl_text = ""
        for line in cover_letter_text:
            cl_text += line

        dict_values.update({ 
            "CL~TEXT": cl_text,
            "FORMAL~DATE": humanize_date(dict_values["DATE~CREATED"], formalize=True)
        })

    # manage/generate filenames and paths
    tex_template_filepath = path.join(build_dir, "coverletter.tex")
    last_name = get_last_name(dict_values)
    filename = "{}CoverLetter".format(last_name+"_" if last_name else "")
    tex_new_filepath = path.join(build_dir, filename + ".tex")

    # use values to generate a pdf
    generate_new_tex_file_with_values(dict_values, tex_template_filepath, tex_new_filepath)
    generate_pdf_from_tex_template(tex_new_filepath)


def clean_up():
    system("rm *.fls")
    system("rm *.gz")
    system("rm *latexmk")
    system("rm *.aux")

if __name__ == "__main__":
    build_resume()
    build_references()
    build_coverletter()
    clean_up()
