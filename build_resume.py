# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: build custom resume from LaTeX template and json

import json
from build import update_values
from pprint import pprint

if __name__ == "__main__":
    dict_values = {}

    # add header
    update_values.generate_header_info(dict_values)

    # add objective
    dict_values.update({
        "OBJECTIVE":"I'm looking for meaningful work involved with the organization, preservation, and expansion of knowledge, with particular regard to library resources and scientific research. By improving the engines which power human understanding, I seek to expedite human progress long-term."
    })

    # add education
    educations = json.load(open('education.json'))
    update_values.generate_school_info(dict_values, educations[0])

    # add work experience
    experiences = json.load(open('experience.json'))
    for i, work_experience in enumerate(experiences[:3], start=1):
        update_values.generate_work_experience(dict_values, work_experience, i)

    # add projects
    projects = json.load(open('projects.json'))
    for i, project in enumerate(projects[:3], start=1):
        update_values.generate_project(dict_values, project, i)

    # add languages
    additional = json.load(open('additional.json'))
    languages = additional['languages']
    update_values.generate_languages(dict_values, languages)

    # export
    pprint(dict_values)
