# -*- coding: utf-8 -*-
import re
from types import UnicodeType
from django.db.models import Q
from xml.dom.minidom import parse
from django.utils.encoding import smart_unicode


def uuslug(s, instance=None):
    """ This method tries a little harder than django's 
        django.template.defaultfilters.slugify.

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

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """ Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    
    """
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    """ Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
    
    """
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def restore_wp_entries(xml_path, instance):
    """ Import your wordpress entries from a wordpress backup xml

        Parameters
        ----------
        xml_path : string
            Must
            The absolute path of the wordpress backup xml
        instance : Post object
            Must
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
