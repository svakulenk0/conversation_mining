for f in *.json
do
	echo "Processing $f file...";
	mongoimport --file $f -d cm -c dstc6;
done
