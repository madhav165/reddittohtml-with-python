#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup
import argparse
import contextlib
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
        orig_post_text = orig_post.find('div', class_='md').text.strip()
    else:
        orig_post_text = orig_post.find('p', class_='title').a.get('href')
    print (orig_title)
    print (orig_poster)
    print (orig_post_text)
    
    comment_area = all_content.find('div', class_='commentarea').find('div', class_='sitetable')
    things = comment_area.findAll('div', class_='thing', recursive=False)
    for thing in things:
        l0_comment = thing.find('div', class_='entry')
        l0_comment_author = l0_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
        l0_comment_text = l0_comment.form.find('div', class_='md').text.strip()
        print (l0_comment_author+'\n')
        print (l0_comment_text+'\n')

        children = thing.findAll('div', class_='child', recursive=False)
        for child in children:
            if (child.find('div', class_='sitetable') is not None):
                things2 = child.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                for thing2 in things2:
                    l1_comment = thing2.find('div', class_='entry')
                    l1_comment_author = l1_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                    l1_comment_text = l1_comment.form.find('div', class_='md').text.strip()
                    print (l1_comment_author+'\n')
                    print (l1_comment_text+'\n')

                    children2 = thing2.findAll('div', class_='child', recursive=False)
                    for child2 in children2:
                        if (child2.find('div', class_='sitetable') is not None):
                            things3 = child2.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                            for thing3 in things3:
                                l2_comment = thing3.find('div', class_='entry')
                                l2_comment_author = l2_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                l2_comment_text = l2_comment.form.find('div', class_='md').text.strip()
                                print (l2_comment_author+'\n')
                                print (l2_comment_text+'\n')
    
                                children3 = thing3.findAll('div', class_='child', recursive=False)
                                for child3 in children3:
                                    if (child3.find('div', class_='sitetable') is not None):
                                        things4 = child3.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                                        for thing4 in things4:
                                            l3_comment = thing4.find('div', class_='entry')
                                            l3_comment_author = l3_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                            l3_comment_text = l3_comment.form.find('div', class_='md').text.strip()
                                            print (l3_comment_author+'\n')
                                            print (l3_comment_text+'\n')

                                            children4 = thing4.findAll('div', class_='child', recursive=False)
                                            for child4 in children4:
                                                if (child4.find('div', class_='sitetable') is not None):
                                                    things5 = child4.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                                                    for thing5 in things5:
                                                        l4_comment = thing5.find('div', class_='entry')
                                                        l4_comment_author = l4_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                                        l4_comment_text = l4_comment.form.find('div', class_='md').text.strip()
                                                        print (l4_comment_author+'\n')
                                                        print (l4_comment_text+'\n')

                                                        children5 = thing5.findAll('div', class_='child', recursive=False)
                                                        for child5 in children5:
                                                            if (child5.find('div', class_='sitetable') is not None):
                                                                things6 = child5.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                                                                for thing6 in things6:
                                                                    l5_comment = thing6.find('div', class_='entry')
                                                                    l5_comment_author = l5_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                                                    l5_comment_text = l5_comment.form.find('div', class_='md').text.strip()
                                                                    print (l5_comment_author+'\n')
                                                                    print (l5_comment_text+'\n')

                                                                    children6 = thing6.findAll('div', class_='child', recursive=False)
                                                                    for child6 in children6:
                                                                        if (child6.find('div', class_='sitetable') is not None):
                                                                            things7 = child6.find('div', class_='sitetable').findAll('div', class_='thing', recursive=False)
                                                                            for thing7 in things7:
                                                                                l6_comment = thing7.find('div', class_='entry')
                                                                                l6_comment_author = l6_comment.find('p', class_='tagline').find('a', class_='author').text.strip()
                                                                                l6_comment_text = l6_comment.form.find('div', class_='md').text.strip()
                                                                                print (l6_comment_author+'\n')
                                                                                print (l6_comment_text+'\n')


get_url()
html_doc = get_html()
get_matches(html_doc)
