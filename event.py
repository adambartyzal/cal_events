from calendar_service import calendarService
from my_dicts import calendars,times
import pprint as pretty
import pickle
import os.path

class Event:

  def __init__(self):
    """Constructor of calendar event object with default values."""
    self.service = calendarService()
    self.event = {
      'summary': '',
      'summary': 'default name',
      'start': {
        'dateTime': times['now'],
      },
      'end': {
        'dateTime': times['hourLater'],
      },
    }
    self.calendarId = calendars['personal']
    self.uploaded = False

  def calendar(self,calendarName):
    """Choose a calendar from my_dict dictionary."""
    self.calendarId = calendars[calendarName]

  def name(self,eventName):
    """Name of a calendar event (string)."""
    self.event['summary'] = eventName

  def show(self):
    """Pretty print the event."""
    #print(f'Event with Google id: {self.event['id']}')
    pretty.pprint(self.event)

  def add(self):
    """Send the event to Google Api."""
    self.event = self.service.events().insert(calendarId=self.calendarId, body=self.event).execute()
    self.uploaded = True

  def update(self):
    self.service.events().update(calendarId=self.calendarId, eventId=self.event['id'], body=self.event).execute()

  def startAt(self,time):
    self.event['start']['dateTime'] = times[time]

  def endAt(self,time):
    self.event['end']['dateTime'] = times[time]

  def save(self, filename):
    if self.uploaded:
      with open(filename, 'wb') as output:
        pickle.dump(self.event, output, pickle.HIGHEST_PROTOCOL)
    else:
      print('Event not uploaded yet!')

  def load(self, filename):
    if os.path.exists(filename):
      with open(filename, 'rb') as input:
        self.event = pickle.load(input)
        self.calendarId = self.event['organizer']['email']
        print(f'File "{filename}" sucesfully loaded.')
