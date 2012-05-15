from __future__ import with_statement
from fabric.api import local, run, cd
from fabric.decorators import hosts
from fabric.colors import blue, green, yellow

#TODO: Re-organize site so that the main blog is not in the base directory
#this will prevent the stream pages (and anything else that is evntually added
#from getting destroyed on deploy

@hosts('jd@goodrobot.net')
def deploy():
  code_dir = "~/apps/Running-Man"
  
  #actually generate the site
  with cd(code_dir):
    print(blue("Updating Running-Man..."))
    run("git pull")
    print(yellow("Generating output..."))
    run("python gen.py")

  print(green("Boom! An update explodes on to the internet scene."))
