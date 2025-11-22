#!/usr/bin/env bash
# Script to organize and archive CSV files with timestamped names and log the operations.
ARCHIVE_dir="/mnt/c/Users/HP/OneDrive/Desktop/summative/-Lab01---brina-cloud-/archive"
if [ ! -d "$ARCHIVE_dir" ]; then
    mkdir "$ARCHIVE_dir"
fi

log="organizer.log"
touch "$log"

for file in $(find . -maxdepth 1 -type f -name "*.csv"); do
    TIMEASTAMP=$(date +%Y%m%d%H%M%S)
    basename=$(basename "$file")
    new_name="${basename%.csv}-${TIMEASTAMP}.csv"
    
    {
        echo "Archived File: $file -> $ARCHIVE_dir/$new_name"
        echo "Timestamp: $TIMEASTAMP"
        echo "Content:"
        cat "$file" 
        echo "\n-----------------------\n"
    } >> "$log"
    mv "$file" "$ARCHIVE_dir/$new_name"
    echo "Archived $file to $ARCHIVE_dir/$new_name."
done
