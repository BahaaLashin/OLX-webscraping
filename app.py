from flask import Flask
# from .Factories.WebScraping.OlxScraping import OlxScraping
from flask import request, jsonify
from Factories.SendEmail import SendEmail
import pprint
from Factories.WebScraping import OlxScraping
app = Flask(__name__)

@app.route('/olx-scrap', methods=['POST'])
def olx_scraping():
    pass

@app.route("/api/scrap-olx", methods=['POST'])
def scraping():

    keyword = request.form.get('keyword')
    email = request.form.get('email')
    limit = request.form.get('limit')
    scrap = OlxScraping.OlxScraping()

    data = scrap.scrap_and_refresh_data_by_key_word(keyword,limit)
    # SendEmail.SendEmail().send_email('A compilation of some elements from the olx site with '+keyword,data,'bhaaface@gmail.com',email)

    return jsonify(isError= False,
                    message= "Success",
                    statusCode= 200,
                    data= data), 200
   
if __name__ == "__main__":
  app.run()
#   OlxScraping()