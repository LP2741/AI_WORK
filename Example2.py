### 🎯 NumPy Array - Student Scores

import numpy as np

# Rows: Students, Columns: Math, Science, English
scores = np.array([[85, 90, 88],
                   [78, 82, 80],
                   [92, 95, 90],
                   [70, 75, 72]])

# 1. Find average score per student (row mean)
avg_per_student = np.mean(scores, axis=1)
print("Average score per student:", avg_per_student)

# 2. Find average score per subject (column mean)
avg_per_subject = np.mean(scores, axis=0)
print("Average score per subject (Math, Science, English):", avg_per_subject)

# 3. Find the highest overall score
highest_score = np.max(scores)
print("Highest overall score:", highest_score)
