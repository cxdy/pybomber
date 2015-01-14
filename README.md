SMS & Email Bomber 
====================

A lightweight SMS &amp; Email Bomber, made in Python.


Requirements
====================

Python 2.7.6

A Text Editor

A Gmail account (Cock.li is no longer supported due to a complaint)

Usage
====================

Run it.
Use numbers to navigate.

Adding carriers
====================

Carrier list can be found here; http://www.emailtextmessages.com/

Remove the 'phonenumber' part!

Let's say we were going to add Boost Mobile.

As you can see, the code is in numerical order. So, you'd go to line 61 and get to a new line, and type this:

<pre><code>if carrier == 10:
	carrier_attack = "@myboostmobile.com"</code></pre>
	
Notice how I changed the carrier number and the SMS gateway. As on the site, it was phonenumber@carrier.com. Remove that phone number part. The program puts the number you supply in. 

You can do this as many times as you want! Add all of the carriers if you're feeling that ambitious. 
Hey, maybe you'd like to commit it to the file? Go for it!
