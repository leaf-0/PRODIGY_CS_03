def check_password_strength(password):
  strength_score = 0
  feedback_message = ""

  if len(password) >= 12:
    strength_score += 2
  elif len(password) >= 8:
    strength_score += 1
  else:
    feedback_message += "Password is too short. Use at least 8 characters.\n"

  # Check for uppercase letters
  if any(char.isupper() for char in password):
    strength_score += 1

  # Check for lowercase letters
  if any(char.islower() for char in password):
    strength_score += 1

  # Check for numbers
  if any(char.isdigit() for char in password):
    strength_score += 1

  # Check for special characters
  if any(char in "!@#$%^&*()" for char in password):
    strength_score += 1

  # Determine strength rating based on score
  if strength_score >= 5:
    strength_rating = "Strong"
  elif strength_score >= 3:
    strength_rating = "Medium"
  else:
    strength_rating = "Weak"

  if not feedback_message:
    feedback_message = "Good password!"
  else:
    feedback_message += "Consider using a mix of uppercase, lowercase letters, numbers, and special characters."

  return strength_score, strength_rating, feedback_message


password = input("Enter your password: ")

strength_score, strength_rating, feedback_message = check_password_strength(password)

# Print results
print(f"Strength Score: {strength_score}")
print(f"Strength Rating: {strength_rating}")
print(f"\nFeedback:\n{feedback_message}")
