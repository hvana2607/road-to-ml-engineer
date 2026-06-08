# #list
# names = ["Ravi", "Priya", "Bo", "Arjun", "Sam", "Lakshmi"]

# # Your job: using a list comprehension, make this:
# # ["Priya", "Arjun", "Lakshmi"]

# result = [n for n in names if len(n)>4]

# print(result)

# numbers = [3, 15, 7, 22, 10, 18, 5]

# # Your job: make this:
# # [45, 66, 54]

# result = [n*3 for n in numbers if n>10]

# print(result)


# sentences = [
#     "i love python",
#     "java is okay",
#     "python is great for ai",
#     "i like coffee",
#     "python pays well",
# ]

# # Your job: make this:
# # ['I LOVE PYTHON', 'PYTHON IS GREAT FOR AI', 'PYTHON PAYS WELL']

# result = [n.upper() for n in sentences if "python" in n]

# print(result)

# prices_usd = [10, 75, 25, 100, 5, 60, 30]

# # Your job: make this:
# # [830, 2075, 415, 2490]

# result = [n*83 for n in prices_usd if n<50]

# print(result)

# words = ["apple", "banana", "avocado", "cherry", "apricot", "grape"]

# # Your job: make this:
# # [5, 7, 7]

# result = [len(n) for n in words if n.startswith("a")]

# print(result)


# temps_celsius = [22, 35, 18, 40, 31, 28, 45]

# # Your job: make this:
# # [95.0, 104.0, 87.8, 113.0]

# result = [(c * 9/5) + 32 for c in temps_celsius if c>30]

# print(result)

# sentences = [
#     "i love python",
#     "python is great for ai engineering",
#     "hello world",
#     "i want to get a job",
#     "keep coding every day",
# ]

# # Your job: make this:
# # [6, 6, 4]

# result = [len(s.split()) for s in sentences if len(s.split()) >3]

# print(result)

# numbers = [1, 2, 3, 4, 5, 6]

# # Your job: make this:
# # [3, 4, 9, 8, 15, 12]

# result = [n*2 if n%2==0 else n*3 for n in numbers]

# print(result)

# students = [

#     {"name": "Ravi",   "score": 85},

#     {"name": "Bob",    "score": 42},

#     {"name": "Priya",  "score": 91},

#     {"name": "Sam",    "score": 65},

#     {"name": "Arjun",  "score": 78},

# ]

# result = [s["name"].upper() for s in students if s["score"] > 70]

# print(result)

# numbers = [1, 2, 3, 4, 5]

# # Your job: make this:
# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# result = {n : n**2 for n in numbers}

# print(result)

# cities = ["Delhi", "Mumbai", "Shimla", "Chennai", "Manali"]
# temps  = [42, 35, 18, 38, 12]

# # Your job: make this:
# # {'Delhi': 42, 'Mumbai': 35, 'Chennai': 38}

# result = {k:v for k,v in zip(cities, temps) if v >30}

# print(result)


# students = {
#     "Ravi": 85,
#     "Bob": 55,
#     "Priya": 91,
#     "Sam": 62,
#     "Arjun": 48,
# }

# # Your job: make this:
# # {'Bob': 60, 'Sam': 67, 'Arjun': 53}

# result = {k:v+5 for k,v in students.items() if v<70}

# print(result)

# words = ["python", "ai", "langchain", "agent", "rag"]

# # Your job: make this:
# # {'python': 1, 'ai': 2, 'langchain': 3, 'agent': 2, 'rag': 1}

# result = {w:sum(1 for letter in w if letter in "aeiou") for w in words}

# print(result)

# products = ["phone", "book", "laptop", "pen", "headphones"]
# prices   = [999, 299, 1499, 49, 799]

# # Your job: make this:
# # {'phone': 899.1, 'laptop': 1349.1, 'headphones': 719.1}

# result = {x:y*0.9 for x,y in zip(products,prices) if y >500}

# print(result)

total = sum(n**2 for n in range(1,101))
print(total)  # 338350

numbers = [3, 15, 7, 22, 10, 18]

biggest = max(n*5 for n in numbers)
print(biggest)  # 110

result = list(n for n in range(1,20) if n%3==0)
print(result)  # [3, 6, 9, 12, 15, 18]