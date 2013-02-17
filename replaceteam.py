"""
A sphinx extension that replaces the ``team.rst`` file with the credits file
from the astropy repository.

Note that this first looks for the ``ASTROPY_REPO_PATH`` environment
variable to try to find a local copy of the astropy repo.
"""


def setup(app):
    app.connect('source-read', replace_team)


def replace_team(app, docname, source):
    if docname == 'team':

        credits = get_astropy_credits(app.warn).decode('utf-8')

        if credits is not False:
            creditslines = credits.split('\n')

            newcreditslines = []
            for l in creditslines:
                # replace section headings with the correct type of heading for web site
                if l.startswith('==='):
                    l = l.replace('=', '-')
                newcreditslines.append(l)

            #replace the title block
            newcreditslines[0] = ''
            newcreditslines[1] = 'The Astropy Team'
            newcreditslines[2] = '================'

            #add the orphan marker
            newcreditslines.insert(0, ':orphan:')

            # now actually use the new source - this is what sphinx processes
            source[0] = '\n'.join(newcreditslines)


def get_astropy_credits(warner):
    """
    Looks for the ``credits.rst`` file in the astropy repo and returns it, or
    returns False if the repo can't be found.
    """
    import os
    from urllib2 import urlopen

    creditspath = os.environ.get('ASTROPY_REPO_PATH',
        'http://raw.github.com/astropy/astropy/master/docs/credits.rst')

    if creditspath.startswith('http'):
        #url - download page from web
        u = None
        try:
            u = urlopen(creditspath)
            return u.read()
        except Exception as e:
            warner('Could not download credits.rst from requested path: "{0}" Using placeholder for "The Team" page.'.format(e))
            return False
        finally:
            if u is not None:
                u.close()
    else:
        if not os.path.isfile(creditspath):
            warner('Credits.rst file at "{0}" is not a file! Using placeholder for "The Team" page.'.format(creditspath))
            return False

        with open(creditspath) as f:
            return f.read()
