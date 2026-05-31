#!/usr/bin/env ruby

args = ARGV

numbers = []
others = []

args.each do |a|
  if a.match?(/^[-]?\d+$/)
    numbers << a.to_i
  else
    others << a
  end
end

numbers.sort.each { |n| puts n }
others.sort.each { |s| puts s }
