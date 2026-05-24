import re

with open('presentation.html', 'r') as f:
    content = f.read()

# Update total slides text
for i in range(1, 14):
    content = content.replace(f'Slide {i:02d} / 14', f'Slide {i:02d} / 15')
content = content.replace('Slide 14 / 14', 'Slide 15 / 15')

# Update id of old slide 14
content = content.replace('id="slide-14"', 'id="slide-15"')

# Update slide total
content = content.replace('<span class="slide-counter-total" id="slide-total">14</span>', '<span class="slide-counter-total" id="slide-total">15</span>')

new_slide = """      <!-- Slide 14: Effectiveness, Efficiency, Productivity -->
      <div
        class="slide"
        id="slide-14"
        data-notes-timing="2"
        data-notes-cumulative="31"
        data-notes-priority="essential"
        data-notes-points="Define Effectiveness: doing right things (What/Why);Define Efficiency: doing things right (How);Define Productivity: consistently delivering right things, right;Explain Systems Thinking perspective - high efficiency + low effectiveness = shipping wrong things perfectly"
      >
        <div class="slide-header">
          <span class="topic-tag">
            <svg class="inline-star" width="14" height="14" fill="currentColor">
              <use href="#icon-star" />
            </svg>
            System Dynamics
          </span>
          <span>Slide 14 / 15</span>
        </div>
        <h3 class="assertion">
          Mixing up Effectiveness, Efficiency, and Productivity leads to shipping the wrong things, incredibly fast.
        </h3>
        <div class="evidence">
          <div class="grid-3" style="margin-bottom: 2rem;">
            <div class="card" style="padding: 1.5rem;">
              <h4 style="margin-bottom: 0.5rem; color: var(--primary);">Effectiveness</h4>
              <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem; font-weight: 600;">The "What" and "Why"</p>
              <p style="font-size: 0.95rem;">Doing the <strong>right things</strong>. Hitting the target, achieving the goal, and delivering value to the user.</p>
            </div>
            <div class="card" style="padding: 1.5rem;">
              <h4 style="margin-bottom: 0.5rem; color: var(--accent);">Efficiency</h4>
              <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem; font-weight: 600;">The "How"</p>
              <p style="font-size: 0.95rem;">Doing things <strong>right</strong>. Optimizing resources, reducing waste, and minimizing costs.</p>
            </div>
            <div class="card accent-card" style="padding: 1.5rem;">
              <h4 style="margin-bottom: 0.5rem; color: var(--text-main);">Productivity</h4>
              <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem; font-weight: 600;">The Net Result</p>
              <p style="font-size: 0.95rem;">Consistently delivering the right things, right. The combination of effectiveness and efficiency over time.</p>
            </div>
          </div>

          <div>
            <h4 style="margin-bottom: 1rem; color: var(--text-main); font-family: var(--font-serif); font-weight: 500;">The Systems Thinking Perspective</h4>
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
              <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; padding: 1rem; background: var(--bg-page); border: 1px solid var(--border); border-radius: 8px;">
                <strong style="color: var(--text-main);">High Efficiency + Low Effectiveness</strong>
                <span style="color: var(--text-muted);">Shipping the wrong feature, perfectly and ahead of schedule.</span>
              </div>
              <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; padding: 1rem; background: var(--bg-page); border: 1px solid var(--border); border-radius: 8px;">
                <strong style="color: var(--text-main);">Low Efficiency + High Effectiveness</strong>
                <span style="color: var(--text-muted);">Solving the right problem, but taking too long (or burning too much budget).</span>
              </div>
              <div style="display: grid; grid-template-columns: 1fr 2fr; gap: 1rem; padding: 1rem; background: var(--primary-light); border: 1px solid var(--primary); border-radius: 8px;">
                <strong style="color: var(--primary);">High Efficiency + High Effectiveness</strong>
                <span style="color: var(--text-main); font-weight: 600;">True Productivity.</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Slide 15: Q&A Closing -->"""

content = content.replace('<!-- Slide 14: Q&A Closing -->', new_slide)

with open('presentation.html', 'w') as f:
    f.write(content)

print("Done updating presentation.html")
