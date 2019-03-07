#!/usr/bin/perl
$input = <STDIN>;
#	first name and last name: John Quincy Adams
	if($input =~ /^[A-Z][a-z]+\s[A-Z][a-z]+$/g)
	{
		print "It is a name: $input";

	}
	if($input =~ /^[A-Z][a-z]+\s+[A-Z][a-z]+\s+[A-Z][a-z]+$/g)
	{
		print "It is a first name, middle name, and last name: $input";

	}
	
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
	if($input =~ /([0-9]+)(\s)([A-Z]{1})([a-z]+)(\s)([A-Z]{1})([a-z]+)/)
	{
		print "It is street address: $input";

	}
#	The regular expression matches the city, state and zip code: Dallas, TX 75206
	if($input =~ /([A-Z]{1})([a-z]+)(,)(\s)([A-Z]{2})(\s)([0-9]+)/g)
	{
		print "It is a city, state and zip code: $input";

	}
#	The regular expression should match the email address 
	if ($input =~ /@/ )
	{
		print "It is an email address: $input";
	}
#	The regular expression should match the phone number
	if ($input =~ /[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]/ )
	{
		print "Input is: $input";
		print "It looks like a phone number.";

	}

#	The regular expression for currency

	if ($input =~ /\$/ )
	{
		print "It is a Currency: $input";
	}
#	The regular expression for debit or credit card number
	if ($input =~ /[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]/ )
	{
		print "Input is: $input";
		print "It looks like a credit card number.";
	}
#	The regular expression for date
	
#	The regular expression for time  
	
#	The regular expression for URL
	
#	The regular expression for IP Address
	if ($input =~ /[0-9]{3}(.)[0-9]{3}(.)[0-9]{3}(.)[0-9]{1}/ )
	{
		print "Input is: $input";
		print "It looks like an IP address.";
	}
