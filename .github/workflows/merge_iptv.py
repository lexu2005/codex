import os
import glob

output_file = "combined_iptv_playlist.m3u"
combined_lines = []
header_added = False

# This automatically finds ALL files that start with 'list' and end with '.m3u'
# It works for list1.m3u, List2.M3U, list10.m3u, etc.
playlist_files = glob.glob("list*.m3u", recursive=True) + glob.glob("List*.m3u", recursive=True)
# Remove duplicate file paths if any overlap occurred
playlist_files = list(set(playlist_files))
# Sort them so they merge in order (list1, list2, etc.)
playlist_files.sort()

print(f"Found {len(playlist_files)} playlist files to merge: {playlist_files}")

if not playlist_files:
    print("❌ Error: No files starting with 'list' and ending with '.m3u' were found in the folder!")
    exit(1)

for filename in playlist_files:
    print(f"Merging: {filename}...")
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.strip().startswith("#EXTM3U"):
                if not header_added:
                    combined_lines.append(line)
                    header_added = True
            else:
                combined_lines.append(line)

if not header_added:
    combined_lines.insert(0, "#EXTM3U\n")

with open(output_file, "w", encoding="utf-8") as out_f:
    out_f.writelines(combined_lines)

print(f"✅ Successfully created: {output_file} with {len(combined_lines)} lines.")
