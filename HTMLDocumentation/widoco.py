
import subprocess
from datetime import datetime

def run_widoco():
    subprocess.run(['java', '-jar', 'widoco-1.4.11-jar-with-dependencies.jar',
                    '-ontFile', '../sto.ttl',
                    '-outFolder', '../docs',
                    '-confFile', './config/config.properties',
                    '-webVowl',
                    '-oops',
                    '-rewriteAll',
                    '-includeAnnotationProperties',
                    '-ignoreIndividuals'])
    return


def replace_widoco_html_output(filename, text):
    newHtml = ''
    skipLines = False
    inserted = False
    with open('../docs/sections/' + filename) as fp:
        for line in fp:
            if line.startswith('<span class="markdown">'):
                skipLines = True
            if line.strip().endswith('/span>'):
                skipLines = False
                continue

            if skipLines and not inserted:
                newHtml += text
                inserted = True
            else:
                newHtml += line.strip()

    with open('../docs/sections/' + filename, 'w') as fp:
        fp.write(newHtml)
        fp.close()
    return


def load_new_html_text(filename):
    with open('../datatext/' + filename, 'r') as fp:
        text = fp.read()

    return text


def insert_into_widoco(section):
    text = load_new_html_text(section + '.html')
    replace_widoco_html_output(section + '-en.html', text)
    return


def finish_widoco_html():
  #  insert_into_widoco('abstract')
    insert_into_widoco('crossref')
    insert_into_widoco('description')
    insert_into_widoco('introduction')
    insert_into_widoco('overview')
    insert_into_widoco('references')



run_widoco()
finish_widoco_html()