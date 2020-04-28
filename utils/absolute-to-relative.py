# cd /path/to/web2018
# python3 ./utils/absolute-to-relative.py

import re

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
    html = html.replace("=\"/", "=\"../")
    html = html.replace("=\'/wp", "=\'../wp")
    html = html.replace("\n0\n", "")
    html = re.sub("[a-f0-9]+(\r)*\n\<", "<", html)
    open(path, 'w').write(html)
