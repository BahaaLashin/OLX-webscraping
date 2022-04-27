from abc import ABC, abstractmethod

class IWebsite(ABC):

    @abstractmethod
    def get_data_by_key_word(self, keyword):
        pass
    
    @abstractmethod
    def scrap_and_refresh_data_by_key_word(self, keyword):
        pass
    
    