#!/bin/sh
exec </dev/null >> /var/log/calendar-event.log 2>&1
su adam -c 'cd /home/adam/coding/python/calendar;python work_start.py'
