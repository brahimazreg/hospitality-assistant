from src.embeddings import get_embedding_model

embeddings = get_embedding_model()

sentences = [
    "What time does breakfast start?",
    "À quelle heure commence le petit-déjeuner ?",
    "متى يبدأ الإفطار؟"
]

vectors = embeddings.embed_documents(sentences)

print("Number of sentences:", len(sentences))
print("Number of vectors:", len(vectors))

for i, vector in enumerate(vectors):
    print(f"Sentence {i + 1}:")
    print("Vector dimensions:", len(vector))
    print("First five values:", vector[:5])
