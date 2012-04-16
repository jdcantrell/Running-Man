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


class Run:
  def __init__(self, date, time, distance, run_time, max_speed, min_speed, run_feeling, mood, leg_status, food, weight):
    self.date = date
    self.time = time
    self.distance = distance
    self.run_time = run_time
    self.max_speed = max_speed
    self.min_speed = min_speed
    self.run_feeling = run_feeling
    self.mood = mood
    self.leg_status = leg_status
    self.food = food
    self.weight = weight
    
    #calculated values
    #run_time in seconds
    #avg speed
#calories?

runs = [
  Run("2012-03-11", "19:30", 1.25, "00:25:00", 5.0, 2.9, "okay", "happy", "fresh", ["rice", "pork", "cheese"], 169.8),
  Run("2012-03-13", "20:30", 1.88, "00:25:00", 6.6, 3.6, "good", "happy", "fresh", ["soda", "pasta", "water", "bread"], 169.8),
  Run("2012-03-18", "19:40", 2.05, "00:24:51", 7.0, 3.8, "good", "happy", "fresh", ["bagel", "turkey", "ham", "cheese"], 167.8),
  Run("2012-03-21", "20:12", 2.14, "00:24:47", 7.5, 4.0, "okay", "meh", "fresh", ["chicken", "noodles", "apple juice"], 168.8),
  Run("2012-03-21", "20:12", 2.14, "00:24:47", 7.5, 4.0, "okay", "meh", "fresh", ["chicken", "noodles", "apple juice"], 168.8),
  Run("2012-04-08", "22:22", 2.16, "00:25:17", 7.5, 4.0, "okay", "meh", "fresh", [], 169.8),
  Run("2012-04-15", "20:16", 2.15, "00:24:30", 7.5, 4.0, "good", "bummed", "fresh", ["sandwich", "chips"], 166.8),
]
