import copy

original_dict = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Data Science"],
    "education": {
      "degree": "Bachelor's",
      "field": "Computer Science"
   }
}

# Creating a deep copy
deep_copy = copy.deepcopy(original_dict)

# Modifying the deep copy
deep_copy["age"] = 26
deep_copy["skills"].append("Machine Learning")
deep_copy["education"]["degree"] = "Master's"

# Retrieving both dictionaries
print("Original dictionary:", original_dict)
print("Deep copy:", deep_copy)