import markdown

from packages.markdown_urlify import urlify


def md_to_html(file_name):
    # 1
    with open(f'data/{file_name}.md', 'r') as f:
        markdown_string = f.read()

    urlify_ext = urlify.URLifyExtension()
    extensions = ['markdown.extensions.tables', urlify_ext]

    html_string = markdown.markdown(markdown_string, extensions=extensions)

    # 3
    with open(f'data/{file_name}.html', 'w') as f:
        f.write(html_string)
