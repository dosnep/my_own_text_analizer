class InvertedIndexation:
    inverted_list = {}

    def indexDocument(self, terms, document_id):
        for term in terms:
            if term in self.inverted_list.keys():
                self.inverted_list[term]['frequency'] =  self.inverted_list[term]['frequency']+1
                self.inverted_list[term]['doc_id'].add(document_id)
            else:
                self.inverted_list[term] = {}
                self.inverted_list[term]['frequency'] = 1
                self.inverted_list[term]['doc_id'] = set()
                self.inverted_list[term]['doc_id'].add(document_id)
