#Eric Miao
#CSE-3342
#Programming Assignment 5: Perl with Regex

#!/usr/bin/perl
$male = 'male';
$female = 'female';
while ($input = <STDIN>) {
	$input_lowercase = lc $input;
#	first name and last name: John Quincy Adams
	if($input =~ /^[A-Z][a-z]+\s[A-Z][a-z]+$/g)
	{
		print "Input is: $input";
		print "It looks like a first name and last name.";
	}
	elsif($input =~ /^[A-Z][a-z]+\s+[A-Z][a-z]+\s+[A-Z][a-z]+$/g)
	{
		print "Input is: $input";
		print "It looks like a first name, middle name, and last name.";
	}
	elsif($input =~ /^[A-Z][a-z]+\s+[A-Z]+\s+[A-Z][a-z]+$/g)
	{
		print "Input is: $input";
		print "It looks like a first name, middle name, and last name.";
	}
	
#	The regular expression should determine the input data is male or female: 
	elsif ($input_lowercase =~ $male)
	{
		print "Input is: $input";
		print "It looks like a gender.";
	}
	
	elsif ($input_lowercase =~ $female)
	{
		print "Input is: $input";
		print "It looks like a gender.";
	}

#	The regular expression should check the input data is street address: 5454 Amesbury Dr
	elsif($input =~ /([0-9]+)(\s)([A-Z]{1})([a-z]+)(\s)([A-Z]{1})([a-z]+)/)
	{
		print "Input is: $input";
		print "It looks like a street address.";
	}
	
#	The regular expression matches the city, state and zip code: Dallas, TX 75206
	elsif($input =~ /([A-Z]{1})([a-z]+)(,)(\s)([A-Z]{2})(\s)([0-9]+)/g)
	{
		print "Input is: $input";
		print "It looks like a city, state and zip code.";
	}
	
#	The regular expression should match the email address 
	elsif ($input =~ /@/ )
	{
		print "Input is: $input";
		print "It looks like an email address.";
	}
	
#	The regular expression should match the phone number
	elsif ($input =~ /[0-9]{3}-[0-9]{3}-[0-9]{4}/ )
	{
		print "Input is: $input";
		print "It looks like a phone number.";
	}

#	The regular expression for currency
	elsif ($input =~ /\$/ )
	{
		print "Input is: $input";
		print "It looks like a currency.";
	}
	
#	The regular expression for debit or credit card number
	elsif ($input =~ /[0-9]{4}-[0-9]{4}-[0-9]{4}/ )
	{
		print "Input is: $input";
		print "It looks like a credit card number.";
	}
	
#	The regular expression for date
	elsif ($input =~ /[0-9]{4}(-)[0-9]{2}-[0-9]{2}/ )
	{
		print "Input is: $input";
		print "It looks like an date.";
	}
	elsif ($input =~ /[0-9]{2}(-)[0-9]{2}-[0-9]{4}/ )
	{
		print "Input is: $input";
		print "It looks like an date.";
	}
	elsif ($input =~ /[0-9]{2}.[0-9]{2}.[0-9]{4}/ )
	{
		print "Input is: $input";
		print "It looks like an date.";
	}
	elsif ($input =~ /[0-9]{4}.[0-9]{2}.[0-9]{2}/ )
	{
		print "Input is: $input";
		print "It looks like an date.";
	}
	
#	The regular expression for time  
	elsif ($input =~ /[0-9]{2}:[0-9]{2}/ )
	{
		print "Input is: $input";
		print "It looks like a time.";
	}
	
#	The regular expression for URL
	elsif ($input_lowercase =~ /^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/ )
	{
			print "Input is: $input";
			print "It looks like an URL.";
	}
		
#	The regular expression for IP Address
	elsif ($input =~ /[0-9]{3}(.)[0-9]{3}(.)[0-9]{3}(.)[0-9]{1}/ )
	{
		print "Input is: $input";
		print "It looks like an IP address.";
	}else {
		{
			print "I don't know what it is... $input";
		}
	}
	print "\n";
	print "\n";

}