sub_pages = [
    "archive",
    "award",
    "call-for-papers",
    "call-for-participants",
    "call-for-participants/challenge",
    "call-for-participants/design-competition",
    "call-for-participants/sponsorship",
    "call-for-participants/student_volunteer",
    "call-for-participants/web-design",
    "committee",
    "demo-poster",
    "local",
    "namecard",
    "program",
    "review_form",
    "review_policy",
]

for sub_page in sub_pages:
    path = "./docs/" + sub_page + "/index.html"
    html = open(path).read()
    html = html.replace("<a href=\"Proceedings/\">", "<a href=\"https://www.wiss.org/WISS2018Proceedings/\">")
    open(path, 'w').write(html)
