import os


def check_all_fixes(folder):
  score = 0
  if os.path.exists(os.path.join(folder, 'index.html')):
    score += 10
  if os.path.exists(os.path.join(folder, 'main.js')):
    score += 5
  if os.path.exists(os.path.join(folder, 'style.css')):
    score += 5
  return score
