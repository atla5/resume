# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: customize dict_values according to passed values

def generate_header_info(dict_values):
    dict_values.update({
        "FULL_NAME": "Aidan Sawyer",
        "EMAIL": "aks5238@rit.edu",
        "PHONE": "(585)-397-5491",
        "GITHUB": "atla5 | lib-re",
        "WEBSITE": "atla5.github.io"
    })

def generate_school_info(dict_values, school, id=None):
    prefix="SCHOOL_" + (str(id) if id else "")
    dict_values.update({
        prefix+"NAME": school['school_name'],
        prefix+"DEGREE": "{} in {}".format(school['degree'], school['major']),
        prefix+"TIME_START": school['time_start'],
        prefix+"TIME_END": school['time_end'],
        prefix+"NOTE_1": "Commendations: {}".format(award+" " for award in school['awards']),
        prefix+"NOTE_2": school['notes'],
        prefix+"NOTE_3": "Minor in {}".format(school['minor']) if school['minor'] else ""
    })

def generate_work_experience(dict_values, work, id=1):
    prefix="W{}_".format(id)
    responsibilities = work['responsibilities']
    num_responsibilities = len(responsibilities)

    dict_values.update({
        prefix+"NAME": work['company_name'],
        prefix+"POSITION": work['position'],
        prefix+"TIME_START": work['time_start'],
        prefix+"TIME_END": work['time_end'] if work['time_end'] else "Present",
        prefix+"ADVISOR_NAME": work['advisor_name'],
        prefix+"ADVISOR_POSITION": work['advisor_position'],
        prefix+"ADMISOR_CONTACT": work['advisor_contact'],
        prefix+"RESPONSIBILITY_1": responsibilities[0] if num_responsibilities >=1 else work['summary_short'],
        prefix+"RESPONSIBILITY_2": responsibilities[1] if num_responsibilities >=2 else "",
        prefix+"RESPONSIBILITY_3": responsibilities[2] if num_responsibilities >=3 else "",
    })

def generate_project(dict_values, project, id=1):
    prefix="P{}_".format(id)
    dict_values.update({
        "NAME": project['name'],
        "DESCRIPTION": project['description_short']
    })

def generate_language_entry(dict_values, level, languages, id=1):
    suffix="_{}".format(id)
    dict_values.update({
        "LEVEL"+suffix: level if languages else "",
        "LANGUAGES"+suffix: str([lang['name'] for lang in languages]).strip('[]') if languages else "",
    })

def generate_languages(dict_values, languages):
    # establish name for proficiencies
    LVL_1 = "Intermediate"
    LVL_2 = "Functional"
    LVL_3 = "Limited"

    # sort languages into lists based on proficiency
    ls_intermediate = []
    ls_functional = []
    ls_limited = []
    for language in languages:
        if language['proficiency'] == LVL_1:
            ls_intermediate.append(language)
        elif language['proficiency'] == LVL_2:
            ls_functional.append(language)
        else:
            ls_limited.append(language)

    # update dict_values with each grouping of languages
    generate_language_entry(dict_values, LVL_1, ls_intermediate, 1)
    generate_language_entry(dict_values, LVL_2, ls_functional, 2)
    generate_language_entry(dict_values, LVL_3, ls_limited, 3)
