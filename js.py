
# # Input data
# # exp = {'talent_skills' : 'Python, Java, C++, GCP' , 'job_skills' : 'python, Machine Learning, C++, GCP-2'};
# exp = {'talent_skills' : 'Serverxen' , 'job_skills' : 'SERVER xen'};
# # exp = {'talent_skills' : 'Python, Java, C++, GCP, Java' , 'job_skills' : 'python, Machine Learning, C++, GCP-2'};        # 33%




# # Extract candidate and job skills
# talent_skills = exp['talent_skills']
# job_skills = exp['job_skills']

# # Preprocess skills by converting them to lowercase and removing spaces
# talent_skills = talent_skills.lower().replace(" ", "")
# print("ttt",talent_skills)
# job_skills = job_skills.lower().replace(" ", "")
# print("jjjj",job_skills)



# # 2. Jaccard Similarity
# def jaccard_similarity(str1, str2):
#     a = set(str1.split(','))
#     print(a)
#     b = set(str2.split(','))
#     print(b)
#     intersection = len(a.intersection(b))
#     print(intersection)
#     union = len(a) + len(b) - intersection
#     print(union)
#     return intersection / union

# jaccard_sim = jaccard_similarity(talent_skills, job_skills) * 100

# print(f"Jaccard Similarity: {jaccard_sim:.2f}%")



















