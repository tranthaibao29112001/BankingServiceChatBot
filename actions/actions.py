# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests
import json

save_last_list_result = []

connection_str = "http://tranthaibao29112001.pythonanywhere.com"

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionWhatService(Action):

    def name(self) -> Text:
        return "action_answer_what_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/what_knowledge?service=" + tracker.get_slot("service")

        response = requests.get(url)

        data = response.json()
        data = filter(lambda x: x['product'] == "" and x['property'] == "", data)

        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            dispatcher.utter_message(text=answer)

        return [SlotSet("product", None)]


class ActionWhatServiceProperty(Action):

    def name(self) -> Text:
        return "action_answer_what_service_property"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/what_knowledge?service=" + tracker.get_slot("service") \
              + "&property=" + tracker.get_slot("property")

        response = requests.get(url)

        data = response.json()
        data = filter(lambda x: x['product'] == "", data)

        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            dispatcher.utter_message(text=answer)

        return [SlotSet("property", None), SlotSet("product", None)]


class ActionWhatProductProperty(Action):

    def name(self) -> Text:
        return "action_answer_what_product_property"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/what_knowledge?product=" + tracker.get_slot("product") \
              + "&property=" + tracker.get_slot("property")

        response = requests.get(url)

        data = response.json()

        data = filter(lambda x: x['service'] == "", data)

        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            dispatcher.utter_message(text=answer)
        return [SlotSet("property", None), SlotSet("service", None)]


class ActionWhatProduct(Action):

    def name(self) -> Text:
        return "action_answer_what_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/what_knowledge?product=" + tracker.get_slot("product")

        response = requests.get(url)

        data = response.json()
        data = filter(lambda x: x['property'] == "" and x['service'] == "", data)
        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            dispatcher.utter_message(text=answer)
        return [SlotSet("service", None)]


class ActionWhatProductServiceProperty(Action):

    def name(self) -> Text:
        return "action_answer_what_service_product_property"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/what_knowledge?service=" + tracker.get_slot("service") \
              + "&product=" + tracker.get_slot("product") \
              + "&property=" + tracker.get_slot("property")

        response = requests.get(url)

        data = response.json()

        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            dispatcher.utter_message(text=answer)
        return [SlotSet("property", None)]


class ActionHowService(Action):

    def name(self) -> Text:
        return "action_answer_how_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/how_knowledge?service=" + tracker.get_slot("service")
        response = requests.get(url)

        data = response.json()

        data = filter(lambda x: x['product'] == "" and x['operation'] == "", data)

        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            text_paragraphs = answer.split('\n')
            for paragraph in text_paragraphs:
                paragraph = paragraph.replace('. ', '-')
                dispatcher.utter_message(text=paragraph)
        return [SlotSet("product", None)]


class ActionHowProduct(Action):

    def name(self) -> Text:
        return "action_answer_how_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/how_knowledge?product=" + tracker.get_slot("product")

        response = requests.get(url)

        data = response.json()

        data = filter(lambda x: x['service'] == "" and x['operation'] == "", data)
        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            text_paragraphs = answer.split('\n')
            for paragraph in text_paragraphs:
                paragraph = paragraph.replace('. ', '-')
                dispatcher.utter_message(text=paragraph)

        return [SlotSet("service", None)]


class ActionHowServiceOperation(Action):

    def name(self) -> Text:
        return "action_answer_how_service_operation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/how_knowledge?service=" + tracker.get_slot("service") \
              + "&operation=" + tracker.get_slot("operation")
        response = requests.get(url)

        data = response.json()

        data = filter(lambda x: x['product'] == "", data)

        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            text_paragraphs = answer.split('\n')
            for paragraph in text_paragraphs:
                paragraph = paragraph.replace('. ', '-')
                dispatcher.utter_message(text=paragraph)
        return [SlotSet("operation", None), SlotSet("product", None)]


class ActionHowProductOperation(Action):

    def name(self) -> Text:
        return "action_answer_how_product_operation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        url = connection_str + "/how_knowledge?product=" + tracker.get_slot("product") \
              + "&operation=" + tracker.get_slot("operation")

        response = requests.get(url)

        data = response.json()

        data = filter(lambda x: x['service'] == "", data)

        list_result = list(data)
        if len(list_result) >= 2:
            global save_last_list_result
            save_last_list_result = list_result
            message = "There are {} option for this question:".format(len(list_result))
            buttons = []
            for item in list_result:
                buttons.append(
                    {"title": "{}".format(item['context']), "payload": item['context']})
            dispatcher.utter_message(text=message, buttons=buttons)
        elif len(list_result) == 0:
            dispatcher.utter_message(
                text="I don't have knowledge about this question yet. Please ask something else !.")
        else:
            answer = list_result[0]['desc'][0]
            text_paragraphs = answer.split('\n')
            for paragraph in text_paragraphs:
                paragraph = paragraph.replace('. ', '-')
                dispatcher.utter_message(text=paragraph)

        return [SlotSet("operation", None), SlotSet("service", None)]


class ActionContext(Action):

    def name(self) -> Text:
        return "action_context"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for item in save_last_list_result:
            if item['context'] == tracker.get_slot('context'):
                answer = item['desc'][0]
                text_paragraphs = answer.split('\n')
                for paragraph in text_paragraphs:
                    paragraph = paragraph.replace('. ', '-')
                    dispatcher.utter_message(text=paragraph)

        return []
