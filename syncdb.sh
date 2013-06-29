#!/usr/bin/env bash

rm fuzzopress.sqlite
python manage.py syncdb --noinput