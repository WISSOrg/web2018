# cd /path/to/web2018
# python3 ./utils/absolute-to-relative.py

sub_pages = [
    "archive",
    "award",
    "call-for-papers",
    "call-for-participants",
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
    open(path, 'w').write(html)
