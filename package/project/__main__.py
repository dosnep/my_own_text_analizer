from project.InvertedIndexation.inverted_indexation import InvertedIndexation

config = [
    {"terms" : ["this", "is", "a", "test", "this", "a", "test", "test"],
     "document_id" : "doc_1"
     },
    {"terms": ["this", "is", "a", "test", "this", "a", "test", "test"],
     "document_id": "doc_2"
     }
]

for obj in config:
    inverted_indexation = InvertedIndexation()
    inverted_indexation.indexDocument(**obj)

print(inverted_indexation.inverted_list)
