"""
Utility to write out work to markdown. Uses pypandoc to convert the markdown to html when complete.
"""

import time
import os.path
import pypandoc

__author__ = "Matt Fister"


#name = str(int(time.time()))
name = 'out'
md_name = name + '.md'
html_name = name + '.html'
md_file_path = os.path.join('output', md_name)
html_file_path = os.path.join('output', html_name)
out_file = open(md_file_path, 'w')

word_count = 0


def print_title(s):
    print('%'+s+'\n')
    global word_count
    word_count += len(s.split(" "))
    out_file.write('%'+s+'\n\n')


def print_sub_title(s):
    print('##'+s+'\n')
    global word_count
    word_count += len(s.split(" "))
    out_file.write('##'+s+'\n')


def print_chapter_heading(s):
    print('###'+s+'\n')
    global word_count
    word_count += len(s.split(" "))
    out_file.write('###'+s+'\n')


def print_chapter_subheading(s):
    print('####'+s+'\n')
    global word_count
    word_count += len(s.split(" "))
    out_file.write('####'+s+'\n')


def print_chapter_sentence(s):
    print(s + ' ')
    global word_count
    word_count += len(s.split(" "))
    try:
        out_file.write(s + ' ')
    except UnicodeEncodeError:
        pass


def print_list_item(s):
    print('* ' + s)
    global word_count
    word_count += len(s.split(" "))
    try:
        out_file.write("* " + s)
    except UnicodeEncodeError:
        pass


def print_quote_line(s):
    print('> ' + s+'\n')
    print(">\n")
    global word_count
    word_count += len(s.split(" "))
    try:
        out_file.write("> " + s + '\n')
        out_file.write(">\n")
    except UnicodeEncodeError:
        pass


def end_paragraph():
    out_file.write('\n\n')


def end_chapter():
    out_file.write('\n\n')


def phrase_as_link(phrase):
    ret_phrase = "["+phrase+"]"+"(#"+phrase.replace(" ", "-")+")"
    return ret_phrase


def phrase_with_anchor(phrase):
    ret_phrase = '<a name="' + phrase.replace(" ", "-") + '"></a>'+phrase
    return ret_phrase


def insert_image(image_rel_path, alt_text):
    print('![' + alt_text + '](' + image_rel_path + ')')
    print("\n")
    try:
        out_file.write("\n")
        out_file.write('![''](' + image_rel_path + ')')
        out_file.write("\n")
        out_file.write("\n")
        out_file.write("\n")
    except UnicodeEncodeError:
        pass

# To add css call like css='https://mattfister.github.io/nanogenmo2015/samples/base.css'
def end_novel(css=None):
    out_file.close()
    if css is None:
        pypandoc.convert(md_file_path, 'html', outputfile=html_file_path, extra_args=['-s'])
    else:
        pypandoc.convert(md_file_path, 'html', outputfile=html_file_path, extra_args=['-s', '-c', css])
    print('Total words: ' + str(word_count))


