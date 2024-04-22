#!/bin/awk -f

BEGIN {
	# ARGC holds the amount of files to be parsed, including the awk binary so we must purge that
	total_files = ARGC - 1

	print("Initiating verification...\n");
}

# if you want to disconsider other lines, add to this rule with "&&"
NF { lines_parsed ++ }

END {
	average = lines_parsed / total_files
	total_lines = NR

	printf("A total of %d file(s) has been parsed.", total_files);
	printf(" Lines checked (total): %d.\n", total_lines)
	printf("Total of parsed lines: %d.", lines_parsed)
	printf(" Average of %.2f lines per file.\n", average)
}
