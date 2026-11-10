import os

# Define the exact names of your 10 files
playlist_files = [f"list{i}.m3u" for i in range(1, 25)]
output_file = "combined_iptv_playlist.m3u"

combined_lines = []
header_added = False

print("Merging IPTV playlists...")

for filename in playlist_files:
    if not os.path.exists(filename):
        print(f"⚠️ Warning: {filename} not found, skipping.")
        continue
        
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
        for line in lines:
            # Check for the mandatory IPTV header line
            if line.strip().startswith("#EXTM3U"):
                # Only keep the very first header found across all files
                if not header_added:
                    combined_lines.append(line)
                    header_added = True
                else:
                    continue  # Skip duplicate headers
            else:
                combined_lines.append(line)

# Fallback if no files had a header
if not header_added:
    combined_lines.insert(0, "#EXTM3U\n")

# Save the unified file
with open(output_file, "w", encoding="utf-8") as out_f:
    out_f.writelines(combined_lines)

print(f"✅ Successfully created: {output_file}")
print(f"Total lines written: {len(combined_lines)}")
