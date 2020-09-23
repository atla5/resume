# author: Aidan Sawyer (atla5)
# date_created: 2017-08-12
# license: MIT
# purpose: customize dict_values according to passed values

import logging
logger = logging.getLogger(__name__)

months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
months_full = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def humanize_date(yyyy_mm, formalize=False):
    output = yyyy_mm

    try:
        if '-' not in yyyy_mm:
            return yyyy_mm
        else:
            tokens = yyyy_mm.split('-')
            year = tokens[0]
            month = int(tokens[1])

        if 0 < month <= 12:
            str_month = months_full[month-1] if formalize else months[month-1]
            output = "{} {}".format(str_month, year)
        else:
            logger.warning("Invalid month: {}\n".format(yyyy_mm))

    except IndexError:
        logger.warning("Improperly formatted date: {}\n".format(yyyy_mm))

    finally:
        return output


def humanize_list(ls):
    return ", ".join(str(s) for s in ls)


def generate_about(dict_values, about):
    contact = about['contact']
    accounts = about['accounts']
    highlights = about['overview']
    dict_values.update({
        "FULL~NAME": about['name'],
        "OBJECTIVE": about['objective'],
        "EMAIL": contact['email'] if contact['email'] else "",
        "PHONE": contact['phone'] if contact['phone'] else "",
        "GITHUB": "{} - {}".format(accounts['github'], accounts['github-org']),
        "WEBSITE": about['url'].replace('http://', ''),
        "HIGHLIGHT~1": highlights[0],
        "HIGHLIGHT~2": highlights[1]
    })


def generate_school_info(dict_values, school, id=None):
    logging.debug("updating school values...")
    prefix = "SCHOOL~" + (str(id) if id else "")
    school_notes = school['notes']

    dict_values.update({
        prefix + "NAME": school['school_name'],
        prefix + "DEGREE": "{} in {}".format(school['degree'], school['major']),
        prefix + "TIME~START": humanize_date(school['time_start']),
        prefix + "TIME~END": humanize_date(school['time_end']),
        prefix + "NOTE~1": school_notes[0] if school_notes else "Minor in {}".format(school['minor']),
        prefix + "NOTE~2": school_notes[1] if len(school_notes) >= 2 else ""
    })


def generate_work_experience(dict_values, work, id=1):
    logging.debug("updating work experience values for work '{}'".format(id))
    prefix = "W{}~".format(id)
    responsibilities = work['responsibilities']
    num_responsibilities = len(responsibilities)

    dict_values.update({
        prefix + "NAME": work['company_name'],
        prefix + "POSITION": work['position'],
        prefix + "TIME~START": humanize_date(work['time_start']),
        prefix + "TIME~END": humanize_date(work['time_end']) if 'time_end' in work else "Present",
        prefix + "ADVISOR~NAME": work['advisor_name'],
        prefix + "ADVISOR~POSITION": work['advisor_position'],
        prefix + "ADVISOR~CONTACT": work['advisor_contact'],
        prefix + "RESPONSIBILITY~1": responsibilities[0] if num_responsibilities >= 1 else work['summary_short'],
        prefix + "RESPONSIBILITY~2": responsibilities[1] if num_responsibilities >= 2 else "",
        prefix + "RESPONSIBILITY~3": responsibilities[2] if num_responsibilities >= 3 else "",
        prefix + "SUMMARY": work['summary_short'] if 'summary_short' in work else ""
    })


def generate_reference(dict_values, reference, id=1):
    logging.debug("updating reference '{}'".format(id))
    prefix = "R{}~".format(id)

    contact = reference['email']
    if 'phone' in reference and reference['phone']:
        contact += " - {}".format(reference['phone'])
    dict_values.update({
        prefix + "NAME": reference['name'],
        prefix + "CONTACT": contact,
        prefix + "POSITION": reference['position'],
        prefix + "DATE~START": humanize_date(reference['date_start']),
        prefix + "DATE~END": humanize_date(reference['date_end']) if 'date_end' in reference else "Present",
        prefix + "RELATIONSHIP": reference['relationship'],
        prefix + "IMPORTANCE": reference['importance'],
    })


def generate_project(dict_values, project, id=1):
    logging.debug("updating project info for project '{}'".format(id))
    prefix = "P{}~".format(id)
    dict_values.update({
        prefix+"NAME": project['name'],
        prefix+"DESCRIPTION": project['description_short']
    })


def generate_language_entry(dict_values, level, languages, id=1):
    logging.debug("updating language entry for level '{}'".format(level))
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
