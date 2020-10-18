from calendar_service import calendarService
from my_dicts import calendars,times
import pprint as pretty
import pickle
import os.path
import sys

class Event:
  """Class for handling Google Calenadar API"""

  def __init__(self):
    """Constructor of calendar event object with default values"""
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
    """Chooses a calendar from my_dict"""
    self.calendarId = calendars[calendarName]

  def name(self,eventName):
    """Name of a calendar event (string)"""
    self.event['summary'] = eventName

  def show(self):
    """Pretty print the event"""
    print(f"Event with Google id: {self.event['id']}")
    pretty.pprint(self.event)

  def add(self):
    """Send the event to Google Api"""
    self.event = self.service.events().insert(calendarId=self.calendarId, body=self.event).execute()
    self.uploaded = True

  def update(self):
    """Updates the body of the event on remote server"""
    self.service.events().update(calendarId=self.calendarId, eventId=self.event['id'], body=self.event).execute()
    print(f"Event {self.event['id']} updated.")

  def startAt(self,time):
    """Start time from my_dict.py"""
    self.event['start']['dateTime'] = times[time]

  def endAt(self,time):
    """End time from my_dict.py"""
    self.event['end']['dateTime'] = times[time]

  def save(self, filename):
    """Saves body of event using pickle (string)"""
    if self.uploaded:
      with open(filename, 'wb') as output:
        pickle.dump(self.event, output, pickle.HIGHEST_PROTOCOL)
        print(f"Event {self.event['id']} saved to {filename} file.")
    else:
      print('Event not uploaded yet!',file=sys.stderr)
      sys.exit()

  def load(self, filename):
    """Loads body of event using pickle (string)"""
    if os.path.exists(filename):
      with open(filename, 'rb') as input:
        self.event = pickle.load(input)
        self.calendarId = self.event['organizer']['email']
        print(f'File "{filename}" sucesfully loaded.')
    else:
      print('File does not exist!', file=sys.stderr)
      sys.exit()
