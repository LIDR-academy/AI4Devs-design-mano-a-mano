from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS
from diagrams.aws.database import RDS, Dynamodb, ElastiCache
from diagrams.aws.network import APIGateway, ALB, Route53
from diagrams.aws.security import Cognito
from diagrams.aws.integration import SQS, SNS, Eventbridge
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Client

with Diagram("ATS System Architecture", show=False):

    client = Client("Frontend Client")

    with Cluster("Frontend"):
        # Load Balancer placed in front of the GraphQL Gateway
        alb = ALB("Load Balancer")
        graphql_gateway = APIGateway("GraphQL API Gateway")
        client >> Edge(label="HTTP/S Requests") >> alb >> graphql_gateway

    with Cluster("Authentication"):
        cognito = Cognito("AWS Cognito")

    # Authentication for the GraphQL Gateway
    graphql_gateway >> Edge(label="JWT Authentication") >> cognito

    with Cluster("Microservices"):
        with Cluster("Job Service"):
            job_service = ECS("Job Service")
            job_db = RDS("Job DB")
            job_service >> job_db

        with Cluster("Candidate Service"):
            candidate_service = ECS("Candidate Service")
            candidate_db = RDS("Candidate DB")
            candidate_service >> candidate_db

        with Cluster("Application Service"):
            application_service = ECS("Application Service")
            application_db = RDS("Application DB")
            application_service >> application_db

        with Cluster("Interview Service"):
            interview_service = ECS("Interview Service")
            interview_db = RDS("Interview DB")
            interview_service >> interview_db

        with Cluster("Evaluation Service"):
            evaluation_service = ECS("Evaluation Service")
            evaluation_db = RDS("Evaluation DB")
            evaluation_service >> evaluation_db

        with Cluster("Offer Service"):
            offer_service = ECS("Offer Service")
            offer_db = RDS("Offer DB")
            offer_service >> offer_db

        with Cluster("Recruiter Service"):
            recruiter_service = ECS("Recruiter Service")
            recruiter_db = RDS("Recruiter DB")
            recruiter_service >> recruiter_db

        with Cluster("Communication Service"):
            communication_service = ECS("Communication Service")
            communication_db = Dynamodb("Communication DB")
            communication_service >> communication_db

    event_bus = Eventbridge("Event Bus")
    
    # Microservices communicating via the Event Bus
    job_service >> event_bus
    application_service >> event_bus
    interview_service >> event_bus
    evaluation_service >> event_bus
    offer_service >> event_bus
    recruiter_service >> event_bus
    communication_service >> event_bus

    # GraphQL Gateway connecting to each microservice directly
    graphql_gateway >> job_service
    graphql_gateway >> candidate_service
    graphql_gateway >> application_service
    graphql_gateway >> interview_service
    graphql_gateway >> evaluation_service
    graphql_gateway >> offer_service
    graphql_gateway >> recruiter_service
    graphql_gateway >> communication_service

    # Cache Layer connected to the GraphQL Gateway for performance optimization
    cache = ElastiCache("Redis Cache")
    graphql_gateway >> cache
    
    # Monitoring all key services using CloudWatch
    cloudwatch = Cloudwatch("Cloudwatch Monitoring")
    cloudwatch >> application_service
    cloudwatch >> event_bus
