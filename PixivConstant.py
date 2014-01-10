﻿#!/usr/bin/python
# -*- coding: UTF-8 -*-

PIXIVUTIL_VERSION = '20131218'
PIXIVUTIL_LINK = 'https://nandaka.wordpress.com/tag/pixiv-downloader/'
PIXIV_URL = 'http://www.pixiv.net'
PIXIV_URL_SSL = 'https://ssl.pixiv.net/login.php'
PIXIV_CSS_LIST_ID = 'display_works'
PIXIV_CSS_PROFILE_NAME_CLASS = 'f18b'
PIXIV_CSS_IMAGE_TITLE_CLASS = 'works_data'
PIXIV_CSS_TAGS_ID = 'tags'
PIXIVUTIL_MODE_UPDATE_ONLY = '1'

## Login Settings
PIXIVUTIL_MODE_OVERWRITE = '2'
PIXIV_LOGIN_URL = '/login.php'
PIXIV_FORM_NUMBER = 1
PIXIV_FORM_NUMBER_SSL = 1

## Log Settings
PIXIVUTIL_LOG_FILE = 'pixivutil.log'
PIXIVUTIL_LOG_SIZE = 10485760
PIXIVUTIL_LOG_COUNT = 10
PIXIVUTIL_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

## Download Results
PIXIVUTIL_NOT_OK = -1
PIXIVUTIL_OK = 0
PIXIVUTIL_SKIP_OLDER = 1
PIXIVUTIL_SKIP_BLACKLIST = 2
PIXIVUTIL_KEYBOARD_INTERRUPT = 3

BUFFER_SIZE = 8192
