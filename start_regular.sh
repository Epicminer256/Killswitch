echo "Outward IP To Listed> "
ip=$(/sbin/ip -o -4 addr list wlan0 | awk '{print $4}' | cut -d/ -f1)
echo "Days till expire (Leave blank for infinite)> "
read exp

clear
cd epicdnschef

../bin/python3 dnschef.py -i $ip --fakeip $ip --fakeipv6 $ip --fakedomains toggle.securly.com,signon.clever.com &

cd ..

./bin/python3 webserver.py $ip $exp
