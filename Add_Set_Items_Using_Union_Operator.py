# Defining three sets
lang1 = {"C", "C++", "Java", "Python"}
lang2 = {"PHP", "C#", "Perl"}
lang3 = {"SQL", "C#"}

# Performing union operation 
combined_set1 = lang1.union(lang2)
combined_set2 = lang2 | lang3

# Print the combined set
print ("Combined Set1:", combined_set1)
print("Combined Set2:", combined_set2)