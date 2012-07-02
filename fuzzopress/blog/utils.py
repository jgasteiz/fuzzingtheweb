# -*- coding: utf-8 -*-
import re
from django.utils.encoding import smart_unicode
from types import UnicodeType

def uuslug(s, instance=None):
    """This method tries a little harder than django's django.template.defaultfilters.slugify.

    Parameters
    ----------
    s : string
        Must
    instance : Model object or None, optional
        If instance received, checks the slug is unique

    Returns
    -------
    slug : string
        sluged string received as parameter

    Examples
    --------
    Example usage in save method for model:

    import uuslug as slugify
    self.slug = slugify(self.title, instance=self)

    Notes
    -----

    Taken from an old snippet, no longer available online
    """

    if type(s) != UnicodeType:
        s = unicode(s, 'utf-8', 'ignore')
    s = smart_unicode(s)

    # replace unwanted characters
    s = re.sub(r'[\']+', '', s.lower()) # replace ' with nothing instead with -
    s = re.sub(r'[^-a-z0-9]+', '-', s.lower())

    # remove redundant -
    s = re.sub('-{2,}', '-', s).strip('-')

    slug = s

    # If an instance is passed
    if instance:
        def get_query():
            # Adapted to app engine datastore
            query = instance.__class__.objects.filter(slug=slug)
            return query
        counter = 1
        # This assures the slug is unique
        while get_query():
            slug = "%s-%s" % (s, counter)
            counter += 1
    return slug
