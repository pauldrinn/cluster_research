for file in ./clustersfasta/*.fa; do
	output="$file output"
	clustalo -i $file -o "$output"
done
