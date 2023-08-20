# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
import random

class GeneralHelp(Action):
    def name(self) -> Text:
        return "action_general_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        user_role = tracker.slots.get("user_role", None)
        
        if user_role is None:
            dispatcher.utter_message(text="Sure! Are you a developer or a client representing an organization?")
        else:
            return [FollowupAction("action_help_with_role")]

# Modified from @Rohit Garg's code https://github.com/rohitkg83/Omdena/blob/master/actions/actions.py
class ActionHelpWithRole(Action):

    def name(self) -> Text:
        return "action_help_with_role"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the value of the first_occurrence_user_type slot
        current_user_type = tracker.slots.get("user_role", None)
   
        if current_user_type == 'developer':
            msg = "Thanks a lot for providing the details. You can join one of our local chapter and collaborate on " \
                    "various projects and challenges to Develop Your Skills, Get Recognized, and Make an Impact. Please " \
                    "visit https://omdena.com/community for more details. Do you have any other questions? "

        elif current_user_type == 'client':
            msg = "Thanks a lot for providing the details. With us you can Innovate, Deploy and Scale " \
                    "AI Solutions in Record Time. For more details please visit https://omdena.com/offerings. Do you have any other questions? "
        else:
            msg = "Please enter either developer or client"

        dispatcher.utter_message(text=msg)

class ResetSlotsAction(Action):
    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots_to_reset = ["user_role"]  # Add the names of the slots you want to reset
        events = [SlotSet(slot, None) for slot in slots_to_reset]
        return events

class ActionJoinClassify(Action):

    def name(self) -> Text:
        return "action_join_classify"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the value of the latest intent 
        last_intent = tracker.slots.get("local_chapter", None)

        # Check if the last intent was 'local_chapter'
         if last_intent and last_intent.lower() in ['local chapter', 'local chapters']:
            dispatcher.utter_message(template="utter_join_chapter")
        else:
            msg = "I'm sorry, I didnt understand your question, Could you please rephrase?"
            dispatcher.utter_message(text=msg)


class ActionEligibilityClassify(Action):

    def name(self) -> Text:
        return "action_eligibility_classify"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the value of the latest intent 
        last_intent = tracker.slots.get("local_chapter", None)

        # Check if the last intent was 'local_chapter'
         if last_intent and last_intent.lower() in ['local chapter', 'local chapters']:
            dispatcher.utter_message(template="utter_local_chapter_participation_eligibility")
        else:
            msg = "I'm sorry, I didn't understand your question. Could you please rephrase?"
            dispatcher.utter_message(text=msg)

 
class ActionCostClassify(Action):

    def name(self) -> Text:
        return "action_cost_classify"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the value of the latest intent 
        last_intent = tracker.slots.get("local_chapter", None)

        # Check if the last intent was 'local_chapter'
         if last_intent and last_intent.lower() in ['local chapter', 'local chapters']:
            dispatcher.utter_message(template="utter_local_chapter_cost")
        else:
            msg = "I'm sorry, I didn't understand your question. Could you please rephrase?"
            dispatcher.utter_message(text=msg)

        