# Matrimony Matching using simple logic

def match_profiles(user, candidates):
    matches = []
    for candidate in candidates:
        score = 0
        if user['age'] == candidate['age']:
            score += 1
        if user['religion'] == candidate['religion']:
            score += 1
        if user['education'] == candidate['education']:
            score += 1
        if score >= 2:
            matches.append(candidate)
    return matches

# Example user
user_profile = {
    "age": 25,
    "religion": "Hindu",
    "education": "BTech"
}

# Example candidates
candidates = [
    {"name": "Akhil", "age": 25, "religion": "Hindu", "education": "BTech"},
    {"name": "Sneha", "age": 24, "religion": "Christian", "education": "BSc"},
    {"name": "Priya", "age": 25, "religion": "Hindu", "education": "MBA"},
]

# Show matches
matched = match_profiles(user_profile, candidates)
print("Matches Found:")
for m in matched:
    print(m["name"])
