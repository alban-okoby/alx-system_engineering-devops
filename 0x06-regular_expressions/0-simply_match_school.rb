#!/usr/bin/env ruby

# Check if the argument matches the regular expression /School/
def check_match(input)
  pattern = /School/
  if input =~ pattern
    puts "School"
  else
    puts ""
  end
end

# Check if an argument is provided
if ARGV.empty?
  puts "Please provide an argument"
else
  # Get the argument from the command line
  argument = ARGV[0]

  # Call the check_match function with the argument
  check_match(argument)
end
