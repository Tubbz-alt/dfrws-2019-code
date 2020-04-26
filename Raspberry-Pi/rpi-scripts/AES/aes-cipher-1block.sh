#!/bin/bash

while true
do
	echo -n "1" > /dev/udp/192.168.3.1/5005
	# wait till the message is delivered (a rough time)
	sleep 0.002

	openssl aes-256-cbc -in short-message.txt -out ciphertext.aes -pass pass:asanka 2>/dev/null
	 
	# wait till the message is delivered (a rough time)
	# longer because capturing through gnuradio often gets delayed as more traces are captured
	sleep 0.150

	echo -n "-1" > /dev/udp/192.168.3.1/5005
	#openssl aes-256-cbc -d -in ciphertext.aes -out decrypted.txt -pass pass:asanka

	#echo "next..."
	sleep 1
done

