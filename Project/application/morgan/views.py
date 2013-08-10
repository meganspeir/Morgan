# -*- coding: utf-8 -*-

"""app.

Write some more shit here. Because no one can make up their mind exactly how to
do this. I really just like the pretty color that shows up in my text editor.

Longer description including the modules and subpackages exported by this
package should go here.

:copyright: Copyright 2013 by Megan Speir

"""

__version__ = "0.0.0"
# $Source$


from morgan import app, render_template, abort, request, redirect, \
    url_for

# root
@app.route('/')
def home():
    sentiment = ['coolest', 'ladies', 'tech', 'girl', 'geek', 'love',
                'hackers','lesson', 'women', 'fear', 'excited', 'digust',
                'nasty', 'horrid', 'smell', 'farts', 'ate', 'puked',
                'violently', 'hello', 'goodbye', 'hot', 'morning',
                'California', 'Texas', 'SF', 'back', 'sunset']
    return render_template('home.html',
                           sentiments=sentiment
                           )

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
