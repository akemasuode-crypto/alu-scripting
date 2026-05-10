#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.+)\] \[to:(.+)\] \[flags:(.+)\]/).map do |sender, receiver, flags|
  "#{sender},#{receiver},#{flags}"
end.join
