#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup
import argparse
import contextlib
import os
#from fake_useragent import UserAgent

global URL

def get_url():
    global URL
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    URL = args.url

def get_html():
    #ua = UserAgent()
    #ua.chrome
    req = urllib.request.Request(URL,
                                headers={'User-Agent': 'Mozilla/5.0 \
                                         (X11; Linux x86_64) \
                                          AppleWebKit/537.36 (KHTML, like Gecko) \
                                          Chrome/53.0.2774.3 Safari/537.36'})
    with contextlib.closing(urllib.request.urlopen(req)) as f:
        return f.read().decode('utf-8');

def get_matches(html_doc):
    soup = BeautifulSoup(html_doc, 'lxml')
    all_content = soup.find('div', class_='content')
    main_post = all_content.find('div', class_='sitetable')
    orig_post = main_post.find('div', class_='entry')
    orig_title = orig_post.find('p', class_='title').a.text.strip()
    orig_poster = orig_post.find('p', class_='tagline').a.text.strip()
    if(orig_post.find('div', class_='md') is not None):
        orig_post_text = orig_post.find('div', class_='md')
    else:
        orig_post_text = orig_post.find('p', class_='title').a.get('href')

    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]
    html_folder_path = os.path.join(script_dir, 'html')
    if (not os.path.exists(html_folder_path)):
        os.makedirs(html_folder_path)
    rel_path = 'html/'+soup.title.text.replace('/','')+'.html'
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path ,'w')
    f.write('<!doctype html><html><body>')
    f.write('<h2>'+orig_title+'</h1>')
    f.write('<p><b>'+orig_poster+'</b></p>')
    f.write('<p>'+str(orig_post_text)+'</p>')

    f.write('<h2>Comments</h2>')
    comment_area = all_content.find('div', class_='commentarea').find('div', class_='sitetable')
    things = comment_area.findAll('div', class_='thing', recursive=False)
    for thing in things:
        l0_comment = thing.find('div', class_='entry')
        if (l0_comment.find('p', class_='tagline').find('a', class_='author') is not None):
            l0_comment_author = l0_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
        else:
            l0_comment_author = 'Deleted'
        if (l0_comment.form is not None):
            l0_comment_text = l0_comment.form.find('div', class_='md')
        else:
            l0_comment_text = 'Deleted'
        f.write('<p><b>'+l0_comment_author+'</b></p>')
        f.write('<p>'+str(l0_comment_text)+'</p>')

        children = thing.findAll('div', class_='child', recursive=False)
        for child in children:
            if (child.find('div', class_='sitetable') is not None):
                things2 = child.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                f.write('<blockquote>')
                for thing2 in things2:
                    l1_comment = thing2.find('div', class_='entry')
                    if (l1_comment.find('p', class_='tagline').find('a', class_='author') is not None):
                        l1_comment_author = l1_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                    else:
                        l1_comment_author = 'Deleted'
                    if (l1_comment.form is not None):
                        l1_comment_text = l1_comment.form.find('div', class_='md')
                    else:
                        l1_comment_text = 'Deleted'
                    f.write('<p><b>'+l1_comment_author+'</b></p>')
                    f.write('<p>'+str(l1_comment_text)+'</p>')

                    children2 = thing2.findAll('div', class_='child', recursive=False)
                    for child2 in children2:
                        if (child2.find('div', class_='sitetable') is not None):
                            things3 = child2.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                            f.write('<blockquote>')
                            for thing3 in things3:
                                l2_comment = thing3.find('div', class_='entry')
                                if (l2_comment.find('p', class_='tagline').find('a', class_='author') is not None):
                                    l2_comment_author = l2_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                else:
                                    l2_comment_author = 'Deleted'
                                if (l2_comment.form is not None):
                                    l2_comment_text = l2_comment.form.find('div', class_='md')
                                else:
                                    l2_comment_text = 'Deleted'
                                f.write('<p><b>'+l2_comment_author+'</b></p>')
                                f.write('<p>'+str(l2_comment_text)+'</p>')
    
                                children3 = thing3.findAll('div', class_='child', recursive=False)
                                for child3 in children3:
                                    if (child3.find('div', class_='sitetable') is not None):
                                        things4 = child3.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                                        f.write('<blockquote>')
                                        for thing4 in things4:
                                            l3_comment = thing4.find('div', class_='entry')
                                            if(l3_comment.find('p', class_='tagline').find('a', class_='author') is not None):
                                                l3_comment_author = l3_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                            else:
                                                l3_comment_author = 'Deleted'
                                            if(l3_comment.form is not None):
                                                l3_comment_text = l3_comment.form.find('div', class_='md')
                                            else:
                                                l3_comment_text = 'Deleted'
                                            f.write('<p><b>'+l3_comment_author+'</b></p>')
                                            f.write('<p>'+str(l3_comment_text)+'</p>')

                                            children4 = thing4.findAll('div', class_='child', recursive=False)
                                            for child4 in children4:
                                                if (child4.find('div', class_='sitetable') is not None):
                                                    things5 = child4.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                                                    f.write('<blockquote>')
                                                    for thing5 in things5:
                                                        l4_comment = thing5.find('div', class_='entry')
                                                        if(l4_comment.find('p', class_='tagline').find('a', class_='author') is not None):
                                                            l4_comment_author = l4_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                                        else:
                                                            l4_comment_author = 'Deleted'
                                                        if(l4_comment.form is not None):
                                                            l4_comment_text = l4_comment.form.find('div', class_='md')
                                                        else:
                                                            l4_comment_text = 'Deleted'
                                                        f.write('<p><b>'+l4_comment_author+'</b></p>')
                                                        f.write('<p>'+str(l4_comment_text)+'</p>')

                                                        children5 = thing5.findAll('div', class_='child', recursive=False)
                                                        for child5 in children5:
                                                            if (child5.find('div', class_='sitetable') is not None):
                                                                things6 = child5.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                                                                f.write('<blockquote>')
                                                                for thing6 in things6:
                                                                    l5_comment = thing6.find('div', class_='entry')
                                                                    if(l5_comment.find('p', class_='tagline').find('a', class_='author') is not None):
                                                                        l5_comment_author = l5_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                                                    else:
                                                                        l5_comment_author = 'Deleted'
                                                                    if(l5_comment.form is not None):
                                                                        l5_comment_text = l5_comment.form.find('div', class_='md')
                                                                    else:
                                                                        l5_comment_text = 'Deleted'
                                                                    f.write('<p><b>'+l5_comment_author+'</b></p>')
                                                                    f.write('<p>'+str(l5_comment_text)+'</p>')

                                                                    children6 = thing6.findAll('div', class_='child', recursive=False)
                                                                    for child6 in children6:
                                                                        if (child6.find('div', class_='sitetable') is not None):
                                                                            things7 = child6.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                                                                            f.write('<blockquote>')
                                                                            for thing7 in things7:
                                                                                l6_comment = thing7.find('div', class_='entry')
                                                                                if(l6_comment.find('p', class_='tagline').find('a', class_='author') is not None):
                                                                                    l6_comment_author = l6_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                                                                else:
                                                                                    l6_comment_author = 'Deleted'
                                                                                if (l6_comment.form is not None):
                                                                                    l6_comment_text = l6_comment.form.find('div', class_='md')
                                                                                else:
                                                                                    l6_comment_text = 'Deleted'
                                                                                f.write('<p><b>'+l6_comment_author+'</b></p>')
                                                                                f.write('<p>'+str(l6_comment_text)+'</p>')
                                                                            f.write('</blockquote>')
                                                                f.write('</blockquote>')
                                                    f.write('</blockquote>')
                                        f.write('</blockquote>')
                            f.write('</blockquote>')
                f.write('</blockquote>')
    f.write('</body></html>')
    f.close()


get_url()
html_doc = get_html()
get_matches(html_doc)
