# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: build custom resume from LaTeX template and json

import json
from build.update_values_helpers import *
from pprint import pprint


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


    # export
    pprint(dict_values)
