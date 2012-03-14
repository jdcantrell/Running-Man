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
'''

runs = [
  ("2012-03-11", "19:30", 1.25, "00:25:00", 5.0, 2.9, "okay", "happy", "fresh", ["rice", "pork", "cheese"]),
  ("2012-03-13", "20:30", 1.88, "00:25:00", 6.6, 3.6, "good", "happy", "fresh", ["soda", "pasta", "water", "bread"]),
]
