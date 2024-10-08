# ChatGPT

# Prompt #1
> You're a product manager expert in ATS (application-tracking-systems). What are the main functionalities you think are important? Please, give me the answer in priority order.

# Prompt #2
>What benefits are there using an ATS to consider its use?

# Prompt #3
> What are the most well-known ATS open source? And the commercial? Compare them based on the principal functionalities: Candidate Sourcing & Job Posting Automation, Candidate Evaluation Tools, Candidate Communication & Engagement and Integration with HR Tech Ecosystem

# Prompt #4
> Going back to the first question, now, as an expert software analyst, I'm building an ATS system. List and briefly describe the most important use cases to implement for achieving basic functionality.

# Prompt #5
> Could yo give me the use cases in a UML diagram using PlantUML?

# Prompt #6
>Now, using the previous information with use cases and functionalities, you're a brilliant software architect. You can design, explain and diagramming the different aspects of a software system.

# Prompt #7.A DiagramGPT
> You're an amazing software architect. Could you provide (at a high level) system design of an ATS system like Linkedin or GlassDoor with the following requirements:
>- Event-Driven architecture
>- Each MS has its own database
>- Fronted that communicates through GraphQL
>- Cloud provider is Microsoft Azure.
>
> Include techniques to improve the performance like cache and load balancer

# Prompt #7.B with ChatGPT
> Hello! You're a brilliant software architect with extensive experience in designing and explaining architectural patterns. I'm building a new ATS (application-tracking-systems) system from scratch.
>
>Could you provide me (at a high level) a system design of an ATS system like Linkedin or GlassDoor with the following requirements:
>- Event-Driven architecture 
>- Each MS has its own database
>- Frontend that communicates through GraphQL 
>- All public endpoints must be protected from unauthorized users' access.
>- The cloud provider is AWS.
>- Include techniques to improve the performance when it's necessary or possible like caches and load balancers. 
>
>The ERD entities for the ATS system that you need to take into account are:
>1. **Job** – Represents a job listing.
>2. **Candidate** – Represents an applicant.
>3. **Application** – Represents an application submitted by a candidate for a job.
>4. **Interview** – Represents interviews scheduled for candidates.
>5. **Evaluation** – Represents the evaluation of a candidate.
>6. **Offer** – Represents a job offer extended to a candidate.
>7. **Recruiter** – Represents the user managing the hiring process.
>8. **Communication** – Represents communication between recruiter and candidate.
>
> Please, give me the information with explanations and the necessary code to generate the code using the Diagram library in Python (https://diagrams.mingrammer.com/)

# Prompt #7.B.2
> In the code of the diagram, the microservices didn't give any connection with the gateway, and the load balancer is not in the correct way because should be put in the middle of the gateway.

# Prompt #8 - ChatGPT
> With the last information provided, could you generate me the C4 diagram?