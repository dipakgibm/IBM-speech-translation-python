#!pip install ibm_watson wget --required
from ibm_watson import LanguageTranslatorV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

url_lt = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/a8272ee2-9feb-492b-831a-ebdfc778cbf0'

apikey_lt = 'jqlY1A9bEif3ijtCkGKoXPrUjp8MsjVD9GGfx7teJ8g-'
version_lt = '2018-05-01'

authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(
    version=version_lt, authenticator=authenticator)
language_translator.set_service_url(url_lt)


def english_to_french(english_text):
    """
    This function will translates English text to French 
    """
    
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation = translation_response.get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation


def english_to_german(english_to_german):
    """
    This function will translates English text to German 
    """
    translation_response = language_translator.translate(text=english_to_german, model_id='en-de')
    translation = translation_response.get_result()
    german_translation = translation['translations'][0]['translation']
    return german_translation
