mkdir -p aligned_clusters

for FILE in separated_clusters/*.fa; do
	NAME="${FILE##*/}"
    OUTPUT="aligned_clusters/${NAME%%.*}_aligned.fa"
	clustalo -i $FILE -o "$OUTPUT" --auto
    echo "$NAME aligned"
done