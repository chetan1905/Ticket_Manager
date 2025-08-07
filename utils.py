from enum import Enum

class Ticket_Status(Enum):
    IN_PROGRESS = "In Progress"
    CODE_REVIEW = "Code Review"
    INTERNAL_TESTING = "Internal Testing"
    DEPLOYED = "Deployed"