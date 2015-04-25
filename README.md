Plug in Decawaves, wait until screen popluates, plug in buspirate

Run with ./kratos_decawave

If you ever get a screen ful of syncing errors
	screen /dev/kratos_decawave 115200
		Then hit enter a few times to get things sending
	?
		This should pull up menu of things you can do
	#
		This should reset the buspirate
	cntl-k
	a
	y
		This exits screen. Unplug-replug buspirate and try code again