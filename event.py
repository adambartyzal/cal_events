from calendar_service import calendarService
from my_dicts import calendars,times

def addEvent(calendarName,eventName,timeFrom,timeTo):
  service = calendarService()
  calendarId = calendars[calendarName]

  event = {
    'summary': eventName,
    'start': {
      'dateTime': times[timeFrom],
    },
    'end': {
      'dateTime': times[timeTo],
    },
  }

  event = service.events().insert(calendarId=calendarId, body=event).execute()
  eventId = event['id']
  print (eventId)
  return eventId

def endEventAt(calendarName,eventId,time):
  service = calendarService()
  calendarId = calendars[calendarName]

  event = service.events().get(calendarId=calendarId,eventId=eventId).execute()
  event['end']['dateTime'] = times[time]
  event = service.events().update(calendarId=calendarId, eventId=eventId, body=event).execute()

#eventId = addEvent('personal','Test','now','hourLater')

endEventAt('personal','m7ohrdgr5kkmfgtifok5bl9gdk','now')
