import numpy as np
# Dummy user-item matrix (rows are users, columns are movies)
user_item_matrix = np.array([
    [1, 4, 0, 0, 0],
    [0, 0, 1, 4, 0],
    [0, 0, 0, 0, 3],
    [4, 0, 3, 0, 0],
    [0, 0, 0, 1, 4]
])
# Function to calculate similarity between two users using cosine similarity
def cosine_similarity(user1, user2):
    dot_product = np.dot(user1, user2)
    norm_user1 = np.linalg.norm(user1)
    norm_user2 = np.linalg.norm(user2)
    
    similarity = dot_product / (norm_user1 * norm_user2)
    return similarity
# Function to generate recommendations for a given user
def recommend(user_id, user_item_matrix):
    num_users = user_item_matrix.shape[0]
    recommendations = np.zeros(user_item_matrix.shape[1])
    
    for i in range(num_users):
        if i != user_id:
            similarity = cosine_similarity(user_item_matrix[user_id], user_item_matrix[i])
            recommendations += similarity * user_item_matrix[i]
    # Set already rated items to zero
    recommendations[user_item_matrix[user_id] > 0] = 0
    # Sort recommendations in descending order
    sorted_indices = np.argsort(recommendations)[::-1]
    
    return sorted_indices

# Example: Recommend items for user 2
user_id_to_recommend = 2
recommended_items = recommend(user_id_to_recommend, user_item_matrix)

print(f"Recommendations for User {user_id_to_recommend}:")
for item_id in recommended_items:
    if user_item_matrix[user_id_to_recommend, item_id] == 0:
        print(f"Movie {item_id + 1}")
