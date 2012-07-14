# -*- coding: utf-8 -*-
import re
from types import UnicodeType
from xml.dom.minidom import parse
from django.utils.encoding import smart_unicode


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
    s = re.sub(r'[\']+', '', s.lower())  # replace ' with nothing instead with -
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


def restore_wp_entries(xml_path, instance):
    """
    Import your wordpress entries from a wordpress backup xml

    Parameters
    ----------
    xml_path : string
        Must
        The absolute path of the wordpress backup xml
    instance : Post object
        Must

    Examples
    --------
    Example usage in save method for model:

    import restore_wp_entries
    restore_wp_entries('/Users/jgasteiz/Downloads/entries.xml')

    Notes
    -----
    Works with wordpress 3.3 and you'll need to adapt to your Post model
    """
    dom1 = parse(xml_path)
    for i in dom1.getElementsByTagName('item'):
        title = i.getElementsByTagName('title')[0].firstChild.nodeValue.encode('utf-8')
        body = i.getElementsByTagName('content:encoded')[0].firstChild.nodeValue.encode('utf-8')
        created = i.getElementsByTagName('wp:post_date')[0].firstChild.nodeValue.encode('utf-8')
        updated_at = i.getElementsByTagName('wp:post_date')[0].firstChild.nodeValue.encode('utf-8')
        published = i.getElementsByTagName('wp:post_date')[0].firstChild.nodeValue.encode('utf-8')
        instance.__class__(title=title,
            body=body,
            created=created,
            updated_at=updated_at,
            published=published).save()
