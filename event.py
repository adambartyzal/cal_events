from calendar_service import calendarService
from my_dicts import calendars,times
import pprint as pretty

class Event:

  def __init__(self):
    self.service = calendarService()
    self.event = {
      'summary': 'default name',
      'start': {
        'dateTime': times['now'],
      },
      'end': {
        'dateTime': times['hourLater'],
      },
    }
    self.calendarId = calendars['personal']
    self.eventId = 'not yet uploaded'

  def calendar(self,calendarName):
    self.calendarId = calendars[calendarName]

  def name(self,eventName):
    self.event['summary'] = eventName

  def show(self):
    print(f'Event with Google id: {self.eventId}')
    pretty.pprint(self.event)

  def add(self):
    event = self.service.events().insert(calendarId=self.calendarId, body=self.event).execute()
    self.eventId = event['id']

  def update(self):
    self.service.events().update(calendarId=calendarId, eventId=eventId, body=event).execute()

  def startAt(self,time):
    self.event['start']['dateTime'] = times[time]

  def endAt(self,time):
    self.event['end']['dateTime'] = times[time]