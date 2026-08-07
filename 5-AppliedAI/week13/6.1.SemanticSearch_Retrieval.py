"""
Week 13 Day 6 — Semantic Search and Retrieval

This program demonstrates how to:

1. Define a small searchable document collection
2. Load an embedding model
3. Create document embeddings
4. Create a query embedding
5. Calculate cosine-similarity scores
6. Rank and return the top-k documents
7. Evaluate results using expected relevant documents
"""


from dataclasses import dataclass
from sentence_transformers import SentenceTransformer,util

# --------------------------------------------------
# 1. Represent each searchable document
# --------------------------------------------------
@dataclass
class Document:
    document_id: str
    text: str
    category: str

DOCUMENTS = [
    Document(
        document_id="D1",
        text="Track your shipment using the order-status page.",
        category="delivery",
    ),
    Document(
        document_id="D2",
        text="Items may be returned within 30 days for a refund.",
        category="refund",
    ),
    Document(
        document_id="D3",
        text="Update an expired credit card in payment settings.",
        category="billing",
    ),
    Document(
        document_id="D4",
        text="Reset your password from the account recovery page.",
        category="account",
    ),
    Document(
        document_id="D5",
        text="Exchange a damaged product by contacting support.",
        category="product",
    ),
    Document(
        document_id="D6",
        text="Cancel an order before it has been shipped.",
        category="order",
    ),
    Document(
        document_id="D7",
        text="Report an incorrect or duplicate charge on your bill.",
        category="billing",
    ),
    Document(
        document_id="D8",
        text="Request a replacement when an item arrives broken.",
        category="product",
    ),
]

# --------------------------------------------------
# 2. Load an embedding model
# --------------------------------------------------
'''
* multi-qa — trained using many question-and-answer pairs, making it suitable for a short query retrieving a longer answer or passage.
* MiniLM — a compact transformer designed to be faster and lighter than large embedding models.
* L6 — uses six transformer layers.
* cos — designed to work with cosine similarity.
* v1 — version identifier.
'''
MODEL_NAME = "sentence-transformers/multi-qa-MiniLM-L6-cos-v1"

model = SentenceTransformer(MODEL_NAME)


# --------------------------------------------------
# 3. Embed the document collection once
# --------------------------------------------------

document_texts = [document.text for document in DOCUMENTS]

document_embeddings = model.encode_document(
        document_texts,
        convert_to_tensor=True,
        normalize_embeddings=True
)


# --------------------------------------------------
# 4. Search the document collection
# --------------------------------------------------

def semantic_search(query: str, top_k: int = 3) -> list[dict]:
    """
    Return the top-k documents that are most similar to the query.
    """

    if not query.strip():
        raise ValueError("The query cannot be empty.")

    if top_k < 1:
        raise ValueError("top_k must be at least 1.")

    # We cannot return more documents than the collection contains.
    top_k = min(top_k, len(DOCUMENTS))

    query_embedding = model.encode_query(
        query,
        convert_to_tensor=True,
        normalize_embeddings=True,
    )

    # Compare the query with every document.
    similarity_scores = util.cos_sim(
        query_embedding,
        document_embeddings,
    )[0]

    # Sort scores from highest to lowest.
    ranked_indices = similarity_scores.argsort(
        descending=True
    )[:top_k]

    results = []

    for rank, index_tensor in enumerate(ranked_indices, start=1):
        index = index_tensor.item()
        document = DOCUMENTS[index]
        score = similarity_scores[index].item()

        results.append(
            {
                "rank": rank,
                "document_id": document.document_id,
                "category": document.category,
                "text": document.text,
                "score": score,
            }
        )

    return results

# --------------------------------------------------
# 5. Display ranked results
# --------------------------------------------------

def display_results(query: str, results: list[dict]) -> None:
    """
    Print the query and its ranked search results.
    """

    print("=" * 70)
    print(f"Query: {query}")
    print("=" * 70)

    for result in results:
        print(
            f"\nRank {result['rank']} "
            f"| ID: {result['document_id']} "
            f"| Category: {result['category']} "
            f"| Similarity: {result['score']:.4f}"
        )
        print(result["text"])

    print()

# --------------------------------------------------
# 6. Evaluate one query using Precision@k
# --------------------------------------------------

def precision_at_k(
    results: list[dict],
    relevant_document_ids: set[str],
) -> float:
    """
    Calculate the proportion of retrieved results that are relevant.
    """

    if not results:
        return 0.0

    retrieved_ids = {
        result["document_id"]
        for result in results
    }

    relevant_retrieved = retrieved_ids.intersection(
        relevant_document_ids
    )

    return len(relevant_retrieved) / len(results)

# --------------------------------------------------
# 7. Run example searches
# --------------------------------------------------

def main() -> None:
    search_examples = [
        {
            "query": (
                "How do I get my money back after "
                "sending something back?"
            ),
            "expected_ids": {"D2"},
        },
        {
            "query": "My card was charged two times.",
            "expected_ids": {"D7"},
        },
        {
            "query": "I forgot how to access my account.",
            "expected_ids": {"D4"},
        },
        {
            "query": "The product arrived broken.",
            "expected_ids": {"D5", "D8"},
        },
    ]

    top_k = 3

    for example in search_examples:
        query = example["query"]
        expected_ids = example["expected_ids"]

        results = semantic_search(
            query=query,
            top_k=top_k,
        )

        display_results(
            query=query,
            results=results,
        )

        precision = precision_at_k(
            results=results,
            relevant_document_ids=expected_ids,
        )

        print(f"Expected relevant IDs: {sorted(expected_ids)}")
        print(f"Precision@{top_k}: {precision:.2f}")
        print()


if __name__ == "__main__":
    main()