#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-12-15 22:07:04 (CST)
# Last Update: Thursday 2018-07-26 10:45:40 (CST)
#          By:
# Description:
# **************************************************************************
from urllib.parse import urljoin

from flask import current_app, render_template, request, url_for
from werkzeug.contrib.atom import AtomFeed

from forums.api.topic.models import Topic
from forums.api.utils import gen_topic_filter, gen_topic_orderby
from forums.common.utils import gen_filter_dict, gen_order_by
from forums.common.views import BaseMethodView as MethodView

from .models import Tags


class TagsListView(MethodView):
    per_page = 99

    def get(self):
        query_dict = request.data
        page, number = self.pageinfo
        keys = ['name']
        order_by = gen_order_by(query_dict, keys)
        filter_dict = gen_filter_dict(query_dict, keys)
        tags = Tags.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number, True)
        data = {'title': 'Tags', 'tags': tags}
        return render_template('tag/tag_list.html', **data)


class TagsView(MethodView):
    def get(self, name):
        page, number = self.pageinfo
        tag = Tags.query.filter_by(name=name).first_or_404()
        topics = self.topics(tag)
        data = {'title': tag.name, 'tag': tag, 'topics': topics}
        return render_template('tag/tag.html', **data)

    def topics(self, tag):
        query_dict = request.data
        page, number = self.pageinfo
        keys = ['name']
        # order_by = gen_order_by(query_dict, keys)
        # filter_dict = gen_filter_dict(query_dict, keys)
        order_by = gen_topic_orderby(query_dict, keys)
        filter_dict = gen_topic_filter(query_dict, keys)
        filter_dict.update(tags__id=tag.id)
        return Topic.query.filter_by(
            **filter_dict).order_by(*order_by).paginate(page, number, True)


class TagFeedView(MethodView):
    def get(self, name):
        setting = current_app.config.get('SITE', {
            'title': '',
            'description': ''
        })
        title = setting['title']
        description = setting['description']
        feed = AtomFeed(
            '%s·%s' % (name, title),
            feed_url=request.url,
            url=request.url_root,
            subtitle=description)
        topics = Topic.query.filter_by(tags__name=name).limit(10)
        for topic in topics:
            if topic.content_type == Topic.CONTENT_TYPE_MARKDOWN:
                content = topic.content
            else:
                content = topic.content
            feed.add(topic.title,
                     content,
                     content_type='html',
                     author=topic.author.username,
                     url=urljoin(
                         request.url_root,
                         url_for(
                             'topic.topic', topicId=topic.id)),
                     updated=topic.updated_at,
                     published=topic.created_at)
        return feed.get_response()
