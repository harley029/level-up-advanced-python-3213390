htmls=[
    'This is in <em>italics</em>. So is <em>this</em>',
    'This sentence has a    lot of    \ninteresting white spaces.',
    '<p>This is a paragraph.</p>',
    '<p>This is a paragraph.</p><p>This is another\nparagraph.</p>',
    'This is the <a href="https://pypi.org/project/html2markdown/">link</a> to the html2markdown package and here is <a href="https://github.com/dlon/html2markdown">another link</a> to the project homepage'
]


def html2markdown(html):
    '''Take in html text as input and return markdown'''
    # clean up html from newlines and spaces
    html = html.replace('\n',' ').split(' ')
    html= ' '.join(list(filter(lambda x: x!= '', html)))
    if "<em>" in html:
        html = html.replace("<em>", "*").replace("</em>", "*")
    if "</p><p>" in html:
        html = html.replace("</p><p>", "\n\n").removeprefix("<p>").removesuffix("</p>")
    if "<p>" in html:
        html = html.replace("<p>", "").replace("</p>", "")
    if "<a href=" in html:
        html = html.replace("<a href=\"", "[link](",1).replace("\">link</a>", ")",1)
    if "<a href=" in html:
        html = html.replace("<a href=\"", "[another link](",1).replace("\">", ") ").replace("another link</a> ", "")
    return html
# print(html2markdown(htmls[4]))
# [print(link) for link in htmls]