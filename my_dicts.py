import datetime as dt

calendars = {
  'personal':'primary',
  'work':'d3udpuspg3qkq7on4tj1rphbco@group.calendar.google.com',
  'automated':'snjtr0iho0iulc3qm4pcp57pms@group.calendar.google.com'
}

times = {
  'now': dt.datetime.now().astimezone().isoformat(),
  'hourLater': (dt.datetime.now().astimezone() + dt.timedelta(hours=1)).isoformat(),
  'eightHoursLater': (dt.datetime.now().astimezone() + dt.timedelta(hours=8)).isoformat(),
  'today': dt.date.today().isoformat(),
  'tommorow': (dt.date.today() + dt.timedelta(days=1)).isoformat()
}
