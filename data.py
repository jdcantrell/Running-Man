'''
This is a list of run data that I have gathered

Format:
  date, 24hr time, distance, run_time, max_speed, min_speed, feeling, food

date - YYYY-MM-DD
time - hr:min
distance - miles
time - hr:min:secs
max_speed - mph
min_speed - mph
feeling - bad, okay, good - this is a description of how I felt about the run
mood - angry, sad, happy, upset, anxious, etc - this is how I felt when I started the run
legs - sore, fresh, tired, etc - this how my legs felt before starting the run
food - list of foods eaten prior to run (the meal before), including liquids
weight - weigh in after run


Todo:
  Make this into a proper data class (Runs iterates over Run objects)
'''

from datetime import datetime

class Run:
  _ID = 0
  def __init__(self, date, time, distance, run_time, max_speed, min_speed, run_feeling, mood, leg_status, food, weight):
    self.id = Run._ID
    Run._ID += 1
    self.date_str = date
    self.time = time
    self.distance = distance
    self.run_time_display = run_time
    self.max_speed = max_speed
    self.min_speed = min_speed
    self.run_feeling = run_feeling
    self.mood = mood
    self.leg_status = leg_status
    self.food = food
    self.weight = weight
    
    #calculated values
    l = run_time.split(':')
    self.run_time_seconds = int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])
    self.average_mph = float(self.distance) / float(self.run_time_seconds) * 3600.0
    self.mile_time = 1.0 / self.average_mph *  60

  @property
  def id(self):
    return self.id

  @property
  def date(self):
    return datetime.strptime("%s %s" % (self.date_str, self.time), "%Y-%m-%d %H:%M")

  @property
  def miles(self):
    return self.distance

  @property
  def lbs(self):
    return self.weight

  @property
  def food(self):
    return self.food

  @property
  def run_feel(self):
    return self.run_feeling

  @property
  def min(self):
    return self.min_speed

  @property
  def max(self):
    return self.max_speed

  @property
  def time(self):
    return self.run_time_seconds

  @property
  def mph(self):
    return self.average_mph

  @property
  def mpm(self):
    return self.mile_time

runs = [
  Run("2012-03-11", "19:30", 1.25, "00:25:00", 5.0, 2.9, "okay", "happy", "fresh", ["rice", "pork", "cheese"], 169.8),
  Run("2012-03-13", "20:30", 1.88, "00:25:00", 6.6, 3.6, "good", "happy", "fresh", ["soda", "pasta", "water", "bread"], 169.8),
  Run("2012-03-18", "19:40", 2.05, "00:24:51", 7.0, 3.8, "good", "happy", "fresh", ["bagel", "turkey", "ham", "cheese"], 167.8),
  Run("2012-03-21", "20:12", 2.14, "00:24:47", 7.5, 4.0, "okay", "meh", "fresh", ["chicken", "noodles", "apple juice"], 168.8),
  Run("2012-04-08", "22:22", 2.16, "00:25:17", 7.5, 4.0, "okay", "meh", "fresh", [], 169.8),
  Run("2012-04-15", "20:16", 2.15, "00:24:30", 7.5, 4.0, "good", "bummed", "fresh", ["sandwich", "chips"], 166.8),
  Run("2012-04-19", "22:21", 2.17, "00:24:56", 7.5, 4.0, "good", "meh", "fresh", ["sandwich", "chips"], 169.8),
  Run("2012-04-30", "22:20", 1.92, "00:21:38", 7.5, 4.0, "good", "meh", "fresh", ["albondigas soup", "chocolate milk"], 169.8),
  Run("2012-05-02", "20:40", 1.93, "00:21:35", 7.5, 4.0, "good", "upset", "tired", ["asparagus carbonara", "chocolate milk"], 168.2),
  Run("2012-05-07", "21:50", 1.96, "00:21:40", 7.5, 4.0, "good", "good", "fresh", ["ham sandwich"], 168.7),
  Run("2012-05-10", "21:20", 2.64, "00:27:26", 7.5, 4.0, "good", "good", "fresh", ["eggs", "cream-o-wheat"], 168.6),
  Run("2012-05-12", "21:30", 2.68, "00:27:53", 7.5, 4.0, "tired", "okay", "fresh", ["taco bell", "pasta"], 166.6),
]

if __name__ == "__main__":
  for d in runs:
    print "MPH: %f MPM: %f" % (d.mph, d.mpm)
