# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: customize dict_values according to passed values

months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]


def generate_header_info(dict_values):
    dict_values.update({
        "FULL~NAME": "Aidan Sawyer",
        "EMAIL": "aks5238@rit.edu",
        "PHONE": "(207)-200-6026",
        "GITHUB": "atla5 - lib-re",
        "WEBSITE": "atla5.github.io"
    })


def humanize_date(yyyy_mm):
    tokens = yyyy_mm.split('-')
    year = tokens[0]
    month = int(tokens[1])

    return "{} {}".format(months[month-1], year)


def humanize_list(ls):
    return ", ".join(s for s in ls).rstrip(", ")


def generate_school_info(dict_values, school, id=None):
    prefix = "SCHOOL~" + (str(id) if id else "")
    school_notes = school['notes']

    dict_values.update({
        prefix + "NAME": school['school_name'],
        prefix + "DEGREE": "{} in {}".format(school['degree'], school['major']),
        prefix + "TIME~START": humanize_date(school['time_start']),
        prefix + "TIME~END": humanize_date(school['time_end']),
        prefix + "NOTE~1": school_notes[0] if school_notes else "Minor in {}".format(school['minor']),
        prefix + "NOTE~2": school_notes[1] if len(school_notes)>= 2 else ""
    })


def generate_work_experience(dict_values, work, id=1):
    prefix = "W{}~".format(id)
    responsibilities = work['responsibilities']
    num_responsibilities = len(responsibilities)

    dict_values.update({
        prefix + "NAME": work['company_name'],
        prefix + "POSITION": work['position'],
        prefix + "TIME~START": humanize_date(work['time_start']),
        prefix + "TIME~END": humanize_date(work['time_end']) if work['time_end'] else "Present",
        prefix + "ADVISOR~NAME": work['advisor_name'],
        prefix + "ADVISOR~POSITION": work['advisor_position'],
        prefix + "ADVISOR~CONTACT": work['advisor_contact'],
        prefix + "RESPONSIBILITY~1": responsibilities[0] if num_responsibilities >= 1 else work['summary_short'],
        prefix + "RESPONSIBILITY~2": responsibilities[1] if num_responsibilities >= 2 else ""
    })


def generate_project(dict_values, project, id=1):
    prefix = "P{}~".format(id)
    dict_values.update({
        prefix+"NAME": project['name'],
        prefix+"DESCRIPTION": project['description_short']
    })


def generate_language_entry(dict_values, level, languages, id=1):
    suffix = "~{}".format(id)
    dict_values.update({
        "LEVEL" + suffix: level if languages else "",
        "LANGUAGES" + suffix: humanize_list([lang['name'] for lang in languages] if languages else "")
    })


def generate_languages(dict_values, languages):
    # establish name for proficiencies
    lvl_1 = "Intermediate"
    lvl_2 = "Functional"
    lvl_3 = "Novice"

    # sort languages into lists based on proficiency
    ls_intermediate = []
    ls_functional = []
    ls_limited = []
    for language in languages:
        if language['proficiency'] == lvl_1:
            ls_intermediate.append(language)
        elif language['proficiency'] == lvl_2:
            ls_functional.append(language)
        else:
            ls_limited.append(language)

    # update dict_values with each grouping of languages
    generate_language_entry(dict_values, lvl_1, ls_intermediate, 1)
    generate_language_entry(dict_values, lvl_2, ls_functional, 2)
    generate_language_entry(dict_values, lvl_3, ls_limited, 3)
