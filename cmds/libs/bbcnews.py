import requests

class GetBBCNews():
    
    def NewsFromBBC(self):
        
        # BBC news api
        # following query parameters are used
        # source, sortBy and apiKey
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "ad5775e7315c448f8cf651438066f941"
        }
        #get own api key from https://newsapi.org/

        main_url = " https://newsapi.org/v1/articles"
    
        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    
        # getting all articles in a string article
        article = open_bbc_page["articles"]
    
        # empty list which will
        # contain all trending news
        results = []
        
        for ar in article:
            results.append(ar["title"])

        #return a string thats easier to see
        news_title = "Today news from BBC：\n"
        for index_resluts in range(len(results)):
            news_title += str(index_resluts + 1) + ". " + results[index_resluts] + '\n'

            
        return news_title