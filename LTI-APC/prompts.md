# Prompts sent to ChatGPT
You can find the full conversation here: https://chatgpt.com/share/670e0418-7a80-8001-8b70-f78ccd0032eb

## Prompt 1 - Lean Canvas
You are an expert product manager in the ATS (Applicant-Tracking System) systems and you want to create a new system called LTI from scratch. First of all, define with a brief description the LTI software, what is the value added and the competitive advantages. Explain the main functions. Take into account competitors. Do you have questions about some of the functions? Don't you know about competitors? Tell me and I will help you on that. All these details necessary to describe the LTI software and the business model I need in a Lean Canvas diagram

_Result: `LeanCanvas.png`_

## Prompt 2
Yes, now you have to put the focus in the 3 main features for this ATS. Define the 3 more prior uses cases, clear to be converted to UML diagrams later

_Personal comment: these 3 use cases were sent exactly without modifications to DiagramGPT. Only I indicated that the system should use preferably UML._

_Results: `UseCase1.png`, `UseCase2.png` and `UseCase3.png`_

## Prompt 3
Now, I need that you design the data model, detailing the entities involved, the attributes (name and types), main key of each entity, relations between entities and even other things that you think are useful for data modeling the project of LTI.

## Prompt 4
I let you decide, as the expert you are, to indicate what fields must be NOT NULL

_Personal comment: after this answer, I took the definition of this answer + the relationships already answered in the previous time and I sent all to DiagramGPT._

_Result: `DataModel.png`_

## Prompt 5
Now, assume you are an experimented software architect that has to design the high-level architecture system, taking into account where will be hosted our application (AWS), the load balancer, the CDN, the frontend technology, the backend technology and that we will use a microservice architecture. Also, remember to consider other middleware technologies like the API connection between them, queues through Kafka, caching and the authentication. Everything is not mandatory, use what you think it's adequate for LTI

## Prompt 6
Give me the High-Level Architecture Components without description and choosing one of the tecnologies were you propose me more than one

_Personal comment: after this answer, I took the definition the simplified answer for the section 2 + the details answered in the section 3 in the previous time and I sent all to DiagramGPT._

_Result: `HighLevelSystemDesign.png`_

## Prompt 7
Do you know C4 model for diagrams? I need that you design a System context diagram of LTI in C4 model syntax in order to design it later

_Result: `C4SystemContextDiagram.png`_
