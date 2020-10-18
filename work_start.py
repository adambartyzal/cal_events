from event import Event

ev = Event()
ev.name('Freebike')
ev.calendar('work')
ev.endAt('eightHoursLater')
ev.add()
ev.save('work_event')
