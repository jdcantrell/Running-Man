# A sample Guardfile
# More info at https://github.com/guard/guard#readme

# Add files and commands to this file, like the example:
#   watch(%r{file/path}) { `command(s)` }
#
# Add files and commands to this file, like the example:
#   watch(%r{file/path}) { `command(s)` }
#
guard 'shell' do
  watch( %r{.*py} ) {|m| `python gen.py` }
  watch( %r{templates/.*html} ) {|m| `python gen.py` }
  watch( %r{.*js} ) {|m| `python gen.py` }
end
