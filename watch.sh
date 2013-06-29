#!/usr/bin/env bash

sass --watch --compass blog/static/scss/base.scss:blog/static/css/base.css
sass --watch --compass blog/static/scss/base-admin.scss:blog/static/css/base-admin.css
sass --watch --compass blog/static/scss/error.scss:blog/static/css/error.css