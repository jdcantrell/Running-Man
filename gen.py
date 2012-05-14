import data;
from jinja2 import Environment, FileSystemLoader
import math
import json

def gen_page():
  # prepare data
  context = {}
  stats = {
    'miles': 0,
    'time': 0,
    'longest_run': 0,
    'best_mph': 0,
    'best_mpm': 0,
  }

  context['json'] = []
  for run in data.runs:
    context['json'].append(run.__dict__)
    stats['miles'] += run.miles
    stats['time'] += run.run_time_seconds
    if run.miles > stats['longest_run']:
      stats['longest_run'] = run.miles
      stats['longest_run_date'] = run.date
    if run.mph > stats['best_mph']:
      stats['best_mph'] = run.mph
      stats['best_mpm'] = run.mpm
      stats['best_mph_date'] = run.date


  stats['best_mph'] = round(stats['best_mph'], 2)
  stats['best_mpm'] = "%d minutes and %d seconds " % (math.trunc(stats['best_mpm']), round(float(math.ceil(stats['best_mpm']) - stats['best_mpm']) * 60.0))

  stats['avg_mph'] = round(float(stats['miles']) / float(stats['time']) * 3600.0, 2)

  avg_mpm = 1.0 / stats['avg_mph'] *  60
  stats['avg_mpm'] = "%d minutes, %d seconds " % (math.trunc(avg_mpm), round(float(math.ceil(avg_mpm) - avg_mpm) * 60.0))

  stats['time_display'] = '%d hours and %d minutes, and %d seconds' % ( stats['time'] / 3600, stats['time'] % 3600 / 60, stats['time'] % 3600 % 60)
  context['stats'] = stats
  context['last'] = data.runs.pop()
  context['json'] = json.dumps(context['json'])

  # parse template
  template_file = "run.html"
  output_file = "output/index.html"
  env = Environment(loader=FileSystemLoader('templates'))
  template = env.get_template(template_file)

  

  f = open(output_file, "w")
  f.write(template.render(context))


if __name__ == "__main__":
  gen_page()
  print "Page generated."
