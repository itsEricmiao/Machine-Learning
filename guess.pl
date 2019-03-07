#!/usr/bin/perl
$input = <STDIN>;

#	first name and last name: John Quincy Adams
	if($input =~ /^[A-Z][a-z]+\s[A-Z][a-z]+$/g)
	{
		print "Input is: $input";
		print "It looks like a first name and last name.";
	}
	
	if($input =~ /^[A-Z][a-z]+\s+[A-Z][a-z]+\s+[A-Z][a-z]+$/g)
	{
		print "Input is: $input";
		print "It looks like a first name, middle name, and last name.";
	}
	
#	The regular expression should determine the input data is male or female: 
	$male = 'male';
	$female = 'female';
	if ($input =~ $male || $input =~ $female )
	{
		print "Input is: $input";
		print "It looks like a gender number.";
	}

#	The regular expression should check the input data is street address: 5454 Amesbury Dr
	if($input =~ /([0-9]+)(\s)([A-Z]{1})([a-z]+)(\s)([A-Z]{1})([a-z]+)/)
	{
		print "Input is: $input";
		print "It looks like a street address.";
	}
	
#	The regular expression matches the city, state and zip code: Dallas, TX 75206
	if($input =~ /([A-Z]{1})([a-z]+)(,)(\s)([A-Z]{2})(\s)([0-9]+)/g)
	{
		print "Input is: $input";
		print "It looks like a city, state and zip code.";
	}
	
#	The regular expression should match the email address 
	if ($input =~ /@/ )
	{
		print "Input is: $input";
		print "It looks like an email address.";
	}
	
#	The regular expression should match the phone number
	if ($input =~ /[0-9]{3}-[0-9]{3}-[0-9]{4}/ )
	{
		print "Input is: $input";
		print "It looks like a phone number.";
	}

#	The regular expression for currency
	if ($input =~ /\$/ )
	{
		print "Input is: $input";
		print "It looks like a currency.";
	}
	
#	The regular expression for debit or credit card number
	if ($input =~ /[0-9]{4}-[0-9]{4}-[0-9]{4}/ )
	{
		print "Input is: $input";
		print "It looks like a credit card number.";
	}
	
#	The regular expression for date
	if ($input =~ /[0-9]{4}(-)[0-9]{2}-[0-9]{2}/ )
	{
		print "Input is: $input";
		print "It looks like an date.";
	}
	if ($input =~ /[0-9]{2}(-)[0-9]{2}-[0-9]{4}/ )
	{
		print "Input is: $input";
		print "It looks like an date.";
	}
	if ($input =~ /[0-9]{2}.[0-9]{2}.[0-9]{4}/ )
	{
		print "Input is: $input";
		print "It looks like an date.";
	}
	if ($input =~ /[0-9]{4}.[0-9]{2}.[0-9]{2}/ )
	{
		print "Input is: $input";
		print "It looks like an date.";
	}
	
#	The regular expression for time  
	if ($input =~ /[0-9]{2}:[0-9]{2}/ )
	{
		print "Input is: $input";
		print "It looks like a time.";
	}
	
#	The regular expression for URL
#	if ($input =)
#		{
#			print "Input is: $input";
#			print "It looks like a URL.";
#		}
#	The regular expression for IP Address
	if ($input =~ /[0-9]{3}(.)[0-9]{3}(.)[0-9]{3}(.)[0-9]{1}/ )
	{
		print "Input is: $input";
		print "It looks like an IP address.";
	}
