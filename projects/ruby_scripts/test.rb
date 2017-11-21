#!/usr/bin/ruby -w

while true do
	puts "enter first number";
	A = gets.chomp;
	puts "enter second number";
	B = gets.chomp;

	puts "enter third number";
	C = gets.chomp;
	if C == nil
		puts ""
		puts Z = A.to_i * B.to_i;
	else
		puts Z = A.to_i * B.to_i * C.to_i;
	end
	puts ""
	A,B,C = nil
end
