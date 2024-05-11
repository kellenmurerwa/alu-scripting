#!/usr/bin/env ruby
puts RGV[0].scan(/^\d{10}$/).join
#^\d[0-9]{10,10}$
#\d{10,10}$