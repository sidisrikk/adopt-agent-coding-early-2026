import re

with open('presentation.html', 'r') as f:
    html = f.read()

pattern = re.compile(r'^\s*<!-- Slide \d+:.*$', re.MULTILINE)
matches = list(pattern.finditer(html))

slides = []
for i in range(len(matches)):
    start = matches[i].start()
    if i < len(matches) - 1:
        end = matches[i+1].start()
    else:
        end_match = re.search(r'^\s*</div>\s*<!-- Keyboard Navigation', html[start:], re.MULTILINE)
        end = start + end_match.start()
    
    slides.append(html[start:end])

prefix = html[:matches[0].start()]
suffix = html[end:]

# Swap 12 and 13 (indices 11 and 12)
slides[11], slides[12] = slides[12], slides[11]

# Re-number and calculate cumulative time
cumulative = 0
for i in range(len(slides)):
    new_num = i + 1
    s = slides[i]
    
    s = re.sub(r'(<!-- Slide )\d+(:)', r'\g<1>' + str(new_num) + r'\2', s, count=1)
    s = re.sub(r'(id="slide-)\d+(")', r'\g<1>' + str(new_num) + r'\2', s, count=1)
    s = re.sub(r'(>Slide )\d+( / 15<)', r'\g<1>' + f'{new_num:02d}' + r'\2', s, count=1)
    
    m = re.search(r'data-notes-timing="(\d+)"', s)
    if m:
        timing = int(m.group(1))
    else:
        timing = 0
    cumulative += timing
    s = re.sub(r'(data-notes-cumulative=")\d+(")', r'\g<1>' + str(cumulative) + r'\2', s, count=1)
    
    slides[i] = s

# Update progress tracker
old_tracker = """      <div class="tracker-step" data-target="11" data-section="ecosystem">
        Ecosystem
      </div>
      <div class="tracker-step" data-target="14" data-section="discussion">
        Discussion
      </div>"""

new_tracker = """      <div class="tracker-step" data-target="11" data-section="ecosystem">
        Ecosystem
      </div>
      <div class="tracker-step" data-target="12" data-section="system-dynamics">
        System Dynamics
      </div>
      <div class="tracker-step" data-target="15" data-section="discussion">
        Discussion
      </div>"""

if old_tracker in prefix:
    prefix = prefix.replace(old_tracker, new_tracker)
else:
    print("Could not find old progress tracker to replace!")

with open('presentation.html', 'w') as f:
    f.write(prefix + ''.join(slides) + suffix)

print("Done swapping and updating tracker.")
