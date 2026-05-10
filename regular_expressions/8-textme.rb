#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.+)\] \[to:(.+)\] \[flags:(.+)\]/).map do |s, r, f|
  "#{s},#{r},#{f}"
end.join
