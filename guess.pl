#!/usr/bin/perl
$input = <STDIN>;
#	first name and last name: John Quincy Adams

#	The regular expression should determine the input data is male or female: 
	
#	The regular expression should check the input data is street address: 5454 Amesbury Dr
	
#	The regular expression matches the city, state and zip code: Dallas, TX 75206

#	The regular expression should match the email address 
	if ($input == ~/(@)/ )
	{
		print "It is an email address: $input";
	}else {
		print "It is NOT an email address: $input";
	}
#	The regular expression should match the phone number

#	The regular expression for currency
	
#	The regular expression for Monetary Input: $55.00 or $0.75, etc 
	if ($input == ~/$/ )
	{
		print "It is a Currency: $input";
	}else {
		print "It is NOT an Currency: $input";
	}
#	The regular expression for debit or credit card number
	
#	The regular expression for date
	
#	The regular expression for time  
	
#	The regular expression for URL
	
#	The regular expression for IP Address

