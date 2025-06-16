"""
    
    This file configures the connection to the gemini api

    
"""


import os
from google import genai
from dotenv import load_dotenv


class GeminiClient:
    
    def __init__(self):
        
        load_dotenv()
        
        self.api_gemini_key = os.getenv('GOOGLE_GEMINI_API_KEY')
        
        if not self.api_gemini_key:
            
            print("Google gemini api key is not found")
            
        self._connect()
        
    def _connect(self):
        
        """
        
            Connection with gemini method
            
        """
        
        
        try:
            
            self.client = genai.Client(api_key=self.api_gemini_key)
            
            print("Successfully connected to Gemini API")
        
        except Exception as ex:
            
            print(f"Error {ex}")
            
            
            
if __name__ == '__main__':
    
    gemini_client = GeminiClient()
            