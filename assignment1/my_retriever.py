
import math
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        #Inverted File Index 
        self.index = index 
        
        #Term weight scheme
        self.termWeighting = termWeighting
        
        # Set up a list for storing the length of each document
        self.doc_length_list = self.docNum(index)*[0]
        
        
        

    # Method for calculating The total number of documents in the collection 
    # sign : (|D|)
    def docNum(self, index):
        doc_list= []
        for term, document in self.index.items(): 
            for docid, count in document.items(): 
                if docid not in doc_list:
                    doc_list.append(docid)
                else:
                    continue
        return len(doc_list)

    # Method for calculating the document frequency dfw of each term w
    # sign : dfw
    def docFreq(self, index):
        df = {}
        for term, documents in index.items():
            df[term] = len(documents)
        return df
    
    #Method for calculating the inverse document frequency of each term w
    # sign : log(|D|/dfw)
    def inverseDocFreq(self,index):
        IDF = {}
        for term, freq in self.docFreq(index).items():
            IDF[term] = math.log(3204/freq) #hard code the number of documents to accelerate running speed
        return IDF
    
    
    # Method for calculating the tf.idf.
    # sign: idf(w,Dd) = tf(w,d) * idf(w,D)
                
    #Method for taking square root of each document length.    
    def squareDocLen(self):
        s_dict = []
        for document in self.doc_length_list:
            s_dict.append(document**0.5)
        self.doc_length_list = s_dict
        return self.doc_length_list
     

    # Method performing retrieval for specified query
    def forQuery(self, query):
        
        #Setup a local index for  method to access
        index = self.index
        
        #access the term weight
        termWeight = self.termWeighting
        
        #local document length
        local_doc_len = self.doc_length_list
        
        
        #set up a list for storing a sum of products of termweights giving query and such termweight in the documents collection.
        # sign: Σ(q*d)
        q_d_sum = self.docNum(index)*[0]
        

        if termWeight == 'binary':
            for term, documents in self.index.items(): #For every term in the outer dictionary
                for document, weight in documents.items(): #For every document and weight in all documents of appearing term
                    self.doc_length_list[document-1] += 1 #count document length for each term
            
            #calling the squaring function
            self.squareDocLen()
                
            for term in query: #For each term in the query
                if term in self.index:  #checking if the term in the index therefore selecting documents
                    documents = self.index[term]  #set up a list for the appearing term in the documents
                    for document in documents: #when term matches for such document, increment 1 in q_d_sum
                        q_d_sum[document-1] += 1
                        
        elif termWeight == 'tf':
            
            for term, documents in self.index.items(): #For every term in the outer dictionary
                for document, weight in documents.items(): #For every document and weight in all documents of appearing term
                    self.doc_length_list[document-1]  += weight**2 #take sqaure of each term weight and add to each document length
            
            #calling the squaring function
            self.squareDocLen()      
                
            for term in query: #For each term in the query
                if term in self.index:  #checking if the term in the index therefore selecting documents
                    documents = self.index[term] #set up a list for the appearing term in the documents
                    for document, weight in documents.items():  #In q_d_sum, the product of query term weight and document term weight are added to the document
                        q_d_sum[document-1] += weight *query[term]
                    
        elif termWeight == 'tfidf':
            
            
            #calling the function to get document frequency list
            self.document_freq_dict = self.docFreq(index)
            
            #calling the function to get inverse document frequency list
            self.idf_dict = self.inverseDocFreq(index)
            
            #calling the function to get tf.idf list
            def tfidf_f1(index):
                local_index = index
                term, docs = local_index[0], local_index[1]
                
                #local method for mapping the list to get tfidf.
                def tfidf_f2(docs):
                    doc, frequency =docs[0], docs[1]
                    return [doc, frequency * self.idf_dict[term]]
                re1 = list(map(tfidf_f2, docs.items()))
                key1 = [li1[0] for li1 in re1]
                value1 = [li1[1] for li1 in re1]
                return [term, dict(zip(key1, value1))]

            #calling the function to get tf.idf list
            re2 = list(map(tfidf_f1, index.items()))
            key2 = [li2[0] for li2 in re2]
            value2 = [li2[1] for li2 in re2]
            self.tfidf_dict = dict(zip(key2, value2))
            
            for term, documents in self.tfidf_dict.items(): #For every term in the outer dictionary
                for document, weight in documents.items(): #For every document and weight in all documents of appearing term
                    self.doc_length_list[document-1]  += weight**2  #take sqaure of each term weight and add to each document length
                
            #calling the squaring function
            self.squareDocLen()
            
            for term in query: #For each term in the query
                if term in self.tfidf_dict: #checking if the term in the tfidf list therefore selecting documents
                    term_tfidf = self.idf_dict[term]*query[term] #get the weight for specific term in the query
                    documents = self.index[term] #set up a list for the appearing term in the documents
                    for document, weight in documents.items(): #In q_d_sum, the product of query term weight and document term weight are added to the document
                        q_d_sum[document-1] += weight * term_tfidf
        
        #Calculating cosine similarity score for relevance between the query and each document.
        sim_score_list = []
        for q_d, d in zip(q_d_sum,self.doc_length_list):
            sim_score = q_d/d
            sim_score_list.append(sim_score)
            
        top_score = sorted(range(len(sim_score_list)), key = lambda i:sim_score_list[i])[-10:]

        result = []
        for i in top_score:
            result.append(i+1)
        return result

        
        
            
        
