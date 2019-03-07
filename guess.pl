#!/usr/bin/perl
$input = <STDIN>;
#	first name and last name: John Quincy Adams

#	The regular expression should determine the input data is male or female: 
	$male = 'male';
	$female = 'female';
	if ($input =~ $male )
	{
			print "It is an gender: $input";
	}
	if ($input =~ $female )
	{
			print "It is an gender: $input";
	}
#	The regular expression should check the input data is street address: 5454 Amesbury Dr
	
#	The regular expression matches the city, state and zip code: Dallas, TX 75206

#	The regular expression should match the email address 
	if ($input =~ /@/ )
	{
		print "It is an email address: $input";
	}
#	The regular expression should match the phone number

#	The regular expression for currency

	if ($input =~ /($)/ )
	{
		print "It is a Currency: $input";
	}
#	The regular expression for debit or credit card number
	
#	The regular expression for date
	
#	The regular expression for time  
	
#	The regular expression for URL
	
#	The regular expression for IP Address

